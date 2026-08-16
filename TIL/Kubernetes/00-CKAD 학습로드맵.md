[[0-Kubernetes MOC.md]] · #kubernetes #ckad <!-- moc-nav -->

# 📋 CKAD 학습 로드맵

> 시작일: 2026-08-15 (2026-08-16 CKA → CKAD로 목표 정정) · 목표: CKAD(Certified Kubernetes Application Developer) 취득
> 학습 방식: 개념 정리 + Q&A (기존 노트를 확장하며, 채팅으로 질문하며 진행)

## 도메인별 비중 및 진행 상태
| 순서 | 도메인 | 비중 | 상태 | 노트 |
|---|---|---|---|---|
| 1 | 애플리케이션 설계와 빌드 | 20% | 🟡 진행 중 | [[01-애플리케이션_설계와_빌드]] |
| 2 | 애플리케이션 배포 | 20% | 🟡 진행 중 | [[02-애플리케이션_배포]] |
| 3 | 관찰가능성과 유지보수 | 15% | 🟡 진행 중 | [[03-관찰가능성과_유지보수]] |
| 4 | 환경, 설정과 보안 (최고 비중) | 25% | ⬜ 예정 | [[04-환경설정과_보안]] |
| 5 | 서비스와 네트워킹 | 20% | 🟡 진행 중 | [[05-서비스와_네트워킹]] |

## 학습 순서 메모
④ 환경/설정/보안이 비중이 가장 높으니(25%) 다음 우선순위로 ConfigMap/Secret/ResourceQuota/SecurityContext부터 채우는 걸 권장. 이미 진행 중인 ①②③⑤는 실습 위주로 계속 보강.

## 진행 로그
- 2026-08-15: (CKA로 착각하고 시작) 클러스터 아키텍처, Pod/RS/Deployment, Service 기초 정리.
- 2026-08-15: Pod 배포 이론 보강 (라이프사이클, restartPolicy, Probe 3종, Init Container, Graceful Shutdown).
- 2026-08-16: **목표를 CKA → CKAD로 정정.** 볼트 구조를 CKAD 5개 도메인 기준으로 재편:
  - Pod 기초/라이프사이클/멀티컨테이너 패턴/Init Container → ① 애플리케이션 설계와 빌드
  - ReplicaSet/Deployment/롤링업데이트 → ② 애플리케이션 배포
  - Probe 3종 + 로그/디버깅 명령어 → ③ 관찰가능성과 유지보수
  - Service 기초 → ⑤ 서비스와 네트워킹
  - 클러스터 아키텍처(kubeadm/HA/etcd/RBAC) 등 CKA 전용 내용은 `CKA-참고(선택)/` 폴더로 이동 (참고용 보관, CKAD 범위 아님)

## 다음 세션에서 할 일
- [ ] ④ 환경/설정/보안: ConfigMap, Secret, ResourceQuota/requests·limits, ServiceAccount, SecurityContext 학습 시작 (비중 최고)
- [ ] ① Job/CronJob, 볼륨(emptyDir 등) 채우기
- [ ] ② 배포 전략(블루/그린, 카나리) 실습 예제, Helm/Kustomize 기초
- [ ] ③ API deprecation, CLI 모니터링 도구
- [ ] ⑤ Ingress, NetworkPolicy 실습
- [ ] 각 도메인 노트 끝의 확인 질문들 답변/토론
- [ ] 실습 환경(minikube/kind, 또는 Docker Desktop k8s) 계속 활용
