"""``/strategies`` — canonical strategy roster + active config bindings."""

def _load_active_roster() -> dict[str, list[dict]]:
    ...

@router.get('/scorecard')
def get_strategy_scorecard() -> dict:
    """Return provenance-aware strategy scorecards from local logs."""
    ...

@router.get('/insights')
def get_strategy_insights() -> dict:
    """Return reusable lessons from local strategy scorecards."""
    ...

@router.get('/hypothesis-lab')
def get_strategy_hypothesis_lab() -> dict:
    """Return research-only strategy hypotheses synthesized from local evidence."""
    ...

@router.get('/external-source-hypothesis-seeds')
def get_strategy_external_source_hypothesis_seeds() -> dict:
    """Return locked external-source strategy hypothesis seeds."""
    ...

@router.get('/external-source-control-readiness')
def get_strategy_external_source_control_readiness() -> dict:
    """Return read-only external-source control readiness checks."""
    ...

@router.get('/external-source-control-candidate-search')
def get_strategy_external_source_control_candidate_search() -> dict:
    """Return public-search candidates for external-source controls."""
    ...

@router.get('/external-source-control-capture-queue')
def get_strategy_external_source_control_capture_queue() -> dict:
    """Return read-only capture queue for external-source controls."""
    ...

@router.get('/external-source-control-evidence-review')
def get_strategy_external_source_control_evidence_review() -> dict:
    """Return review gates for external-source control evidence."""
    ...

@router.get('/hypothesis-validation-specs')
def get_strategy_hypothesis_validation_specs() -> dict:
    """Return JSON spec handoffs for hypothesis validation jobs."""
    ...

@router.get('/hypothesis-artifact-collection')
def get_strategy_hypothesis_artifact_collection() -> dict:
    """Return artifact collection jobs for hypothesis validation specs."""
    ...

@router.get('/hypothesis-artifact-evidence-cycle')
def get_strategy_hypothesis_artifact_evidence_cycle() -> dict:
    """Return saved-evidence attachments for hypothesis validation artifacts."""
    ...

@router.get('/hypothesis-artifact-review')
def get_strategy_hypothesis_artifact_review() -> dict:
    """Return review gates for collected hypothesis validation artifacts."""
    ...

@router.get('/hypothesis-artifact-review-decision-template')
def get_strategy_hypothesis_artifact_review_decision_template() -> dict:
    """Return a non-confirmed manual review decision template."""
    ...

@router.get('/hypothesis-replay-inputs')
def get_strategy_hypothesis_replay_inputs() -> dict:
    """Return replay input handoffs for reviewed hypothesis artifacts."""
    ...

@router.get('/hypothesis-replay-runner-preview')
def get_strategy_hypothesis_replay_runner_preview() -> dict:
    """Return locked replay runner preview rows without running replay."""
    ...

@router.get('/hypothesis-replay-result-record-candidates')
def get_strategy_hypothesis_replay_result_record_candidates() -> dict:
    """Return candidate replay result-log records without appending them."""
    ...

@router.get('/hypothesis-research-scorecard')
def get_strategy_hypothesis_research_scorecard() -> dict:
    """Return research-only ranking for hypothesis replay candidates."""
    ...

@router.get('/hypothesis-profit-edge-plan')
def get_strategy_hypothesis_profit_edge_plan() -> dict:
    """Return locked profit-edge validation tasks for blocked hypotheses."""
    ...

@router.get('/hypothesis-resolved-market-backfill')
def get_strategy_hypothesis_resolved_market_backfill() -> dict:
    """Return resolved-market outcome backfill for profit-edge candidates."""
    ...

@router.get('/hypothesis-entry-price-diagnostics')
def get_strategy_hypothesis_entry_price_diagnostics() -> dict:
    """Return research-only entry-price diagnostics for resolved PnL samples."""
    ...

@router.get('/hypothesis-signal-entry-snapshot-plan')
def get_strategy_hypothesis_signal_entry_snapshot_plan() -> dict:
    """Return read-only collection tasks for diagnostic-positive entry rules."""
    ...

@router.get('/hypothesis-signal-entry-market-candidates')
def get_strategy_hypothesis_signal_entry_market_candidates() -> dict:
    """Return current market candidates for diagnostic-positive entry rules."""
    ...

@router.get('/hypothesis-signal-entry-semantic-review')
def get_strategy_hypothesis_signal_entry_semantic_review() -> dict:
    """Return outcome-semantics review gates for signal-entry candidates."""
    ...

@router.get('/hypothesis-signal-entry-semantic-map')
def get_strategy_hypothesis_signal_entry_semantic_map() -> dict:
    """Return locked proposition-map queues for signal-entry candidates."""
    ...

@router.get('/hypothesis-signal-entry-semantic-map-decision-template')
def get_strategy_hypothesis_signal_entry_semantic_map_decision_template() -> dict:
    """Return a non-confirmed operator template for semantic-map decisions."""
    ...

