#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
옵시디언 볼트용 로컬 RAG MCP 서버.

- 볼트의 .md 노트를 청크 단위로 나눠 로컬 임베딩 모델(sentence-transformers)로 색인합니다.
- Claude Desktop 등 MCP 클라이언트에서 search_notes / read_note / reindex 도구로 사용합니다.
- 임베딩은 전부 로컬에서 계산되며 외부로 전송되지 않습니다 (API 키 불필요).

사용법:
    python server.py                # MCP stdio 서버로 실행 (Claude Desktop이 이 방식으로 호출)
    python server.py --reindex      # 색인만 새로 만들고 종료
    python server.py --test "질문"   # MCP 없이 터미널에서 바로 검색 테스트
"""
import os
import sys
import re
import json
import pickle
import argparse
from pathlib import Path
from dataclasses import dataclass, field

import numpy as np

# ---------------------------------------------------------------------------
# 설정
# ---------------------------------------------------------------------------

DEFAULT_VAULT_PATH = r"C:\Users\KIMJAESUNG\Documents\Obsidian Vault"
VAULT_PATH = Path(os.environ.get("OBSIDIAN_VAULT_PATH", DEFAULT_VAULT_PATH))

# 색인에서 제외할 디렉터리(옵시디언 내부 파일, 이 서버 자신의 폴더 등)
EXCLUDE_DIR_NAMES = {".git", ".obsidian", ".idea", "_mcp-obsidian-rag"}

EMBED_MODEL_NAME = "paraphrase-multilingual-MiniLM-L12-v2"  # 한국어/영어 혼용 지원
CHUNK_SIZE = 800       # 청크당 최대 글자 수
CHUNK_OVERLAP = 100    # 청크 간 겹치는 글자 수
INDEX_CACHE_PATH = Path(__file__).parent / ".rag_index.pkl"

# 노트 상단에 자동 삽입된 MOC 백링크 마커(별도 스킬로 추가된 것) - 검색 노이즈이므로 청크에서 제외
NAV_MARKER_LINE_RE = re.compile(r"^\[\[.*\]\].*<!-- moc-nav -->\s*$", re.MULTILINE)


# ---------------------------------------------------------------------------
# 색인 데이터 구조
# ---------------------------------------------------------------------------

@dataclass
class Chunk:
    rel_path: str
    title: str
    text: str
    vector: np.ndarray = field(repr=False)


class RagIndex:
    def __init__(self):
        self.chunks: list[Chunk] = []
        self._file_meta: dict[str, float] = {}  # rel_path -> mtime
        self._model = None

    # -- 모델 -----------------------------------------------------------
    def _get_model(self):
        if self._model is None:
            from sentence_transformers import SentenceTransformer
            print(f"[rag] 임베딩 모델 로딩 중: {EMBED_MODEL_NAME} (최초 1회는 다운로드 시간이 걸립니다)", file=sys.stderr)
            self._model = SentenceTransformer(EMBED_MODEL_NAME)
        return self._model

    def embed(self, texts: list[str]) -> np.ndarray:
        model = self._get_model()
        vecs = model.encode(texts, normalize_embeddings=True, show_progress_bar=False)
        return np.asarray(vecs, dtype=np.float32)

    # -- 파일 -> 청크 -----------------------------------------------------
    @staticmethod
    def _iter_md_files():
        for p in VAULT_PATH.rglob("*.md"):
            if any(part in EXCLUDE_DIR_NAMES for part in p.parts):
                continue
            yield p

    @staticmethod
    def _title_of(text: str, fallback: str) -> str:
        for line in text.splitlines():
            line = line.strip()
            if line.startswith("# "):
                return line[2:].strip()
        return fallback

    @classmethod
    def _chunk_text(cls, text: str) -> list[str]:
        text = NAV_MARKER_LINE_RE.sub("", text).strip()
        if not text:
            return []
        paragraphs = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
        chunks, cur = [], ""
        for p in paragraphs:
            if len(cur) + len(p) + 2 <= CHUNK_SIZE:
                cur = f"{cur}\n\n{p}" if cur else p
            else:
                if cur:
                    chunks.append(cur)
                if len(p) > CHUNK_SIZE:
                    for i in range(0, len(p), CHUNK_SIZE - CHUNK_OVERLAP):
                        chunks.append(p[i:i + CHUNK_SIZE])
                    cur = ""
                else:
                    cur = p
        if cur:
            chunks.append(cur)
        return chunks

    # -- 색인 빌드/갱신 -----------------------------------------------------
    def load_cache(self):
        if INDEX_CACHE_PATH.exists():
            try:
                with open(INDEX_CACHE_PATH, "rb") as f:
                    data = pickle.load(f)
                self.chunks = data["chunks"]
                self._file_meta = data["file_meta"]
                print(f"[rag] 캐시된 색인 로드: 청크 {len(self.chunks)}개", file=sys.stderr)
            except Exception as e:
                print(f"[rag] 캐시 로드 실패, 새로 색인합니다: {e}", file=sys.stderr)
                self.chunks, self._file_meta = [], {}

    def save_cache(self):
        INDEX_CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
        with open(INDEX_CACHE_PATH, "wb") as f:
            pickle.dump({"chunks": self.chunks, "file_meta": self._file_meta}, f)

    def build(self, force: bool = False):
        if not VAULT_PATH.exists():
            raise RuntimeError(f"볼트 경로를 찾을 수 없습니다: {VAULT_PATH}")

        if force:
            self.chunks, self._file_meta = [], {}

        current_files = {}
        to_embed_texts, to_embed_owner = [], []
        kept_chunks = [] if not force else []
        seen_paths = set()

        for p in self._iter_md_files():
            rel = p.relative_to(VAULT_PATH).as_posix()
            seen_paths.add(rel)
            mtime = p.stat().st_mtime
            current_files[rel] = mtime

            if not force and self._file_meta.get(rel) == mtime:
                # 변경 없음: 기존 청크 재사용
                kept_chunks.extend([c for c in self.chunks if c.rel_path == rel])
                continue

            try:
                text = p.read_text(encoding="utf-8", errors="ignore")
            except Exception as e:
                print(f"[rag] 파일 읽기 실패 {rel}: {e}", file=sys.stderr)
                continue
            title = self._title_of(text, fallback=p.stem)
            for chunk_text in self._chunk_text(text):
                to_embed_texts.append(chunk_text)
                to_embed_owner.append((rel, title))

        # 삭제된 파일의 청크는 자동으로 kept_chunks에서 빠짐 (seen_paths에 없으므로)
        new_chunks = []
        if to_embed_texts:
            print(f"[rag] {len(to_embed_texts)}개 청크 새로 임베딩 중...", file=sys.stderr)
            vectors = self.embed(to_embed_texts)
            for (rel, title), text, vec in zip(to_embed_owner, to_embed_texts, vectors):
                new_chunks.append(Chunk(rel_path=rel, title=title, text=text, vector=vec))

        self.chunks = [c for c in kept_chunks if c.rel_path in seen_paths] + new_chunks
        self._file_meta = current_files
        self.save_cache()
        print(f"[rag] 색인 완료: 노트 {len(seen_paths)}개, 청크 {len(self.chunks)}개", file=sys.stderr)

    def ensure_ready(self):
        if not self.chunks and not self._file_meta:
            self.load_cache()
        if not self.chunks:
            self.build()

    # -- 검색 -------------------------------------------------------------
    def search(self, query: str, top_k: int = 5):
        self.ensure_ready()
        if not self.chunks:
            return []
        q_vec = self.embed([query])[0]
        mat = np.stack([c.vector for c in self.chunks])
        scores = mat @ q_vec  # 이미 정규화된 벡터라 내적 = 코사인 유사도
        top_idx = np.argsort(-scores)[:top_k]
        return [
            {
                "path": self.chunks[i].rel_path,
                "title": self.chunks[i].title,
                "text": self.chunks[i].text,
                "score": float(scores[i]),
            }
            for i in top_idx
        ]


INDEX = RagIndex()


# ---------------------------------------------------------------------------
# MCP 서버
# ---------------------------------------------------------------------------

def build_mcp_server():
    from mcp.server import MCPServer

    mcp = MCPServer("obsidian-rag")

    @mcp.tool()
    def search_notes(query: str, top_k: int = 5) -> str:
        """옵시디언 볼트 노트를 의미 기반(RAG)으로 검색합니다.
        query: 자연어 질문이나 키워드
        top_k: 반환할 결과 개수 (기본 5)
        """
        results = INDEX.search(query, top_k=top_k)
        if not results:
            return "검색 결과가 없습니다."
        lines = []
        for r in results:
            lines.append(
                f"### {r['title']}  (score={r['score']:.3f})\n"
                f"경로: {r['path']}\n\n{r['text']}\n"
            )
        return "\n---\n".join(lines)

    @mcp.tool()
    def read_note(path: str) -> str:
        """볼트 루트 기준 상대 경로로 노트 전체 내용을 읽습니다. search_notes 결과의 '경로' 값을 그대로 사용하세요."""
        p = (VAULT_PATH / path).resolve()
        if VAULT_PATH.resolve() not in p.parents and p != VAULT_PATH.resolve():
            return "볼트 밖의 경로는 읽을 수 없습니다."
        if not p.exists():
            return f"파일을 찾을 수 없습니다: {path}"
        return p.read_text(encoding="utf-8", errors="ignore")

    @mcp.tool()
    def reindex() -> str:
        """볼트 내용이 바뀐 뒤 색인을 다시 만듭니다. 변경/추가/삭제된 파일만 다시 임베딩합니다."""
        INDEX.build(force=False)
        return f"색인 갱신 완료: 노트 {len(INDEX._file_meta)}개, 청크 {len(INDEX.chunks)}개"

    @mcp.tool()
    def list_notes() -> str:
        """색인된 전체 노트 목록(경로)을 반환합니다."""
        INDEX.ensure_ready()
        paths = sorted(INDEX._file_meta.keys())
        return "\n".join(paths) if paths else "색인된 노트가 없습니다."

    return mcp


# ---------------------------------------------------------------------------
# 진입점
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--reindex", action="store_true", help="색인만 새로 만들고 종료")
    parser.add_argument("--test", metavar="QUERY", help="MCP 없이 터미널에서 검색 테스트")
    args = parser.parse_args()

    if args.reindex:
        INDEX.build(force=True)
        return

    if args.test:
        for r in INDEX.search(args.test, top_k=5):
            print(f"\n=== {r['title']} (score={r['score']:.3f}) ===")
            print(f"경로: {r['path']}")
            print(r["text"][:300])
        return

    mcp = build_mcp_server()
    mcp.run()


if __name__ == "__main__":
    main()
