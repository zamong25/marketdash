# ADR 0003: Write-Time Trade Log Validation and Quarantine

- Status: accepted
- Date: 2026-04-19

## Context

Trade logs are the project's audit trail, but the repository has already
seen two classes of contamination:

- live fills where `filled_shares` was not the authoritative adapter
  output
- live cost accounting where the log fell back to an estimated cost
  source instead of the observed wallet delta

Those records are useful for forensics, but they should not be mixed into
the canonical trade stream that powers daily stats, replay, and
calibration.

At the same time, older contaminated rows already exist in `logs/*/`.
Deleting them would erase evidence. Leaving them in place without a
formal quarantine path would keep analysis noisy.

## Decision

Add a write-time validator layer for trade records:

- canonical records go through `TradeLogValidator`
- valid records remain in `logs/<strategy>/trades_YYYY-MM-DD.jsonl`
- invalid records are diverted to
  `logs/<strategy>/trades_YYYY-MM-DD.<record_type>_unverified.jsonl`

Also add a one-shot quarantine script for existing logs:

- scan `logs/*/trades_*.jsonl`
- quarantine invalid rows to
  `trades_YYYY-MM-DD.quarantine.jsonl` in the same directory
- append an incident row to
  `data/quarantine/CONTAMINATION_REGISTRY.md`

## Why this shape

1. It blocks contamination at the point of write instead of relying on
   downstream filters.
2. It preserves the original row for auditability when a record fails.
3. It keeps canonical logs small and trustworthy while still making bad
   rows easy to inspect.
4. It matches the repository's provenance model: canonical data stays in
   place, quarantined data is explicitly labeled, and the registry gives
   operators a single ledger of incidents.

## Consequences

Positive:

- trade-log consumers can treat the canonical stream as validated by
  default
- suspicious records remain recoverable
- the quarantine registry records what was found and where it went

Negative:

- an extra write path is introduced for invalid rows
- existing contaminated logs require a separate cleanup pass
- validators need to stay aligned with the record schema as execution
  changes

## Scope

This phase validates cost and share accounting only:

- `live_buy` is checked against balance delta and token delta
- `live_settlement` is checked against the corresponding buy and the
  realized pnl math
- `live_redemption_confirmation` is checked against the buy and the
  redemption proceeds math
- `paper_*` records get shape checks only

That keeps the rule set focused on the contamination observed in Phase 4
without turning the validator into a full market truth engine.

## Rejected alternatives

### Keep filtering only in analysis code

Rejected because contaminated rows would still be written into the
canonical stream and could leak into new consumers.

### Mutate or delete bad rows in place

Rejected because the repository treats logs as evidence. We want
quarantine, not silent erasure.

### Make quarantine the default destination for all records

Rejected because valid records need a stable canonical path for daily
operations, runner restore, and analysis tooling.

## Rollout

1. Introduce the validator and writer wrapper.
2. Route all trade-log writes through the wrapper.
3. Add the quarantine script and registry template.
4. Run the dry-run quarantine scan to enumerate existing contamination.
5. Review the dry-run report before any destructive cleanup is run.

## Notes

The canonical writer should remain the only place that decides whether a
record is verified or unverified. Batch quarantine is for legacy logs
already on disk.
