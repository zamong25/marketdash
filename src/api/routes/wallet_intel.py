"""``/wallet-intel`` — read-only profitable-wallet research surface."""

@router.get('/summary')
def get_wallet_intel_summary() -> dict:
    """Return the latest wallet-intelligence snapshot for the dashboard."""
    ...

@router.get('/readiness-gap-summary')
def get_wallet_intel_readiness_gap_summary() -> dict:
    """Return compact wallet-copy and public-flow readiness blockers."""
    ...

@router.get('/wallet-pattern-readiness-scorecard')
def get_wallet_intel_wallet_pattern_readiness_scorecard() -> dict:
    """Return read-only wallet-pattern hypothesis readiness rankings."""
    ...

@router.get('/wallet-pattern-independent-replay-specs')
def get_wallet_intel_wallet_pattern_independent_replay_specs() -> dict:
    """Return read-only independent replay specs for wallet-pattern candidates."""
    ...

@router.get('/wallet-pattern-independent-replay-result')
def get_wallet_intel_wallet_pattern_independent_replay_result() -> dict:
    """Return read-only proxy replay results for wallet-pattern specs."""
    ...

@router.get('/focus')
def get_wallet_intel_focus() -> dict:
    """Return dashboard-ready focus rows for top wallet research targets."""
    ...

@router.get('/history')
def get_wallet_intel_history() -> dict:
    """Return append-only wallet observation history for database review."""
    ...

@router.get('/candidates')
def get_wallet_intel_candidates() -> dict:
    """Return wallet-derived strategy hypotheses for research triage."""
    ...

@router.get('/qualification')
def get_wallet_intel_qualification() -> dict:
    """Return wallet promotion blockers and copy-risk diagnostics."""
    ...

@router.get('/backfill-queue')
def get_wallet_intel_backfill_queue() -> dict:
    """Return wallet-level public-data backfill jobs."""
    ...

@router.get('/backfill-result')
def get_wallet_intel_backfill_result() -> dict:
    """Return the latest public-data wallet backfill run result."""
    ...

@router.get('/backfill-evidence')
def get_wallet_intel_backfill_evidence() -> dict:
    """Return re-scored wallet evidence from completed public backfills."""
    ...

@router.get('/backfill-reconciliation')
def get_wallet_intel_backfill_reconciliation() -> dict:
    """Return PnL reconciliation over completed wallet backfills."""
    ...

@router.get('/pnl-diagnostics')
def get_wallet_intel_pnl_diagnostics() -> dict:
    """Return public PnL anomaly diagnostics from wallet backfills."""
    ...

@router.get('/pnl-review-dossier')
def get_wallet_intel_pnl_review_dossier() -> dict:
    """Return durable manual PnL review dossier."""
    ...

@router.get('/pnl-review-dossier-history')
def get_wallet_intel_pnl_review_dossier_history() -> dict:
    """Return append-only PnL review dossier history."""
    ...

@router.get('/pnl-review-verdicts')
def get_wallet_intel_pnl_review_verdicts() -> dict:
    """Return PnL review verdicts derived from the current dossier."""
    ...

@router.get('/pnl-review-verdicts-history')
def get_wallet_intel_pnl_review_verdicts_history() -> dict:
    """Return append-only PnL review verdict history."""
    ...

@router.get('/pnl-scale-review')
def get_wallet_intel_pnl_scale_review() -> dict:
    """Return manual PnL-scale triage packets."""
    ...

@router.get('/pnl-scale-review-history')
def get_wallet_intel_pnl_scale_review_history() -> dict:
    """Return append-only manual PnL-scale triage history."""
    ...

@router.get('/pnl-source-review')
def get_wallet_intel_pnl_source_review() -> dict:
    """Return source-row review packets for manual wallet PnL checks."""
    ...

@router.get('/pnl-source-review-history')
def get_wallet_intel_pnl_source_review_history() -> dict:
    """Return append-only source-row review history."""
    ...

