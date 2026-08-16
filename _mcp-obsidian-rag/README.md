# Obsidian RAG MCP 서버

이 볼트의 노트를 로컬 임베딩으로 색인해서, Claude Desktop 같은 MCP 클라이언트에서 의미 기반으로 검색할 수 있게 해주는 서버입니다. 임베딩은 전부 내 컴퓨터에서 계산되고 외부로 전송되지 않습니다 (API 키 불필요).

## 1. 설치 (Windows, 최초 1회)

PowerShell 또는 명령 프롬프트를 열고:

```powershell
cd "C:\Users\KIMJAESUNG\Documents\Obsidian Vault\_mcp-obsidian-rag"
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

`pip install` 단계에서 sentence-transformers와 함께 torch가 설치되며 용량이 꽤 큽니다(수백 MB, 몇 분 소요). 최초 색인 실행 시 임베딩 모델도 한 번 다운로드됩니다.

## 2. 색인 만들기 + 터미널에서 테스트

```powershell
python server.py --reindex
python server.py --test "스프링 의존성 주입 관련 노트 알려줘"
```

검색 결과가 노트 제목/경로/유사도 점수와 함께 출력되면 정상입니다. 이후 노트를 수정하거나 추가하면 `--reindex`를 다시 실행하거나, Claude Desktop에서 `reindex` 도구를 호출하면 됩니다 (바뀐 파일만 다시 임베딩해서 빠릅니다).

## 3. Claude Desktop에 연결

설정 파일 위치: `%APPDATA%\Claude\claude_desktop_config.json`

이 파일을 열어 `mcpServers`에 아래 항목을 추가하세요 (경로의 `.venv\Scripts\python.exe`는 위에서 만든 가상환경의 파이썬입니다):

```json
{
  "mcpServers": {
    "obsidian-rag": {
      "command": "C:\\Users\\KIMJAESUNG\\Documents\\Obsidian Vault\\_mcp-obsidian-rag\\.venv\\Scripts\\python.exe",
      "args": [
        "C:\\Users\\KIMJAESUNG\\Documents\\Obsidian Vault\\_mcp-obsidian-rag\\server.py"
      ],
      "env": {
        "OBSIDIAN_VAULT_PATH": "C:\\Users\\KIMJAESUNG\\Documents\\Obsidian Vault"
      }
    }
  }
}
```

저장 후 Claude Desktop을 완전히 종료했다가 다시 켜세요. 대화창 하단 도구 목록에 `obsidian-rag`가 보이면 연결된 것입니다.

## 4. 사용 예시

Claude Desktop 대화에서 그냥 이렇게 물어보면 됩니다:

> "옵시디언 노트에서 JWT 관련 내용 찾아줘" → `search_notes` 도구 호출
> "그 노트 전체 내용 보여줘" → `read_note` 도구 호출
> "노트 수정했으니 다시 색인해줘" → `reindex` 도구 호출

## 제공 도구

| 도구 | 설명 |
| --- | --- |
| `search_notes(query, top_k=5)` | 의미 기반 검색. 청크 텍스트 + 점수 반환 |
| `read_note(path)` | 노트 전체 내용 읽기 (검색 결과의 경로 그대로 사용) |
| `reindex()` | 변경분만 다시 임베딩해서 색인 갱신 |
| `list_notes()` | 색인된 노트 경로 전체 목록 |

## 참고

- `.git`, `.obsidian`, `.idea`, 이 폴더(`_mcp-obsidian-rag`) 자체는 색인 대상에서 제외됩니다.
- 색인 캐시는 `.rag_index.pkl`에 저장됩니다. 문제가 생기면 이 파일을 지우고 `--reindex`를 다시 실행하면 됩니다.
- 임베딩 모델은 한국어/영어를 함께 지원하는 `paraphrase-multilingual-MiniLM-L12-v2`를 씁니다. 검색 품질을 더 올리고 싶으면 `server.py`의 `EMBED_MODEL_NAME`을 더 큰 다국어 모델로 바꿀 수 있어요(대신 느려집니다).
