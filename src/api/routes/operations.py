"""``/operations`` — operational log and intent audit surfaces."""

@router.get('/execution-log')
def get_operations_execution_log() -> dict:
    """Return recent local execution/order-decision log rows."""
    ...

@router.get('/execution-quality')
def get_operations_execution_quality() -> dict:
    """Return local route, fill, latency, and rejection quality summaries."""
    ...

@router.get('/manual-trade-intents')
def get_manual_trade_intents() -> dict:
    """Return saved manual trade intents from the dashboard workbench."""
    ...

@router.get('/manual-trade-execution-readiness')
def get_manual_trade_execution_readiness() -> dict:
    """Return locked pre-order readiness for saved manual trade intents."""
    ...

@router.get('/manual-trade-paper-observation-handoff')
def get_manual_trade_paper_observation_handoff() -> dict:
    """Return paper-observation handoff jobs for saved manual trade intents."""
    ...

@router.get('/manual-trade-paper-observations')
def get_manual_trade_paper_observations() -> dict:
    """Return saved paper observation outcomes for manual trade intents."""
    ...

@router.get('/manual-trade-paper-observation-insights')
def get_manual_trade_paper_observation_insights() -> dict:
    """Return read-only insights derived from manual paper observations."""
    ...

@router.post('/manual-trade-paper-observations')
def post_manual_trade_paper_observation(payload: dict[str, Any]) -> dict:
    """Save a paper observation outcome without placing an order."""
    ...

@router.post('/manual-trade-intents')
def post_manual_trade_intent(payload: dict[str, Any]) -> dict:
    """Save a dashboard trade-ticket intent without placing an order."""
    ...