@router.get('/pnl-copyability-review')
def get_wallet_intel_pnl_copyability_review() -> dict:
    """Return bankroll copyability gates for source-cleared PnL wallets."""
    ...

@router.get('/pnl-copyability-review-history')
def get_wallet_intel_pnl_copyability_review_history() -> dict:
    """Return append-only bankroll copyability review history."""
    ...

@router.get('/deep-activity-queue')
def get_wallet_intel_deep_activity_queue() -> dict:
    """Return deeper public activity coverage jobs from PnL diagnostics."""
    ...

@router.get('/deep-activity-result')
def get_wallet_intel_deep_activity_result() -> dict:
    """Return latest deep public activity coverage run result."""
    ...

@router.get('/deep-activity-inventory')
def get_wallet_intel_deep_activity_inventory() -> dict:
    """Return cumulative deep public activity coverage from persisted summaries."""
    ...

@router.get('/data-requirements')
def get_wallet_intel_data_requirements() -> dict:
    """Return wallet data requirements that block promotion."""
    ...

@router.get('/wallet-replay-fixture-manifest')
def get_wallet_intel_wallet_replay_fixture_manifest() -> dict:
    """Return latest wallet replay fixture handoff manifest."""
    ...

@router.get('/wallet-replay-result')
def get_wallet_intel_wallet_replay_result() -> dict:
    """Return latest research-only wallet replay simulation result."""
    ...

@router.get('/wallet-replay-sweep-result')
def get_wallet_intel_wallet_replay_sweep_result() -> dict:
    """Return latest research-only wallet replay parameter sweep result."""
    ...

@router.get('/promotion-verdicts')
def get_wallet_intel_promotion_verdicts() -> dict:
    """Return wallet promotion verdicts from evidence, replay, and sweep gates."""
    ...

@router.get('/promotion-verdicts/history')
def get_wallet_intel_promotion_verdicts_history() -> dict:
    """Return persisted wallet promotion verdict run history."""
    ...

@router.get('/promotion-pipeline-result')
def get_wallet_intel_promotion_pipeline_result() -> dict:
    """Return latest read-only wallet promotion closure pipeline result."""
    ...

@router.get('/promotion-pipeline-history')
def get_wallet_intel_promotion_pipeline_history() -> dict:
    """Return append-only wallet promotion closure pipeline history."""
    ...

@router.get('/promotion-closure-review')
def get_wallet_intel_promotion_closure_review() -> dict:
    """Return joined wallet promotion closure blockers across evidence gates."""
    ...

@router.get('/pipeline-result')
def get_wallet_intel_pipeline_result() -> dict:
    """Return latest read-only wallet-intel pipeline run result."""
    ...

@router.get('/pipeline-history')
def get_wallet_intel_pipeline_history() -> dict:
    """Return append-only wallet-intel pipeline run history."""
    ...

@router.get('/observer-result')
def get_wallet_intel_observer_result() -> dict:
    """Return latest public wallet observation cycle result."""
    ...

@router.get('/observer-history')
def get_wallet_intel_observer_history() -> dict:
    """Return append-only public wallet observation cycle history."""
    ...

@router.get('/research-decisions')
def get_wallet_intel_research_decisions() -> dict:
    """Return append-only wallet research decision history."""
    ...

@router.get('/research-actions')
def get_wallet_intel_research_actions() -> dict:
    """Return prioritized open research actions from blocked decisions."""
    ...

@router.get('/research-backlog')
def get_wallet_intel_research_backlog() -> dict:
    """Return high-level next research work across wallet-intel subsystems."""
    ...

@router.get('/operations-plan')
def get_wallet_intel_operations_plan() -> dict:
    """Return advisory operations plan for the next safe research commands."""
    ...

@router.get('/operations-plan-history')
def get_wallet_intel_operations_plan_history() -> dict:
    """Return append-only operations-plan history."""
    ...