@router.get('/hypothesis-signal-entry-semantic-map-decision-draft')
def get_strategy_hypothesis_signal_entry_semantic_map_decision_draft() -> dict:
    """Return a locked recommended semantic-map decision draft."""
    ...

@router.get('/hypothesis-signal-entry-snapshot-join')
def get_strategy_hypothesis_signal_entry_snapshot_join() -> dict:
    """Return research-only signal-entry snapshot cost joins."""
    ...

@router.get('/hypothesis-signal-entry-research-pnl')
def get_strategy_hypothesis_signal_entry_research_pnl() -> dict:
    """Return research-only current-cost EV rows for signal-entry snapshots."""
    ...

@router.get('/hypothesis-signal-entry-settlement-sample-plan')
def get_strategy_hypothesis_signal_entry_settlement_sample_plan() -> dict:
    """Return read-only settlement-sample follow-ups for positive EV rows."""
    ...

@router.get('/hypothesis-signal-entry-execution-sensitivity')
def get_strategy_hypothesis_signal_entry_execution_sensitivity() -> dict:
    """Return read-only execution-friction sensitivity for signal-entry EV rows."""
    ...

@router.get('/hypothesis-signal-entry-promotion-gate')
def get_strategy_hypothesis_signal_entry_promotion_gate() -> dict:
    """Return strict research-to-simulation gates for signal-entry leads."""
    ...

@router.get('/hypothesis-signal-entry-promotion-action-queue')
def get_strategy_hypothesis_signal_entry_promotion_action_queue() -> dict:
    """Return read-only next actions for blocked signal-entry promotion gates."""
    ...

@router.get('/hypothesis-signal-entry-reprice-watch')
def get_strategy_hypothesis_signal_entry_reprice_watch() -> dict:
    """Return read-only price watch for reject/reprice signal-entry actions."""
    ...

@router.get('/hypothesis-signal-entry-evidence-collection-plan')
def get_strategy_hypothesis_signal_entry_evidence_collection_plan() -> dict:
    """Return post-reprice read-only evidence collection priorities."""
    ...

@router.get('/hypothesis-signal-entry-fill-quality-review')
def get_strategy_hypothesis_signal_entry_fill_quality_review() -> dict:
    """Return read-only fill-quality review for signal-entry evidence rows."""
    ...

@router.get('/hypothesis-signal-entry-stress-reprice-review')
def get_strategy_hypothesis_signal_entry_stress_reprice_review() -> dict:
    """Return read-only stress reprice targets for fill-quality rows."""
    ...

@router.get('/hypothesis-signal-entry-actual-settlement-watch')
def get_strategy_hypothesis_signal_entry_actual_settlement_watch() -> dict:
    """Return read-only settlement watches for actual signal-entry samples."""
    ...

@router.get('/hypothesis-signal-entry-direction-conflict-decision-template')
def get_strategy_hypothesis_signal_entry_direction_conflict_decision_template() -> dict:
    """Return a non-confirmed operator template for direction-conflict decisions."""
    ...

@router.get('/hypothesis-signal-entry-resolution-source-review')
def get_strategy_hypothesis_signal_entry_resolution_source_review() -> dict:
    """Return resolution-source review queue for actual-settlement rows."""
    ...

@router.get('/hypothesis-signal-entry-resolution-source-decision-template')
def get_strategy_hypothesis_signal_entry_resolution_source_decision_template() -> dict:
    """Return a non-confirmed operator template for source decisions."""
    ...

@router.get('/hypothesis-signal-entry-operator-board')
def get_strategy_hypothesis_signal_entry_operator_board() -> dict:
    """Return read-only operator board for signal-entry promotion work."""
    ...

@router.get('/hypothesis-operator-review-queue')
def get_strategy_hypothesis_operator_review_queue() -> dict:
    """Return locked manual review queue for top hypothesis candidates."""
    ...

@router.get('/experiment-portfolio-board')
def get_strategy_experiment_portfolio_board() -> dict:
    """Return read-only cross-market strategy experiment lanes."""
    ...

@router.get('/experiment-rework-queue')
def get_strategy_experiment_rework_queue() -> dict:
    """Return read-only kill/rework/data-repair queue for strategy experiments."""
    ...

@router.get('/scenario-frontier')
def get_strategy_scenario_frontier() -> dict:
    """Return cross-market scenario candidates joined from current evidence."""
    ...

@router.get('/scenario-proof-queue')
def get_strategy_scenario_proof_queue() -> dict:
    """Return proof tasks derived from the cross-market scenario frontier."""
    ...

@router.get('/scenario-coverage-matrix')
def get_strategy_scenario_coverage_matrix() -> dict:
    """Return all-market scenario-template coverage against current proof work."""
    ...

