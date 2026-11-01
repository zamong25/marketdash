"""``/copy-radar`` — read-only surface for the copy-radar cohort + shadow ledger."""

def _detection_day_kst(raw_timestamp: Any) -> date | None:
    """Return the KST calendar date for one detection timestamp."""
    ...

def _detection_counts_from_log(path: Path, *, start_offset: int=0) -> tuple[Counter[str], int]:
    """Count detections per KST day from ``start_offset`` onward."""
    ...

def _saved_scan_offset(document: Any) -> int:
    """Byte offset after the last complete line the rollup already counted."""
    ...

def _saved_detection_counts(path: Path) -> dict[str, int]:
    ...

def _refresh_detections_daily(now: datetime | None=None) -> dict[str, Any]:
    """Merge the current JSONL into the durable rollup and return 14 KST days."""
    ...

def _detections_daily_payload() -> dict[str, Any]:
    ...

def _read_json(path: Path, default: Any) -> Any:
    """Read a JSON file, returning ``default`` on any error (never raises)."""
    ...

def _tail_opportunities(limit: int) -> list[dict[str, Any]]:
    """Return the newest ``limit`` opportunities, newest first."""
    ...

@router.get('/opportunities')
def get_opportunities(limit: int=Query(50, ge=1, le=500), era_filter: str=Query('all', alias='era', pattern='^(current|prior|all)$')) -> dict[str, Any]:
    """Newest shadow-copy opportunities (newest first)."""
    ...

@router.get('/detections/daily')
def get_detections_daily() -> dict[str, Any]:
    """Last 14 KST calendar days of detections, backed by a durable rollup."""
    ...

@router.get('/opportunities/history')
def get_opportunities_history(limit: int=Query(50, ge=1, le=200), offset: int=Query(0, ge=0), guard: str | None=Query(None, pattern='^(none|event_cap|per_wallet_cap|daily_loss_stop|wallet_suspended|any)$'), wallet: str | None=Query(None), cat: str | None=Query(None), since: float | None=Query(None), until: float | None=Query(None)) -> dict[str, Any]:
    """Paginated opportunities log (newest first), including guard-excluded ones."""
    ...

def _resolve_variant(variant: str | None) -> str:
    """Map ``?variant=`` to a book key. Absent → the configured ``champion_variant``"""
    ...

@router.get('/guru-dossiers')
def get_guru_dossiers() -> dict[str, Any]:
    """Guru dossier corpus for the dossier screen (read-only file serving)."""
    ...

@router.get('/guru-profiles')
def get_guru_profiles() -> dict[str, Any]:
    """전수 기계 도씨에 — one auto profile per roster/cluster wallet."""
    ...

@router.get('/premium-canary')
def get_premium_canary() -> dict[str, Any]:
    """지연 웃돈 카나리아 — 연못별 웃돈 최근72h vs 이전, 오르는 연못 깃발."""
    ...

@router.get('/guru-clusters')
def get_guru_clusters() -> dict[str, Any]:
    """Same-owner wallet-cluster registry for the cluster console screen."""
    ...

@router.get('/variants')
def get_variants() -> dict[str, Any]:
    """The evolution-lab roster with each book's headline stats."""
    ...

@router.get('/ledger')
def get_ledger(variant: str | None=Query(None, pattern=VARIANT_PATTERN), era_filter: str=Query('all', alias='era', pattern='^(current|prior|all)$')) -> dict[str, Any]:
    """Shadow-ledger rollup for a variant book (default = configured champion)."""
    ...

def _position_row(raw: dict[str, Any], *, settled: bool) -> dict[str, Any]:
    """Map a stored ledger position to the frozen ``/positions`` row shape."""
    ...

def _position_sort_key(row: dict[str, Any]) -> float:
    """Newest activity first — settled by settlement time, open by open time."""
    ...

def _filter_rows_by_era(rows: list[dict[str, Any]], era_filter: str, era_start: float) -> list[dict[str, Any]]:
    """Keep ledger rows in their detection/opening era (never settlement era)."""
    ...

def _entry_price_of(row: dict[str, Any]) -> float | None:
    """Buy-side price for breakeven math — ``entry_price`` with ``their_price``"""
    ...

def _ledger_rollup(open_rows: list[dict[str, Any]], settled_rows: list[dict[str, Any]], *, voided_n: int=0) -> dict[str, Any]:
    """Recompute the display summary from one era's ``ts_open`` membership."""
    ...

def _position_identity(position: dict[str, Any]) -> str:
    """Mirror the durable ledger correction key without loading a live book."""
    ...

def _active_open_rows(state: dict[str, Any]) -> tuple[list[dict[str, Any]], int]:
    """Exclude both durable correction markers and WP-90 quarantine rows."""
    ...

