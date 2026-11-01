"""``/quick-trade`` — dynamic event-scoped CLOB trading dashboard endpoints."""

def _repo_relative(path: Path) -> str:
    ...

def _latest_file_health(path: Path, *, stale_after_s: float, now_ts: float | None=None) -> dict:
    ...

def _iso_epoch(value: object) -> float | None:
    ...

def _live_validation_heartbeat_health(path: Path, *, stale_after_s: float, now_ts: float | None=None) -> dict:
    ...

def _live_validation_freshness(*, latest_path: Path, heartbeat_path: Path, stale_after_s: float, now_ts: float | None=None) -> dict:
    ...

def _live_validation_payload(raw: object, file_health: dict) -> dict:
    ...

def _window_capture_loop() -> None:
    """Watch the live Oracle stream; pin each 5-min window's opening price to the"""
    ...

def _current_updown_market_meta(window_slug: str | None) -> dict:
    ...

def _current_updown_clob_depth(market_meta: dict) -> dict:
    """Read public CLOB books for both BTC 5m tokens and return best-level depth."""
    ...

def _best_depth_payload(book: dict | None, token_id: str) -> dict:
    ...

def _apply_updown_clob_depth(pm: dict, clob_depth: dict) -> dict:
    """Fill missing/zero PM best-level sizes from public CLOB depth when aligned."""
    ...

def _positive_float(value: object) -> float | None:
    ...

def _price_close(left: object, right: object, *, tolerance: float=0.02) -> bool:
    ...

def _market_meta_market_lookup_requests(slug: str) -> list[tuple[str, str, dict[str, str]]]:
    ...

def _market_meta_get_json(path: str, params: dict[str, str]) -> object:
    ...

def _market_meta_lookup_failure_reason(failures: list[str]) -> str:
    ...

def _local_updown_market_meta(slug: str) -> dict[str, object]:
    """Recover current BTC 5m token ids from the local live orderbook capture."""
    ...

def _read_live_latest_snapshot() -> dict:
    ...

def _book_reference_price(book: dict[str, object]) -> float | None:
    ...

def _as_float_local(value: object) -> float | None:
    ...

def _updown_question_from_slug(slug: str) -> str:
    ...

def _btc_5m_slug_from_ts(value: object) -> str:
    ...

def _oracle_watchdog_loop() -> None:
    """Restart the oracle collector if latest.json goes stale (>60s) — a backstop"""
    ...

def _ensure_window_capture() -> None:
    ...

def _oracle_window_start(epoch_sec: int) -> float | None:
    """Oracle BTC/USD price at the window start epoch — the settlement basis"""
    ...

@router.get('/discover')
def discover_quick_trade(category: str=Query('all', min_length=1, max_length=64), feed_filter: str=Query('all', min_length=1, max_length=32), feed_mode: str=Query('live', min_length=1, max_length=32), q: str=Query('', min_length=0, max_length=512), limit: int=Query(36, ge=8, le=60), offset: int=Query(0, ge=0, le=5000)) -> dict:
    """Return a light category feed for Venue-style discovery."""
    ...

@router.get('/resolve')
def resolve_quick_trade(q: str=Query('', min_length=0, max_length=512), limit: int=Query(80, ge=8, le=160)) -> dict:
    """Resolve a query/URL into one focused event tree and normalized markets."""
    ...

def _cache_account_preflight(key: tuple[str, ...], future: concurrent.futures.Future[dict]) -> None:
    ...

def _quick_trade_account_future(tokens: list[str]) -> concurrent.futures.Future[dict]:
    ...

def _bounded_quick_trade_account(tokens: list[str]) -> dict:
    ...

@router.get('/account')
def get_quick_trade_account(token_ids: str=Query('', max_length=6000)) -> dict:
    """Read balance/allowance/open-order preflight for the selected market."""
    ...

@router.get('/user-activity')
def get_quick_trade_user_activity(market_ids: str=Query('', max_length=6000), event_id: str=Query('', max_length=64), limit: int=Query(80, ge=1, le=500), offset: int=Query(0, ge=0, le=10000)) -> dict:
    """Read Data API positions/activity for the configured proxy wallet."""
    ...

@router.get('/wallet-analytics')
async def get_quick_trade_wallet_analytics(wallet: str=Query('', max_length=64), window: str=Query('30d', min_length=2, max_length=4), funding: bool=Query(True)) -> dict:
    """Read wallet analytics — local-first, cached per (wallet, window, funding)."""
    ...

