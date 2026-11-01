# ADR 0007: Stale Archive Buckets

- Status: Accepted
- Date: 2026-04-19

## Context

The repository still exposed retired strategy code and historical research in
active top-level locations such as `src/`, `docs/problems/`, and
`docs/research/`. That made new sessions pay an unnecessary discovery cost and
blurred the line between active runtime assets and historical material.

Phase 1 already cataloged archived families in `docs/DATA_PROVENANCE.md`, and
Phase 8 requires moving stale code, docs, and models into a clear archive
layout with link updates.

## Decision

Create typed archive buckets under `docs/archive/`:

- `docs/archive/problems/`
- `docs/archive/research/`
- `docs/archive/strategies/`
- `docs/archive/analysis/`
- `docs/archive/models/`

Move clearly retired assets there with `git mv`, preserving history.

Keep active or ambiguous families out of scope for this phase. In particular,
do not archive active strategy families such as `late_entry` or
`bayesian_arbitrage`, and do not force-move untracked artifacts that are not
present in the phase worktree.

## Consequences

- Active repo surfaces become easier to scan.
- Historical material remains available with preserved git history.
- Some archived documents still mention pre-archive paths as historical
  references; active pointers should prefer the new archive locations.
- Future restoration should happen explicitly with `git mv` in a dedicated
  change, not by reintroducing ad hoc copies.
