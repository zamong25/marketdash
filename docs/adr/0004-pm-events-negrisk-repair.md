# 0004: Repair MultiOutcome Complement Inversion in pm_events Depth

**Status:** Accepted
**Date:** 2026-04-19
**Phase:** Foundation Phase 5

## Context

`pm_events` depth snapshots were being consumed directly by realistic simulation and paper replay. A subset of MultiOutcome windows contained inverted complement books, which surfaced as crossed depth (`best_bid >= best_ask`) or impossible no-arb sums against the complementary token. That contamination propagated into fill-price estimates, backtests, and paper diagnostics.

Raw pm_events files are evidence and must remain intact. Repairing only at the trade-log layer was not enough, because the poisoned depth snapshots were still the upstream source for simulation.

## Decision

- Keep raw `pm_events` inputs immutable.
- Write raw depth snapshots to `data/raw/pm_events*/`.
- Repair inverted MultiOutcome depth snapshots from the complementary token's book and write the repaired view to `data/processed/depth*/`.
- Send snapshots that still cannot be reconstructed to `data/quarantine/pm_events_unrepairable*/`.
- Update historical simulation/replay readers to consume processed depth instead of raw depth.

## Alternatives Considered

- Filter only at the trade-log validator:
  too late; simulation inputs remain poisoned.
- Mutate raw `pm_events` files in place:
  destroys provenance and makes future debugging harder.
- Ignore crossed snapshots during replay:
  avoids the worst rows but throws away recoverable depth and leaves silent gaps.
- Repair only in each consumer:
  duplicates logic and guarantees drift across replay, paper, and research paths.

## Consequences

Positive:

- Historical replay and realistic simulation read one cleaned depth source.
- Raw vs processed provenance becomes explicit.
- Unrepairable rows stay inspectable in quarantine.

Negative:

- Extra storage for raw, processed, and quarantine depth outputs.
- One additional repair/backfill step is required for existing history.
- Live `live_book.json` remains on the legacy path until a later phase updates live consumers.

## Rollback

- Point historical readers back to the previous raw depth root.
- Stop running the repair/backfill script.
- Leave raw files untouched; no reverse migration is needed because raw remains the source of truth.

## Validation

- Unit tests for healthy, crossed, sum-check, partial, and unrepairable snapshots.
- `repair_pm_events_history.py --dry-run` summary of repaired and unrepairable rows.
- Crossed-book rate measurement before and after repair.

## Links

- `docs/tasks/helm_project_foundation/phase_5_multi_outcome_fix.md`
- `src/data/pm_events/README.md`
- `scripts/repair_pm_events_history.py`
- `tests/test_data/test_pm_events/test_multi_outcome_repair.py`
