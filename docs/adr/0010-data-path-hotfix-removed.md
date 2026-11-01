# ADR 0010: data/live/realtime/ symlink hotfix 제거

- Status: Accepted
- Date: 2026-04-19
- Task: helm_live_hardening/01

## Context

2026-04-19 Phase 3 (data layout v2) 머지 후 코드가 `data/realtime/latest.json`
→ `data/live/realtime/latest.json` 로 경로를 바꿨으나, launchd 로 관리되는
콜렉터와 이미 돌고 있던 baseline twin 은 재시작되지 않아 옛 코드를
메모리에 유지한 채 옛 경로에서 동작. 신규 기동한 tight twin 은 새 코드를
로드해 새 경로를 찾다가 파일이 없어 silent no-op 상태로 stall.

즉시 복구를 위해 2026-04-19 21:19 KST 에 다음 심볼릭 링크를 임시로 생성:

```
data/live/realtime/latest.json -> ../../realtime/latest.json
```

## Decision

- 2026-04-19 21:43-21:44 KST 에 아래 순서로 hotfix 를 제거하고 경로를 완결:
  1. Baseline twin kill (`in_position=False` 확인 후)
  2. 심볼릭 링크 삭제
  3. Collector kill → launchd `KeepAlive=true` 가 새 프로세스로 자동 재시작
  4. 새 경로에 실제 파일이 생기는지 확인 (약 5 초 소요)
  5. Baseline twin 재기동 → 새 경로 read
- 이후 심볼릭 링크 유지 금지. 마이그레이션 완료 후 재생성도 금지.

## Consequences

- 데이터 공백: 약 5 초 (콜렉터 재시작). 이 구간 baseline, tight 모두 snapshot
  없음.
- Baseline tick 공백: kill ~ WS 재연결까지 약 20 초 + strategy warmup 30 초 =
  signal 가능 시점까지 ~50 초. 이 구간 signal 놓쳤을 수 있음.
- 콜렉터 launchd plist 의 stdout/stderr 경로는 여전히 `data/realtime/_logs/`.
  별도 cleanup 으로 이관 예정 (task 01 스코프 밖).
