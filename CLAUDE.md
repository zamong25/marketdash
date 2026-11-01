# marketdash — project map for AI agents

## System (one paragraph)
5-minute binary-market auto-trading stack. A 1-second collector writes
`data/live/realtime/latest.json` from the spot feed, the venue order book and
the settlement oracle. Strategies read snapshots through a shared `Strategy`
Protocol and emit `Signal` objects. A runner routes signals through paper /
live / twin execution engines, holds positions to settlement, and redeems
them. A FastAPI read-only API feeds the React dashboard. This public copy
keeps structure only: signatures, one-line docstrings, ADRs and screenshots.

## Module layout (Layer 0 → 7; a layer imports only layers below it)
- **L0 `src/infra/`** — Config, Telegram, heartbeat, atomic JSON IO.
- **L1 `src/adapters/clob/`** — V1 + V2 venue SDK wrappers behind one Protocol. SDK imports MUST live here only.
- **L2 `src/core/`** — `Strategy` Protocol, domain types, enums.
- **L3 `src/strategies/`** — Strategy classes + `registry.py`. One file = one strategy = one `@register_strategy`.
- **L4 `src/execution/`** — Order manager, safety guard, execution engines (paper / live / realistic_sim), settlement manager.
- **L5 `src/validation/`** — Replay engines, sim runner, paper↔live parity scoring.
- **L6 `src/runner/`** — `live_runner.py`, `twin_runner.py` (orchestrators).
- **L7 `src/api/`** — FastAPI dashboard endpoints. MUST NOT import L4.
- **`frontend/dashboard/`** — React/Vite dashboard; API contract in `docs/adr/0015-react-dashboard-contract.md`.

## Where to find
| concept | file/dir |
| --- | --- |
| Add a new strategy | `src/strategies/{name}.py` + `@register_strategy` |
| Strategy Protocol | `src/core/protocol.py` |
| SDK factory + bootstrap validate | `src/adapters/clob/factory.py` |
| Live runner | `src/runner/live_runner.py` |
| Dashboard API entry | `src/api/server.py` |
| Acceptance tests (executable spec) | `tests/acceptance/` |
| Architecture boundary tests | `tests/test_architecture/` |
| Decisions | `docs/adr/` |

## Rules
- Tick interval is 1 second. `latest.json` schema is shared with the collector — do not change its shape unilaterally.
- Paper / live share the strategy + order-manager spine; only the execution engine differs.
- Kill switch: `touch runs/KILL_SWITCH`.
- Never present a backtest hit-rate as a PnL guarantee (N=0 is not evidence).
- Cap planning at one round; route follow-ups into ADRs / acceptance tests, not plan rewrites.
- No silent scope shrink: every reduction is flagged in the conversation.
