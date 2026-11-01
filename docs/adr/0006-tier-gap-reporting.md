# ADR 0006: Tier Gap Reporting

- Status: Accepted
- Date: 2026-04-19
- Phase: Foundation Phase 7

## Context

- The repository now produces four comparable execution tiers:
  `backtest`, `realistic_sim`, `paper`, and `live`.
- Twin paper/live runs made it easy to inspect single windows manually, but
  not to quantify daily drift in fill rate, win rate, PnL, or slippage.
- Calibration decisions depend on daily paired comparisons, not on ad hoc
  log spelunking.
- Runtime artifacts are split between the tracked worktree and a parent repo
  that may own the real `logs/` and legacy `data/realtime/` inputs.

## Decision

- Add `src/research/gap_report.py` as the canonical daily gap-report module.
- Compare tiers on paired `(strategy_name, window_slug)` keys.
- Treat `live` as the default baseline tier.
- Persist one human-readable Markdown report and one structured parquet file
  per day under `data/derived/reports/`.
- Mirror settlement precedence already used by runner recovery:
  `redemption_confirmation` > `redemption_completed` > `settlement`.
- Mark alerting days at the top of the report and append one summary line to
  `data/derived/reports/ALERTS.md`.
- Allow input auto-discovery when running inside `.worktrees/...` so the
  worktree can read parent-repo runtime data without writing back into it.

## Alert Thresholds

- Mean absolute per-trade PnL gap > 20% of the baseline absolute mean
  per-trade PnL reference.
- Absolute win-rate gap > 2 percentage points.
- Absolute fill-rate gap > 5 percentage points.
- Pair coverage < 80% of baseline windows.

## Alternatives Considered

- Notebook/manual JSONL comparison:
  too slow, inconsistent, and not append-only.
- Real-time dashboard first:
  useful later, but larger than the daily calibration gate.
- Telegram alert integration in this phase:
  deferred to a later phase.
- Writing derived gap fields back into trade logs:
  rejected because logs are source artifacts and must stay immutable.

## Consequences

- Daily recalibration gets a repeatable, operator-readable scorecard.
- Coverage loss becomes explicit instead of silently disappearing into
  missing windows.
- Reports can run from a clean worktree even when real runtime artifacts
  live in the parent repo.
- Some tier combinations can collapse to near-zero gap when the paper tier
  itself already runs in realistic mode; the report keeps that visible
  rather than inventing synthetic separation.
- Backtest coverage depends on either structured derived rows or an
  importable strategy implementation in the active worktree.

## Validation

- Unit tests cover metric aggregation, settlement precedence, alert
  thresholds, report writing, and derived backtest-row ingestion.
- `scripts/daily_gap_report.py --date <day>` writes both Markdown and
  parquet outputs.

## Links

- `docs/tasks/helm_project_foundation/phase_7_gap_report.md`
- `src/research/gap_report.py`
- `scripts/daily_gap_report.py`
- `tests/test_research/test_gap_report.py`
