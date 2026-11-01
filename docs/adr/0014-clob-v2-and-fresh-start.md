# ADR 0014 — CLOB v2 SDK migration + fresh-start architecture

**Status**: accepted, 2026-05-04
**Phases**: 0 → A → B → C → D → E → F (May 2026 migration)

## Context

By late April 2026, three concurrent pressures forced a structural reset:

1. **Venue cut the V1 CLOB endpoint on 2026-04-28.** Our `venue-sdk`
   0.34.6 wallet flow stopped authenticating; live trading went down. The
   community fork at `github.com/Venue/venue-sdk-v2` exposed a new
   typed-data signing path but was never published to PyPI.
2. **24+ legacy strategies had accumulated** across `config/strategies/`,
   `src/strategies/`, `tests/test_strategies/`, and `logs/` from a year of
   exploration. Most had been retired but never archived; the loader still
   tried to import their source files; configs still referenced strategies
   whose performance was stale or whose realistic-sim numbers had since been
   invalidated by the realistic_fill bug (2026-04-20) or the D-bug stale 0.28
   pattern (2026-04-23).
3. **Future-feature pressure** (web dashboard, registry-driven roster) kept
   colliding with the existing single-process monolith — adding any
   surface meant editing 4 disjoint registries (`STRATEGY_REGISTRY`,
   `STRATEGY_CAPABILITY_REGISTRY`, `STRATEGY_EMOJI`, `config_version`).

Three plan-rewrite cycles in March/April (V1 → V2 → V3) all came back from
review with "needs revision". The fourth try (`MIGRATION_MVM.md`) replaced the
18-stage governance scaffolding with **6 acceptance tests as the success
measure** (one file = one decorated strategy → discoverable; remove a strategy
→ runner still boots; etc.). Acceptance tests + 7 phases → migration
finished in one focused day.

## Decision

### 1. Archive, don't delete (reversibility)

Every legacy file moves through `scripts/migration_archive.py` into
`archive/2026-05-fresh-start/manifest.json` with SHA-256 entries. A symmetric
`scripts/migration_revert.py` undoes any stage by manifest. Off-repo backup at
`~/migration-backup-2026-05/` (5,481 files, 13GB, manifest verified) is the
canonical full-state snapshot before any changes ran. **Why**: the cost of
losing one in-flight log file (paper realistic mode trades, calibration runs)
is huge; the cost of keeping a 200MB archive in-repo for a quarter is zero.

### 2. Strategy registry decorator pattern (`@register_strategy`)

`src/strategies/registry.py` is now the single source of truth. Adding a
strategy = drop a `.py` file with a decorated class. The registry knows
canonical names, aliases, capabilities, and emojis from one place. We
discovered 4 fragmented sub-registries during planning (`STRATEGY_REGISTRY`
class-path map, `STRATEGY_CAPABILITY_REGISTRY` field requirements,
`STRATEGY_EMOJI` runner display map, `config_version._strategy_source` source
tracker) — all four now consume `registry.resolve(name)`. **Why**: removing N
edit sites for one strategy add-action is the cheapest "extension is trivial"
proof we can build.

### 3. Ports in L2 (port-and-adapter clarity)

`src/core/ports/clob.py` defines the `CLOBClient` Protocol. V1 and V2 SDK
wrappers live as concrete adapters at `src/adapters/clob/{v1,v2}.py` behind
this Protocol. Test guard
`tests/test_architecture/test_clob_swap.py::test_no_venue-sdk_outside_adapter`
catches any direct SDK leak. **Why**: the V2 cutover proved the SDK is the
volatile boundary; isolating it lets a future SDK swap (V3, Native API, etc.)
touch one file.

### 4. Six acceptance tests as success measure

Instead of a 18-stage gate sequence, `tests/acceptance/` holds 6 tests that
collectively define "migration complete":