def _book_bet_row(raw: dict[str, Any], *, settled: bool) -> dict[str, Any]:
    """Map either shadow-book format to WP-113's per-bet wire shape."""
    ...

def _bet_cat(row: dict[str, Any]) -> str:
    ...

def _opened_at(row: dict[str, Any]) -> float:
    ...

def _row_timestamp(row: dict[str, Any], key: str) -> float:
    ...

@router.get('/book/{variant}/bets')
def get_book_bets(variant: str=PathParam(pattern=BOOK_BET_VARIANT_PATTERN), status: str=Query('all', pattern='^(open|settled|all)$'), era_filter: str=Query('current', alias='era', pattern='^(current|prior|all)$'), offset: int=Query(0, ge=0), limit: int=Query(20, ge=1, le=200), market_cat: str | None=Query(None), wallet: str | None=Query(None)) -> dict[str, Any]:
    """Browse one simulated book bet-by-bet, newest opening first."""
    ...

def _state_rows(state: dict[str, Any]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    ...

@router.get('/virtual-real')
def get_virtual_real(era_filter: str=Query('current', alias='era', pattern='^(current|prior|all)$'), offset: int=Query(0, ge=0), limit: int=Query(20, ge=1, le=200)) -> dict[str, Any]:
    """Era-scoped champion -> delayed -> real ladder and validation pairs."""
    ...

@router.get('/positions')
def get_positions(limit: int=Query(200, ge=1, le=1000), offset: int=Query(0, ge=0), status: str=Query('all', pattern='^(open|settled|all)$'), market_cat: str | None=Query(None), wallet: str | None=Query(None), event_key: str | None=Query(None), variant: str | None=Query(None, pattern=VARIANT_PATTERN), era_filter: str=Query('all', alias='era', pattern='^(current|prior|all)$'), since: float | None=Query(None), until: float | None=Query(None)) -> dict[str, Any]:
    """Per-position shadow rows (open + settled), newest activity first."""
    ...

@router.get('/autopsy')
def get_autopsy(era_filter: str=Query('all', alias='era', pattern='^(current|prior|all)$')) -> dict[str, Any]:
    """Re-scoring rollups + guard counterfactual (60s in-process cache)."""
    ...

def _champion_settled() -> list[dict[str, Any]]:
    """The champion book's settled positions (WP-9 our-results are champion-only)."""
    ...

def _cohort_churn() -> dict[str, Any]:
    """This-week new/left counts vs the prior cohort snapshot (best-effort)."""
    ...

def _real_copy_result(metrics: dict[str, Any], *, split: dict[str, dict[str, Any]] | None=None) -> dict[str, Any]:
    """The small, explicitly REAL subset exposed to the roster."""
    ...

def _real_copy_results(now_ts: float) -> tuple[dict[str, dict[str, Any]], dict[str, Any]]:
    """Read-only validation-ledger totals, overall and attributed by guru."""
    ...

@router.get('/cohort')
def get_cohort() -> dict[str, Any]:
    """The current selected cohort — gate stats PLUS the WP-9 quality loop."""
    ...

def _surgery_summary(status_doc: dict[str, Any]) -> dict[str, Any] | None:
    """안건 A-2 명단 대수술 요약 — 화면 배너용 (수술 정지가 없으면 None)."""
    ...

def _iso_age(ts: Any) -> float | None:
    """Seconds since an ISO-8601 timestamp, or ``None`` if unparsable."""
    ...

def _heartbeat_age(payload: dict[str, Any]) -> float | None:
    """Seconds since a heartbeat's ``ts`` (ISO 8601), or ``None`` if unparsable."""
    ...

@router.get('/pond-map')
def get_pond_map() -> dict[str, Any]:
    """The per-category pond map + freshness (weekly batch artifact)."""
    ...

@router.get('/health')
def get_health() -> dict[str, Any]:
    """Heartbeat freshness + loaded sizing config."""
    ...

def _roster_sources() -> list[tuple[str, Path]]:
    """(generation id, file) pairs — the id doubles as the detail allowlist."""
    ...

def _roster_swaps() -> list[dict[str, Any]]:
    """Swap-log rows (oldest first) with only screen-safe fields."""
    ...

@router.get('/roster-generations')
def get_roster_generations() -> dict[str, Any]:
    """Every archived roster generation plus the current one, newest first."""
    ...

@router.get('/roster-generations/{generation_id}')
def get_roster_generation(generation_id: str) -> dict[str, Any]:
    """One generation's roster with per-wallet report-card numbers."""
    ...

@router.get('/roster-blacklist')
def get_roster_blacklist() -> dict[str, Any]:
    """Suspended wallets with their bench reason and post-bench scoring."""
    ...
