# ADR 0009: Memory Curation and Re-entry

- Status: Accepted
- Date: 2026-04-19
- Phase: Foundation Phase 10

## Context

Foundation Phases 1-9 changed the project's architecture, data layout,
execution engine names, validation gates, and archive map. A fresh session
needs a short, reliable path into the current truth without treating old
memory fragments as authoritative.

## Decision

- Add a fixed re-entry guide at the top of `MEMORY.md`.
- Treat `docs/ARCHITECTURE.md`, `docs/TERMINOLOGY.md`,
  `docs/DATA_PROVENANCE.md`, and `docs/CONTRIBUTING.md` as the truth set.
- Store memory entries under `memory/` with frontmatter status.
- Make new Phase 1-9 memory entries pointer-only.
- Validate active memory links with `scripts/check_memory_links.py`.

## Consequences

- New sessions can start from a bounded read path.
- Memory entries become hints, not a competing source of truth.
- Future stale entries can be marked `superseded_by_phase_N` or `archived`
  without deleting their history.

## Validation

- `MEMORY.md` stays under 200 lines.
- Active memory entry links must exist.
- Fresh-session smoke imports `src.core`, `src.execution`, `src.strategies`,
  and `src.validation`.