def _scorecard_wallet_is_quarantined(wallet: str) -> bool:
    """Read WP-120's derived quarantine artifact on the display path."""
    ...

@router.get('/wallet-favorites')
def list_wallet_favorites() -> dict:
    ...

@router.post('/wallet-favorites', status_code=201)
def create_wallet_favorite(address: str=Query(..., min_length=40, max_length=64), alias: str=Query('', max_length=40)) -> dict:
    ...

@router.patch('/wallet-favorites/{favorite_id}')
def update_wallet_favorite(favorite_id: str, alias: str=Query('', max_length=40)) -> dict:
    ...

@router.post('/wallet-favorites/{favorite_id}/touch')
def touch_wallet_favorite(favorite_id: str) -> dict:
    ...

@router.delete('/wallet-favorites/{favorite_id}', status_code=204)
def delete_wallet_favorite(favorite_id: str) -> None:
    ...

@router.get('/price-history')
def get_quick_trade_price_history(token_id: str=Query('', min_length=1, max_length=90), interval: str=Query('1d', min_length=1, max_length=8), fidelity: int=Query(5, ge=1, le=60)) -> dict:
    """Read public CLOB price history for a selected outcome token."""
    ...

@router.get('/price-history-batch')
def get_quick_trade_price_history_batch(token_ids: str=Query('', max_length=900), interval: str=Query('1d', min_length=1, max_length=8), fidelity: int=Query(5, ge=1, le=60)) -> dict:
    """Read public CLOB price histories for selected outcome tokens."""
    ...

@router.get('/live-mode')
def get_quick_trade_live_mode() -> dict:
    """Read the runtime live-orders gate (follows env until toggled; resets on restart)."""
    ...

@router.post('/live-mode')
def set_quick_trade_live_mode(payload: dict) -> dict:
    """Flip the runtime live-orders gate. Body: {"enabled": bool}. Resets to env on restart."""
    ...

@router.post('/orders')
def post_quick_trade_order(payload: dict) -> dict:
    """Validate and dry-run by default; live submit requires explicit gate + payload confirm."""
    ...

@router.get('/orders/audit')
def get_quick_trade_order_audit(limit: int=Query(12, ge=1, le=50)) -> dict:
    """Recent dashboard order attempts, independent of the currently selected market."""
    ...

@router.get('/redeemable')
def get_quick_trade_redeemable() -> dict:
    """List winning positions Venue flags as ready to redeem (read-only)."""
    ...

@router.post('/redeem')
def post_quick_trade_redeem(payload: dict) -> dict:
    """Gasless redeem of every redeemable position. Dry-run by default;"""
    ...

@router.get('/live-price')
def get_quick_trade_live_price(symbol: str=Query('BTC', min_length=1, max_length=12)) -> dict:
    """Latest spot price from the realtime collector snapshot. 1s freshness."""
    ...

@router.get('/updown-analytics')
def get_quick_trade_updown_analytics() -> dict:
    """BTC up/down decision panel: Oracle (settlement, WS ~1s) vs SpotFeed (market)"""
    ...

@router.get('/updown-entry-exit')
def get_quick_trade_updown_entry_exit() -> dict:
    """Per-second entry/exit research: which entry times / prices / conditions were"""
    ...

@router.get('/updown-late-rebound')
def get_quick_trade_updown_late_rebound() -> dict:
    """Last-60s cheap-side rebound grid statistics and read-only automation gate."""
    ...

class _LateReboundExecuteRequest(BaseModel):
    mode: str
    stake_usd: float

@router.post('/updown-late-rebound/execute')
def post_quick_trade_updown_late_rebound_execute(req: _LateReboundExecuteRequest) -> dict:
    """Manual last-minute rebound button."""
    ...

@router.get('/updown-live-decision-validation')
def get_quick_trade_updown_live_decision_validation() -> dict:
    """Read-only validation summaries for the BTC live decision panel."""
    ...

@router.get('/oracle-series')
def get_quick_trade_oracle_series(symbol: str=Query('btc/usd', min_length=3, max_length=16), minutes: int=Query(5, ge=1, le=60)) -> dict:
    """Downsampled Oracle price series (settlement feed) for the up/down chart."""
    ...

@router.get('/btc-bars')
def get_quick_trade_btc_bars(interval: str=Query('1m', min_length=1, max_length=5), limit: int=Query(30, ge=5, le=120)) -> dict:
    """Recent BTC futures klines from SpotFeed. Cached 30s. Used by the"""
    ...
