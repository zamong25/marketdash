"""``/markets`` — public-data market research and local focus surfaces."""

@router.get('/scanner')
def get_market_scanner() -> dict:
    """Return scanner rows from local latest snapshot files."""
    ...

@router.get('/search')
def search_markets(q: str=Query('', min_length=0, max_length=96), limit: int=Query(12, ge=1, le=30)) -> dict:
    """Search Venue markets through public MarketMeta data only."""
    ...

@router.get('/universe-coverage')
def get_market_universe_coverage() -> dict:
    """Return local artifact coverage across broad Venue market families."""
    ...

@router.get('/universe-expansion-plan')
def get_market_universe_expansion_plan() -> dict:
    """Return read-only search and evidence jobs for uncovered market families."""
    ...

@router.get('/universe-search-cycle')
def get_market_universe_search_cycle() -> dict:
    """Return the latest saved broad-market public search cycle."""
    ...

@router.get('/external-signal-gap-queue')
def get_market_external_signal_gap_queue() -> dict:
    """Return saved external source gaps for selected proof-cycle tasks."""
    ...

@router.get('/external-signal-source-scan')
def get_market_external_signal_source_scan() -> dict:
    """Return saved MarketMeta detail source scan for external source gaps."""
    ...

@router.get('/wti-timestamped-source-capture')
def get_market_wti_timestamped_source_capture() -> dict:
    """Return saved WTI/Pyth source capture joined to public market data."""
    ...

@router.get('/wti-source-depth-flow-join')
def get_market_wti_source_depth_flow_join() -> dict:
    """Return saved WTI source-depth-flow observation join rows."""
    ...

@router.get('/resolved-outcome-samples')
def get_market_resolved_outcome_samples() -> dict:
    """Return the latest saved resolved outcome sample set."""
    ...

@router.get('/resolved-sample-replay-readiness')
def get_market_resolved_sample_replay_readiness() -> dict:
    """Return saved joins between resolved samples and replay evidence."""
    ...

@router.get('/resolved-public-trade-backfill')
def get_market_resolved_public_trade_backfill() -> dict:
    """Return saved public trade backfill for resolved sample condition IDs."""
    ...

@router.get('/resolved-public-depth-feasibility')
def get_market_resolved_public_depth_feasibility() -> dict:
    """Return saved public current-book feasibility for resolved trade samples."""
    ...

@router.get('/resolved-archived-depth-window-scan')
def get_market_resolved_archived_depth_window_scan() -> dict:
    """Return saved local pm_depth overlap scan for resolved trade windows."""
    ...

@router.get('/resolved-forward-capture-plan')
def get_market_resolved_forward_capture_plan() -> dict:
    """Return saved active-market depth capture jobs for future resolved samples."""
    ...

@router.get('/resolved-forward-flow-capture')
def get_market_resolved_forward_flow_capture() -> dict:
    """Return saved public flow capture paired to forward depth snapshots."""
    ...

@router.get('/resolved-forward-profit-probe-queue')
def get_market_resolved_forward_profit_probe_queue() -> dict:
    """Return future resolved-market profit-probe seeds and blockers."""
    ...

@router.get('/resolved-forward-depth-flow-dataset')
def get_market_resolved_forward_depth_flow_dataset() -> dict:
    """Return local forward snapshot-history rows joined to public flow."""
    ...

@router.get('/resolved-forward-profit-probe-results')
def get_market_resolved_forward_profit_probe_results() -> dict:
    """Return settlement-PnL probes for forward depth+flow rows."""
    ...

@router.get('/resolved-forward-resolution-watch-queue')
def get_market_resolved_forward_resolution_watch_queue() -> dict:
    """Return market-level watch queue for unresolved forward profit probes."""
    ...

@router.get('/resolved-forward-entry-repair-review')
def get_market_resolved_forward_entry_repair_review() -> dict:
    """Return review rows for missing selected-entry profit probes."""
    ...

@router.get('/resolved-forward-entry-repair-recovery-scan')
def get_market_resolved_forward_entry_repair_recovery_scan() -> dict:
    """Return local archived-depth recovery evidence for entry-repair rows."""
    ...

@router.get('/resolved-forward-strategy-insights')
def get_market_resolved_forward_strategy_insights() -> dict:
    """Return research hypotheses from forward depth+flow evidence."""
    ...

