# ADR 0012: live_book.json dumps MultiOutcome-repaired payload

- Status: Accepted
- Date: 2026-04-19
- Related: ADR 0004 (pm-events-multi_outcome-repair), `memory/ws_bridge_operational_status.md`

## Context

Phase 5 added MultiOutcome complement-inversion repair to the pm_events pipeline,
but the repair was only applied to records bound for
`data/processed/depth*` parquet. The `live_book.json` consumer file — read
in real time by `LiveBookProvider` and consumed by `run_paper.py` and
`run_twin.py` for the realistic fill model — was still dumped straight
from the raw in-memory books in `PMEventsService._books`.

**Observed failure:** 2026-04-19 13:33 UTC, window
`btc-updown-5m-1776605400`:
- `live_meta.ask_price_at_order` = **0.49** (preflight snapshot from
  `live_book.json`)
- Live actual CLOB fill = **0.8876** (balance-delta ground truth)
- Paper realistic fill used 0.49 as fill_price → paper settled +$0.98 vs
  live +$0.25 (40¢ fill-price gap).

The raw `live_book.json` contained an inverted complement book that
never passed through `repair_snapshot`. Every paper trade today sampled
that file; most had small enough inversions to go unnoticed.

## Decision

`PMEventsService` now caches the *processed* (repaired-or-no-repair-needed)
payload per token in `self._latest_processed_books`, and
`_maybe_dump_live_book` writes `live_book.json` from that cache instead
of directly from `self._books`.

- A token stays out of `live_book.json` until its first successful
  repair / no-repair-needed snapshot (no raw leakage during bootstrap).
- If a subsequent snapshot is quarantined (unrepairable), the cache
  retains the last known good state — `live_book.json` goes stale for
  that token rather than regressing to bad data.
- The repair logic, cadence, and atomic-rename contract are unchanged;
  only the data source for the dump is swapped.

## Consequences

- Paper realistic fill now reads repaired prices. Paper / live fill-price
  divergence caused by complement inversion is eliminated.
- Regression test `test_service_live_book_uses_repaired_payload` guards
  the invariant: after repair, every token's best_bid < best_ask in the
  dump.
- Existing analysis that re-read historical `live_book.json` snapshots
  (none committed to git; file is gitignored) would still have the old
  contaminated values — prefer `data/processed/depth*` for any
  historical work.

## Rollout

- Fix landed on `main` 2026-04-19 23:xx KST.
- `scripts/multi_collector.py` (launchd-managed) restarted to load the
  new code. Auto-restart verified via launchctl.
- Next paper trade entry against `live_book.json` should see the new
  repaired payload path.