@router.get('/strategy-lead-review')
def get_wallet_intel_strategy_lead_review() -> dict:
    """Return current read-only strategy leads from research artifacts."""
    ...

@router.get('/cohorts')
def get_wallet_intel_cohorts() -> dict:
    """Return repeated wallet behavior cohorts for research triage."""
    ...

@router.get('/cohort-history')
def get_wallet_intel_cohort_history() -> dict:
    """Return append-only cohort observations for trend review."""
    ...

@router.get('/cohort-replay-queue')
def get_wallet_intel_cohort_replay_queue() -> dict:
    """Return cohort-derived replay jobs for research triage."""
    ...

@router.get('/cohort-replay-manifest')
def get_wallet_intel_cohort_replay_manifest() -> dict:
    """Return latest cohort replay handoff manifest."""
    ...

@router.get('/simulation-queue')
def get_wallet_intel_simulation_queue() -> dict:
    """Return wallet-derived replay jobs for simulation triage."""
    ...

@router.get('/strategy-evidence-queue')
def get_wallet_intel_strategy_evidence_queue() -> dict:
    """Return independent evidence collection jobs for blocked strategies."""
    ...

@router.get('/strategy-evidence-collection-result')
def get_wallet_intel_strategy_evidence_collection_result() -> dict:
    """Return latest independent strategy evidence collection result."""
    ...

@router.get('/strategy-evidence-scout-cycle-result')
def get_wallet_intel_strategy_evidence_scout_cycle_result() -> dict:
    """Return latest bounded strategy evidence scout-cycle result."""
    ...

@router.get('/strategy-evidence-scout-pipeline-result')
def get_wallet_intel_strategy_evidence_scout_pipeline_result() -> dict:
    """Return latest strategy evidence scout-to-review pipeline result."""
    ...

@router.get('/strategy-evidence-scout-pipeline-history')
def get_wallet_intel_strategy_evidence_scout_pipeline_history() -> dict:
    """Return append-only strategy evidence scout pipeline run history."""
    ...

@router.get('/strategy-evidence-scout-diagnostic-result')
def get_wallet_intel_strategy_evidence_scout_diagnostic_result() -> dict:
    """Return latest scout diagnostic and pivot recommendation."""
    ...

@router.get('/strategy-evidence-scout-diagnostic-history')
def get_wallet_intel_strategy_evidence_scout_diagnostic_history() -> dict:
    """Return append-only scout diagnostic run history."""
    ...

@router.get('/strategy-evidence-backfill-result')
def get_wallet_intel_strategy_evidence_backfill_result() -> dict:
    """Return latest public backfill result for strategy evidence wallets."""
    ...

@router.get('/strategy-evidence-review-result')
def get_wallet_intel_strategy_evidence_review_result() -> dict:
    """Return latest replay-readiness review for strategy evidence wallets."""
    ...

@router.get('/strategy-evidence-filter-sensitivity-result')
def get_wallet_intel_strategy_evidence_filter_sensitivity_result() -> dict:
    """Return latest filter sensitivity over strategy evidence candidates."""
    ...

@router.get('/strategy-evidence-filter-review-result')
def get_wallet_intel_strategy_evidence_filter_review_result() -> dict:
    """Return latest cross-check review for filter-sensitivity candidates."""
    ...

@router.get('/market-baseline-queue')
def get_wallet_intel_market_baseline_queue() -> dict:
    """Return non-copy market-level baseline jobs for simulation triage."""
    ...

@router.get('/market-baseline-replay-result')
def get_wallet_intel_market_baseline_replay_result() -> dict:
    """Return latest non-copy market baseline proxy replay result."""
    ...

@router.get('/market-baseline-depth-replay-result')
def get_wallet_intel_market_baseline_depth_replay_result() -> dict:
    """Return latest non-copy market baseline depth replay result."""
    ...

