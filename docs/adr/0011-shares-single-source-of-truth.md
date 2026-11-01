# ADR 0011: Shares Single Source of Truth for Live Trade Logs

- Status: Accepted
- Date: 2026-04-19

## Context

On 2026-04-19, live `buy` records for `p1_confident_direction_tight` and
related twins started failing validation because the logged `filled_shares`
did not match the observed wallet token delta. One representative row reported
`filled_shares=2.258418`, while the on-chain token balance moved from
`0.0` to `2.240538`. The mismatch was small in absolute terms, but it was
large enough to trigger `live_buy_filled_shares_mismatch` and route the row
to `_unverified.jsonl`.

This is the same class of error that already affected live cost accounting:
strategy intent and SDK/WS responses are useful signals, but they are not the
ground truth for canonical trade logs. The canonical record must reflect the
adapter-observed balance delta.

## Decision

- `live_buy.filled_shares` must be derived from `token_after - token_before`.
- `live_buy.shares` must mirror that same value.
- `live_meta` may retain SDK return values and WebSocket fill events, but only
  as diagnostics.
- `fak_returned_shares`, bridge-confirmed shares, and requested shares must not
  override the balance delta in the canonical record.
- The validator must treat exact agreement with the balance delta as the pass
  condition for live buy share accounting.

## Consequences

Positive:

- canonical live logs become internally consistent and replayable
- small overfills and bridge quirks no longer poison the trusted stream
- downstream settlement and PnL checks can trust the entry shares field without
  unpacking diagnostics

Negative:

- rows with missing or stale post-trade balance reads will be quarantined
- operators lose the convenience of “best available” share estimates in the
  canonical field, but keep those numbers in `live_meta`

Operationally, this reduces write-time ambiguity and lowers the chance that a
valid fill is mislabeled as contaminated because a non-authoritative source won
the field merge.

## Notes

The WebSocket bridge inversion issue remains a separate problem. This ADR does
not attempt to repair price reporting or bridge semantics; it only defines the
canonical source for live share accounting.
