# ADR 0001: Unified ExecutionEngine

## Status

Accepted

## Context

Before Phase 2, the repository had four execution lineages:

- `backtest` via `src/research/replay_engine.py`
- `realistic_sim` via ad hoc research scripts
- `paper` via `src/execution/engines/paper_engine.py`
- `live` via `src/execution/engines/live_engine.py`

They shared strategy ideas but not a common execution contract. Fill
prices, costs, latency, and rejection reasons diverged by tier, which made
cross-tier comparisons fragile.

## Decision

Introduce `src/core/execution/engine.py` with:

- `ExecutionEngine` protocol
- `ExecutionResult` dataclass

and implement four concrete engines:

- `BacktestExecutionEngine`
- `RealisticSimExecutionEngine`
- `PaperExecutionEngine`
- `LiveExecutionEngine`

The concrete implementations live under `src/execution/engines/`. Phase 10
removed the temporary `src/execution/paper_executor.py` and
`src/execution/live_executor.py` shim modules, so new code imports from
`src.execution.engines`.

## Why This Shape

1. It creates one result schema for success, partial fill, and rejection.
2. It lets research scripts reuse execution math instead of carrying their
   own copy.
3. It keeps mode-specific behavior in separate implementations rather than
   burying `if mode == ...` branches inside one monolith.

## Rejected Alternatives

### One executor with mode switches

Rejected because it would keep `backtest`, `realistic_sim`, `paper`, and
`live` tightly coupled inside one class and make accounting regressions
harder to isolate.

### Leave research scripts separate

Rejected because Phase 2 is specifically about reducing fill/cost drift
between runtime and research tiers.

### Rewrite Runner and OrderManager around `ExecutionResult` immediately

Rejected for the Phase 2 landing because the repository already had broad
test coverage for `execute_order()` / `fast_execute_order()` returning
`Fill | None`. Phase 10 kept those methods on the concrete engines and
removed the import-path shims.