@router.get('/market-depth-coverage-result')
def get_wallet_intel_market_depth_coverage_result() -> dict:
    """Return depth-covered public-flow market baseline evidence."""
    ...

@router.get('/market-depth-coverage-replay-result')
def get_wallet_intel_market_depth_coverage_replay_result() -> dict:
    """Return latest depth replay over depth-covered public-flow baselines."""
    ...

@router.get('/market-depth-coverage-sensitivity-result')
def get_wallet_intel_market_depth_coverage_sensitivity_result() -> dict:
    """Return latest sensitivity over depth-covered public-flow replay."""
    ...

@router.get('/market-depth-research-diagnostic-result')
def get_wallet_intel_market_depth_research_diagnostic_result() -> dict:
    """Return latest market-depth research diagnostic."""
    ...

@router.get('/market-depth-research-diagnostic-history')
def get_wallet_intel_market_depth_research_diagnostic_history() -> dict:
    """Return append-only market-depth research diagnostic history."""
    ...

@router.get('/market-depth-price-filter-scout-result')
def get_wallet_intel_market_depth_price_filter_scout_result() -> dict:
    """Return latest market-depth price-filter scout."""
    ...

@router.get('/market-depth-price-filter-scout-history')
def get_wallet_intel_market_depth_price_filter_scout_history() -> dict:
    """Return append-only market-depth price-filter scout history."""
    ...

@router.get('/market-depth-sample-plan-result')
def get_wallet_intel_market_depth_sample_plan_result() -> dict:
    """Return latest market-depth sample expansion plan."""
    ...

@router.get('/market-depth-sample-plan-history')
def get_wallet_intel_market_depth_sample_plan_history() -> dict:
    """Return append-only market-depth sample expansion plan history."""
    ...

@router.get('/market-depth-orderbook-sample-cycle-result')
def get_wallet_intel_market_depth_orderbook_sample_cycle_result() -> dict:
    """Return latest targeted public orderbook sample cycle result."""
    ...

@router.get('/market-depth-orderbook-sample-cycle-history')
def get_wallet_intel_market_depth_orderbook_sample_cycle_history() -> dict:
    """Return append-only targeted public orderbook sample cycle history."""
    ...

@router.get('/market-depth-signal-capture-gap-result')
def get_wallet_intel_market_depth_signal_capture_gap_result() -> dict:
    """Return latest same-window public-flow capture gap diagnostic."""
    ...

@router.get('/market-depth-signal-capture-gap-history')
def get_wallet_intel_market_depth_signal_capture_gap_history() -> dict:
    """Return append-only same-window public-flow capture gap history."""
    ...

@router.get('/market-depth-sample-stalled-review-result')
def get_wallet_intel_market_depth_sample_stalled_review_result() -> dict:
    """Return latest stalled market-depth sample diagnostic."""
    ...

@router.get('/market-depth-sample-stalled-review-history')
def get_wallet_intel_market_depth_sample_stalled_review_history() -> dict:
    """Return append-only stalled market-depth sample diagnostic history."""
    ...

@router.get('/market-depth-research-pipeline-result')
def get_wallet_intel_market_depth_research_pipeline_result() -> dict:
    """Return latest market-depth research pipeline result."""
    ...

@router.get('/market-depth-research-pipeline-history')
def get_wallet_intel_market_depth_research_pipeline_history() -> dict:
    """Return append-only market-depth research pipeline history."""
    ...

@router.get('/replay-manifest')
def get_wallet_intel_replay_manifest() -> dict:
    """Return latest replay manifest generated from the simulation queue."""
    ...

@router.get('/wallet/{address}')
def get_wallet_intel_detail(address: str) -> dict:
    """Return latest row and score observations for one wallet."""
    ...

@router.get('/wallet/{address}/research-decisions')
def get_wallet_intel_wallet_research_timeline(address: str) -> dict:
    """Return append-only research decisions for one wallet."""
    ...
