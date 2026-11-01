# ADR 0013: Universal strategy simulator

- Status: Accepted
- Date: 2026-04-20
- Task: post-live-hardening tooling

## Context

Until now, every strategy variant that needed offline PnL projection
shipped its own analysis script under ``docs/analysis/p1_*_sim_v2.py``.
Each script:

1. Re-implemented the strategy's selection rule in Python (scan window,
   price gate, BTC move check, velocity check, …).
2. Called ``RealisticSimExecutionEngine`` directly to simulate fills.
3. Emitted a bespoke markdown report.

Two problems compounded:

- **Rule drift.** Every new strategy (or variant) required a matching
  sim script, and the hand-coded rule usually lagged the real
  ``strategy.on_tick`` implementation by days or weeks. The offline
  sim's numbers no longer matched what the live strategy would actually
  trigger on.
- **Scope creep.** Adding a filter to one strategy (e.g. the trend
  filter for P1) forced an edit to at least three places: strategy
  class, live config, sim script.

We needed one simulator that:

- Accepts any strategy via its TOML config.
- Calls the *actual* ``strategy.on_tick`` — no rule re-implementation.
- Routes emitted signals through the current production
  ``RealisticSimExecutionEngine`` with the same effects config that
  paper/live use.
- Writes a report that's directly comparable to live telemetry.

## Decision

Ship two files:

- ``src/research/sim_runner.py`` — core module:
  - ``HistoricalSnapshotBuilder`` — reconstructs
    ``MarketSnapshot`` for any (window_slug, ts_s) from on-disk
    parquet (BTC oracle + processed pm_events depth + token map).
  - ``SimRunner`` — loads a strategy via
    ``src.execution.strategy_loader.load_strategy``, iterates every
    second in every requested window, calls
    ``strategy.on_tick(snapshot, history, portfolio)``, and routes the
    emitted Signal through ``RealisticSimExecutionEngine`` (fill
    model from ``build_default_effects`` using the production effects
    config: ``adverse_selection=True``, others off until calibrated).
  - ``SimReport`` — aggregates per-trigger results into CSV + markdown.
- ``scripts/run_sim.py`` — thin CLI. Accepts ``--strategy`` (one or
  comma-separated list), ``--dates`` (range or list), ``--seeds``,
  ``--notional``. Writes reports under
  ``data/derived/reports/sim/``.

The simulator explicitly does **not** copy strategy logic. When a
strategy adds a filter, the filter is automatically picked up because
the simulator calls the real ``on_tick``. New strategies need zero
simulator code — just a config TOML.

## Scope and limits

- **Data coverage.** Simulator works on the date range where
  ``data/raw/pm_events/*/pm_depth_*.parquet`` exists. Today that's
  2026-04-14 through the current day minus the unflushed hour. The
  BTC oracle coverage is much wider and is the binding factor only
  during pre-pm-events dates.
- **Futures aux fields.** Strategies that read
  ``snapshot.btc_oi_change_pct``, ``btc_long_short_ratio``,
  ``btc_liq_*``, ``btc_taker_buy_ratio_15m``, etc. will see zeroed
  values because we don't (yet) backfill those from SpotFeed. P1 does
  not use those fields; strategies that do must pre-check. A future
  iteration can wire in a ``data/raw/btc_futures/`` parquet source.
- **Fee model.** ``fee_rate=0.0`` by default (matches existing sim
  scripts). Live production charges a redeemer + Venue fee; adjust
  via constructor when comparing absolute PnL against live.

## Alternatives considered

- **Extend ``src/research/paper_live_replay.py``.** It is focused on
  trade-log replay (given a live fill list, replay under different
  latency distributions). Not a fit for "generate triggers from
  scratch using the strategy class".
- **Fold sim into production runner.** Rejected: production runner
  tails ``data/live/realtime/latest.json`` and requires real-time
  ticks; adapting it to consume historical parquet would double its
  surface area.

## Consequences

- One-shot ``docs/analysis/p1_*_sim_v2.py`` scripts become deprecated
  the moment they stop being the canonical source of truth. They are
  not deleted yet because their hand-coded rule scans produce
  slightly different trigger counts than the real ``on_tick``, and
  a few analysis reports still reference those counts. Subsequent
  cleanup should migrate the reports to ``run_sim.py`` output and
  archive the scripts under ``docs/analysis/archive/``.
- Validation: the first full-coverage run (5 days, baseline + tight)
  matched the earlier hand-coded sim's per-trade PnL to within a few
  cents, but produced fewer triggers and a lower win rate — because
  the real ``on_tick`` has stricter dedup and filter behaviour than
  the analysis scripts faithfully replicated. Treat the new numbers
  as the trustworthy projection; treat the old scripts' numbers as
  historically-optimistic.
- Regression guard: ``tests/test_research/test_sim_runner.py``
  covers the pure helpers (window arithmetic, BTC as-of lookup, book
  lookup, token map merge) and the report aggregation.

## Follow-ups

1. Backfill SpotFeed futures fields so sim can faithfully drive
   filter-heavy strategies.
2. Deprecate and archive the per-strategy hand-coded sim scripts in
   ``docs/analysis/``.
3. Add a ``--include-pm-events-quarantine`` flag if we ever need to
   simulate on the repaired alternative snapshot source.