| test                                  | proves                                                         |
| ------------------------------------- | -------------------------------------------------------------- |
| `test_add_strategy_one_file`          | one decorated file → registry knows it; no loader edits needed |
| `test_remove_strategy_runner_starts`  | removing one strategy doesn't break the others                 |
| `test_three_strategy_roster`          | the 3 active names resolve + each reaches `on_tick`            |
| `test_dashboard_endpoint`             | `/runtime/status` returns JSON + api/ doesn't import execution |
| `test_clob_v2_canary` (`CLOB_V2_LIVE=1`) | V2 SDK 5/5 criteria including INSUFFICIENT_BALANCE          |
| `test_polluted_data_cleanup`          | tmp_calibration / pre-D reports / pre-fix paper data archived  |

**Why**: acceptance tests are executable spec. They never disagree with
themselves the way 18 prose stop-gates do.

### 5. Phase 0 backup before any code changes

The first script that ran was `scripts/migration_backup.py --scope=full`
(refuses same-disk targets by default; SHA-256 verified). Phase 0 took ~12
minutes; a restore drill verified 5/5 random files match. **Why**: the
project's pollution sources (D-bug, realistic_fill bug, paper logs from
multiple modes) gitignored most of the affected state. Without an off-repo
snapshot, a misstep would have been irreversible.

### 6. 7 phases (0–F) over 18 stages (V3)

V3 used 18 stages with full governance per stage: review reports, scoring,
checklist updates, "stop gates". V3 reviews kept finding contradictions
between stages; revisions produced more contradictions. The MVM compressed
to 7 phases:
- **0** Backup. **A** Preflight (scripts + tests + V2 wheel).
- **B** Cleanup (archive 378 files: 19 configs, 11 tests, 7 logs, 15
  tmp_calibration dirs, 317 pre-D-fix reports, 7 pre-fix paper files,
  src/btc_bot_c).
- **C** Architecture pivot (registry + Protocol + 12 file archive: legacy
  strategy sources + capability_registry).
- **D** CLOB v2 (Protocol + adapters + factory + facade + terminal refactor +
  V1 archive). Phase D9 canary verified 5/5 criteria including
  `INSUFFICIENT_BALANCE` classification — V2 SDK works.
- **E** Runner decomposition + dashboard + data regen (runner shim
  L4→L6, FastAPI app at L7).
- **F** Final verification + AI-resumability docs.

**Why**: the V3 governance overhead exceeded the engineering work. Compressing
the structure lets the work fit a single focused execution session.

## Consequences

### Positive
- 30-second AI session pickup: `CLAUDE.md` + this ADR + acceptance tests give
  a new Claude/Codex session enough to answer "what does this project do" /
  "how do I add a strategy" / "where's the SDK boundary" without re-deriving.
- Future SDK swap is one file (a new adapter at `src/adapters/clob/v3.py`).
- Future strategy add is one file (decorated class).
- Layer 7 (`src/api/`) is reachable for any frontend (Streamlit, React,
  Grafana) without reaching into execution.

### Negative / accepted debt
- The `src/execution/runner.py` + `twin_runner.py` shims are layer-violations
  (L4 → L6 imports). Acceptable for the transition; planned removal in a
  follow-up that updates all callers to `src.runner.live_runner` directly.
- `src/infra/config_version.py` imports `src.strategies.registry` (L0 → L3).
  Strictly violates layer rules but materially smaller than the previous
  L0 → L4 import via `strategy_loader`. Future cleanup: extract
  source-tracking to L3 or L4.
- Eight pre-existing layer-boundary violations from before the migration are
  still present (`src/execution/realistic_fill/*` → L5 research, etc.). Out
  of scope for this migration; tracked for a future cleanup cycle.

## References

- `docs/tasks/clob_v2_migration/MIGRATION_MVM.md` — full execution plan.
- `docs/tasks/clob_v2_migration/sdk_pin.md` — V2 SDK commit pin
  (`afa772185b233f90b602e0794e9dbe0e44763d9d`) + wheel sha256.
- `archive/2026-05-fresh-start/manifest.json` — every move recorded.
- `runs/clob_v2_canary_*.json` — 5/5 criterion canary outputs.
- 12+ review reports under `runs/master_plan_*_review_*.md`,
  `runs/migration_mvm_review_*.md`, `runs/stage_minus_1_review_*.md`. They
  document why three plan iterations failed and what the MVM corrected.