@router.get('/scenario-template-rotation-plan')
def get_strategy_scenario_template_rotation_plan() -> dict:
    """Return the saved template-balanced next proof rotation plan."""
    ...

@router.get('/scenario-template-rotation-execution-ledger')
def get_strategy_scenario_template_rotation_execution_ledger() -> dict:
    """Return saved evidence observed for the template rotation plan."""
    ...

@router.get('/scenario-template-rotation-evidence-review')
def get_strategy_scenario_template_rotation_evidence_review() -> dict:
    """Return non-confirming review queue for template rotation evidence."""
    ...

@router.get('/scenario-template-rotation-action-batch')
def get_strategy_scenario_template_rotation_action_batch() -> dict:
    """Return non-executing action batch for template rotation review items."""
    ...

@router.get('/scenario-template-rotation-artifact-acceptance-review')
def get_strategy_scenario_template_rotation_artifact_acceptance_review() -> dict:
    """Return local artifact acceptance review for template rotation evidence."""
    ...

@router.get('/scenario-template-rotation-learning-ledger')
def get_strategy_scenario_template_rotation_learning_ledger() -> dict:
    """Return learning records from template rotation artifact reviews."""
    ...

@router.get('/scenario-template-rotation-learning-refresh-plan')
def get_strategy_scenario_template_rotation_learning_refresh_plan() -> dict:
    """Return learning-aware refresh plan for template rotation."""
    ...

@router.get('/scenario-template-rotation-public-read-batch-selection')
def get_strategy_scenario_template_rotation_public_read_batch_selection() -> dict:
    """Return locked public-read batch selection for template rotation."""
    ...

@router.get('/scenario-template-rotation-public-read-evidence-gap-review')
def get_strategy_scenario_template_rotation_public_read_evidence_gap_review() -> dict:
    """Return local evidence-gap review for selected public-read batch."""
    ...

@router.get('/scenario-template-rotation-public-read-decision-review')
def get_strategy_scenario_template_rotation_public_read_decision_review() -> dict:
    """Return locked decision review for selected public-read candidates."""
    ...

@router.get('/scenario-template-rotation-public-read-hypothesis-seeds')
def get_strategy_scenario_template_rotation_public_read_hypothesis_seeds() -> dict:
    """Return locked hypothesis seeds for selected public-read decisions."""
    ...

@router.get('/scenario-proof-cycle-plan')
def get_strategy_scenario_proof_cycle_plan() -> dict:
    """Return the saved diversity-capped next cycle for scenario proof tasks."""
    ...

@router.get('/scenario-proof-cycle-runbook')
def get_strategy_scenario_proof_cycle_runbook() -> dict:
    """Return the saved non-executing runbook for the selected proof cycle."""
    ...

@router.get('/scenario-proof-cycle-execution-ledger')
def get_strategy_scenario_proof_cycle_execution_ledger() -> dict:
    """Return saved evidence observed for the selected proof-cycle runbook."""
    ...

@router.get('/market-timing-depth-replay')
def get_market_timing_depth_replay_result() -> dict:
    """Return read-only market-timing replay diagnostics."""
    ...

@router.get('/market-timing-depth-sample-plan')
def get_market_timing_depth_sample_plan() -> dict:
    """Return targeted collection tasks for failed market-timing replay rows."""
    ...

@router.get('/hypothesis-replay-results')
def get_strategy_hypothesis_replay_results() -> dict:
    """Return review gates for recorded hypothesis replay results."""
    ...

@router.get('/drilldown')
def get_strategy_drilldown() -> dict:
    """Return per-strategy joined research evidence and gates."""
    ...

@router.get('/promotion-readiness')
def get_strategy_promotion_readiness() -> dict:
    """Return strict per-strategy promotion readiness blockers."""
    ...

@router.get('/simulation-handoff')
def get_strategy_simulation_handoff() -> dict:
    """Return runnable local sim-vs-live handoff jobs for blocked strategies."""
    ...

@router.get('/config-drafts')
def get_strategy_config_drafts() -> dict:
    """Return read-only strategy config drafts from validated research evidence."""
    ...

@router.get('/config-materialization')
def get_strategy_config_materialization_handoff() -> dict:
    """Return read-only checks before config drafts can reach sim handoff."""
    ...

@router.get('/draft-simulation-handoff')
def get_strategy_draft_simulation_handoff() -> dict:
    """Return run_sim handoff commands for reviewed draft configs."""
    ...

@router.get('/simulation-scorecards')
def get_strategy_simulation_scorecards() -> dict:
    """Return local sim-vs-live scorecards for dashboard triage."""
    ...

@router.get('/paper-validation-audits')
def get_strategy_paper_validation_audits() -> dict:
    """Return local paper validation tick-decision audit summaries."""
    ...

@router.get('')
def list_strategies() -> dict:
    """All canonical strategies registered + their active config bindings."""
    ...