@router.get('/orderbook-preview')
def get_market_orderbook_preview(token_ids: str=Query('', max_length=4096), selected_token_id: str=Query('', max_length=512), side: str=Query('BUY', pattern='^(BUY|SELL|buy|sell)$'), shares: float=Query(0.0, ge=0.0, le=100000.0), limit_price: float | None=Query(None, ge=0.0, le=1.0), market_tradeable: bool | None=Query(None), existing_position_exposure_usd: float=Query(0.0, ge=0.0, le=1000000.0), existing_position_shares: float=Query(0.0, ge=0.0, le=1000000.0)) -> dict:
    """Return a read-only public CLOB book walk preview for one market."""
    ...

@router.get('/quotes')
def get_market_quotes() -> dict:
    """Return local top-of-book quote summaries from pm_events snapshots."""
    ...

@router.get('/watchlist')
def get_market_watchlist() -> dict:
    """Return local market watchlist rows for research triage."""
    ...

@router.get('/opportunity-review')
def get_market_opportunity_review() -> dict:
    """Return research-ranked market opportunities with live blockers."""
    ...

@router.get('/pins')
def get_market_pins() -> dict:
    """Return saved and suggested market pins for dashboard focus."""
    ...

@router.post('/pins')
def post_market_pin(payload: dict) -> dict:
    """Persist a research-only market pin without placing orders."""
    ...

@router.get('/orderbook-plan')
def get_market_orderbook_plan() -> dict:
    """Return read-only public-data orderbook snapshot work."""
    ...

@router.get('/orderbook-snapshots')
def get_market_orderbook_snapshots() -> dict:
    """Return collected public orderbook snapshot records."""
    ...

@router.get('/price-quality-review')
def get_market_price_quality_review() -> dict:
    """Return read-only market price-quality review rows."""
    ...

@router.get('/depth-replay-plan')
def get_market_depth_replay_plan() -> dict:
    """Return read-only depth replay plan for price-quality passes."""
    ...

@router.get('/pin-replay-specs')
def get_market_pin_replay_specs() -> dict:
    """Return read-only replay specs derived from saved market pins."""
    ...

@router.get('/pin-rules-resolution-adapters')
def get_market_pin_rules_resolution_adapters() -> dict:
    """Return market-rules and resolution adapter drafts for saved pins."""
    ...

@router.get('/pin-resolution-evidence')
def get_market_pin_resolution_evidence() -> dict:
    """Return resolution-evidence readiness for saved market pins."""
    ...

@router.get('/pin-depth-replay-result')
def get_market_pin_depth_replay_result() -> dict:
    """Return depth-replay readiness for saved-market replay specs."""
    ...

@router.get('/pin-replay-runner-handoff')
def get_market_pin_replay_runner_handoff() -> dict:
    """Return read-only replay-runner handoff contracts for saved pins."""
    ...

@router.get('/pin-full-market-depth-replay-result')
def get_market_pin_full_market_depth_replay_result() -> dict:
    """Return full-market depth replay diagnostics for saved pins."""
    ...

@router.get('/pin-strategy-signal-handoff')
def get_market_pin_strategy_signal_handoff() -> dict:
    """Return signal timestamp research handoffs for full-market replay diagnostics."""
    ...

@router.get('/pin-strategy-signal-evidence')
def get_market_pin_strategy_signal_evidence() -> dict:
    """Return validated pre-resolution signal evidence for market-pin handoffs."""
    ...

@router.get('/pin-strategy-control-comparison')
def get_market_pin_strategy_control_comparison() -> dict:
    """Return same-category control checks for market-pin strategy signals."""
    ...

@router.get('/current-recapture-control-evidence-coverage')
def get_current_market_recapture_control_evidence_coverage() -> dict:
    """Return saved evidence coverage for current recapture controls."""
    ...

@router.get('/current-recapture-control-comparison')
def get_current_market_recapture_control_comparison() -> dict:
    """Return saved target-vs-control comparisons for current recapture rows."""
    ...

@router.get('/current-recapture-candidate-action-queue')
def get_current_market_recapture_candidate_action_queue() -> dict:
    """Return read-only next actions for current recapture candidates."""
    ...

@router.get('/research-rotation-board')
def get_market_research_rotation_board() -> dict:
    """Return read-only cross-market rotation actions from saved evidence."""
    ...

@router.get('/research-queue')
def get_market_research_queue() -> dict:
    """Return read-only market research jobs derived from opportunity review."""
    ...
