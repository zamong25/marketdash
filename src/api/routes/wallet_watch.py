"""``/quick-trade/wallet-watch`` — live activity feed for watched wallets."""

@router.get('/activities')
def get_activities(limit: int=Query(100, ge=1, le=500), wallets: str=Query('', max_length=8192)) -> dict:
    """Recent BUY/SELL events on watched wallets (newest first)."""
    ...

@router.get('/status')
def get_status() -> dict:
    """Per-wallet polling summary (last seen ts, error count, etc.)."""
    ...

@router.get('/settlements')
def get_settlements(slugs: str=Query('', max_length=4096), condition_ids: str=Query('', max_length=8192)) -> dict:
    """Settlement labels for recent watched-market slugs."""
    ...
