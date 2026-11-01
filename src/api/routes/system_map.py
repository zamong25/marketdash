"""Read-only system-map and archive API."""

def _is_v2_cohort(wallets: list[Any] | None) -> bool:
    """Feature-detect scorecard-backed cohort rows without breaking v1 docs."""
    ...

def _ordered_funnel_entries(funnel: dict[str, Any]) -> list[dict[str, Any]]:
    """Expose builder insertion order explicitly while retaining ``funnel``."""
    ...

def _scandir_size(path: Path) -> tuple[int, int]:
    """Return apparent file bytes and unreadable-entry count without following links."""
    ...

def _dated_growth_bytes(root: Path, growth: dict[str, Any] | None, *, today: datetime) -> tuple[float | None, int]:
    """Average bytes written on the three complete UTC calendar days."""
    ...

def _measure_dataset_block(root: Path, registry: Sequence[dict[str, Any]], now: datetime) -> dict[str, Any]:
    ...

class _DatasetMeasurementCache:
    """Small process-local TTL cache; serializes stale scans across requests."""

    def __init__(self, *, ttl_s: float=DATASET_CACHE_TTL_S, clock: Callable[[], float]=time.monotonic, measure: Callable[[Path, Sequence[dict[str, Any]], datetime], dict[str, Any]]=_measure_dataset_block) -> None:
        ...

    def get(self, root: Path, registry: Sequence[dict[str, Any]], now: datetime) -> dict[str, Any]:
        ...

    def _fill(self, key: tuple[Any, ...], root: Path, registry: Sequence[dict[str, Any]], now: datetime) -> dict[str, Any]:
        ...

def _dataset_measurement_block(root: Path, registry: Sequence[dict[str, Any]], now: datetime) -> dict[str, Any]:
    ...

def _absolute_plan_path(root: Path, value: Any) -> Path | None:
    ...

def _path_contains(parent: Path, child: Path) -> bool:
    ...

def _next_dataset_deletion(root: Path, paths: Sequence[str], streams: Sequence[Any]) -> dict[str, Any] | None:
    ...

def _warehouse_dataset_block(root: Path, registry: Sequence[dict[str, Any]], now: datetime) -> dict[str, Any]:
    ...

def _now() -> datetime:
    ...

def _iso(value: datetime | None=None) -> str:
    ...

def _finite_float(value: Any) -> float | None:
    ...

def _nonnegative_int(value: Any) -> int | None:
    ...

def _parse_time(value: Any) -> datetime | None:
    ...

def _read_json(path: Path) -> tuple[Any | None, bool]:
    ...

def _read_object(path: Path) -> tuple[dict[str, Any], bool]:
    ...

def _source_age_s(payload: dict[str, Any], path: Path, *, now: datetime | None=None) -> float | None:
    ...

def station_state(*, source_present: bool, age_s: float | None, warn_after_s: float, halt_after_s: float, locked: bool=False) -> Literal['ok', 'warn', 'halt']:
    """Map source freshness and a station lock to the frozen state vocabulary."""
    ...

def _caption(value: Any, known: bool, known_caption: str, missing_caption: str) -> str:
    ...

def _money_text(value: float | None, *, signed: bool=False) -> str:
    ...

def _compact_money_text(value: float | None) -> str:
    """Money copy for narrow rule cards: omit only a redundant .00."""
    ...

def _number_text(value: int | None, suffix: str='건') -> str:
    ...

def _daily_book_rows(snapshot: dict[str, Any]) -> list[dict[str, Any]]:
    ...

def _book_period(daily: list[dict[str, Any]]) -> tuple[str | None, str | None]:
    ...

def _redemption_rows(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    ...

def _read_live_book_cached(path: Path) -> tuple[dict[str, Any], bool]:
    """live_book.json은 수십 MB — 파일 버전당 1회만 파싱 (감사 P2)."""
    ...

def _validation_rows() -> tuple[list[dict[str, Any]], bool]:
    """Parse validation pairs once per file version — the file is tens of MB"""
    ...

def _validation_metrics(rows: list[dict[str, Any]] | None=None, *, source_ok: bool | None=None) -> tuple[dict[str, Any] | None, bool]:
    ...

def _today_fill_split(rows: list[dict[str, Any]], now_ts: float) -> tuple[int, int, int]:
    """Today's real fills split into (filled, settled, open) per validation ledger."""
    ...

def _same_utc_day(value: Any, now: datetime) -> bool:
    ...

def _latest_detections(now: datetime) -> tuple[list[dict[str, Any]], bool]:
    ...

def _radar_detail(now: datetime) -> dict[str, Any]:
    ...

def _filter_skip_copy(reason: str) -> dict[str, str]:
    ...

def _champion_guard_breakdown(now: datetime) -> list[dict[str, Any]]:
    """Today's real champion guard reasons from the opportunities log."""
    ...

def _filter_skip_rows(validation_rows: list[dict[str, Any]], now: datetime) -> list[dict[str, Any]]:
    ...

def _guard_counter_effectiveness(now: datetime) -> dict[str, dict[str, Any]]:
    ...

def _shadow_books(*, now_ts: float) -> tuple[list[dict[str, Any]], bool, float | None]:
    ...

def _champion_wallet_stats() -> tuple[dict[str, dict[str, Any]], bool]:
    ...

def _real_settled_wallet_counts() -> tuple[dict[str, int], bool]:
    ...

def _roi_proxy(wallet: dict[str, Any]) -> float | None:
    """Return only the cohort builder's real return proxy."""
    ...

def _cohort_list_rows() -> tuple[str | None, list[dict[str, Any]]]:
    ...

def _sort_cohort_rows(rows: list[dict[str, Any]], sort: str, direction: str) -> list[dict[str, Any]]:
    ...

def _normalize_wallet_buy(row: dict[str, Any], address: str) -> dict[str, Any] | None:
    ...

def _read_wallet_trade_file(path: Path, address: str) -> tuple[list[dict[str, Any]], bool]:
    ...

def _recent_wallet_buys(address: str, limit: int) -> tuple[list[dict[str, Any]], Literal['ok', 'empty', 'unavailable'], str | None]:
    ...

def _game_history_rows() -> list[dict[str, Any]]:
    ...

def _game_history_revision(source: str) -> str:
    """Stable read revision used to detect append activity between pages."""
    ...

def _book_snapshot(key: str) -> tuple[dict[str, Any], bool, float | None]:
    ...

def _book_era_split(snapshot: dict[str, Any], *, now_ts: float) -> dict[str, dict[str, Any]]:
    ...

def _judge_book_basis(gate: dict[str, Any], delay: dict[str, Any], era_split: dict[str, dict[str, Any]]) -> dict[str, Any]:
    """Describe Amendment 5's delay-reflected judge evidence honestly."""
    ...

def _heartbeat_path(name: str) -> Path:
    ...

def _hard_halt_reason(live_heartbeat: dict[str, Any], armed: bool | None) -> str | None:
    ...

def _heartbeat_history_paths() -> tuple[Path, ...]:
    ...

def _read_history_objects(path: Path) -> list[dict[str, Any]]:
    ...

def _balance_candidate(row: dict[str, Any]) -> tuple[float | None, datetime | None]:
    ...

def _last_known_balance(live_heartbeat: dict[str, Any], live_book: dict[str, Any]) -> tuple[float | None, datetime | None, str | None, bool]:
    ...

def _open_position_rows(live_book: dict[str, Any]) -> list[dict[str, Any]]:
    """Normalize the executor's current open book for display-only consumers."""
    ...

def _live_bet_principal(raw: dict[str, Any]) -> float | None:
    """Return signed principal, falling back to the best legacy stake value."""
    ...

def _asset_day_bet_rows(live_book: dict[str, Any]) -> list[dict[str, Any]]:
    """Normalize already-loaded executor rows for client-side KST day filtering."""
    ...

def _gate_counts(gate: dict[str, Any], gate_ok: bool) -> tuple[int | None, int | None, str]:
    ...

def _system_map_payload() -> dict[str, Any]:
    ...

def next_run_at(schedule: dict[str, Any], *, now: datetime, last_run: datetime | None=None) -> datetime | None:
    """Return the next scheduled instant without inventing a missing interval anchor."""
    ...

def derive_batch_status(*, group: Literal['always', 'scheduled'], launchd_known: bool, launchd_loaded: bool, pid_present: bool, freshness_known: bool, fresh: bool) -> Literal['running', 'stopped', 'disabled', 'unknown']:
    """Combine read-only liveness signals into the operator vocabulary."""
    ...

def _launchctl_snapshot() -> tuple[dict[str, dict[str, Any]], bool]:
    """Read launchd only; failures stay unknown and never trigger recovery."""
    ...

def _batch_source_path(source: tuple[str, str, str]) -> Path:
    ...

def _source_timestamp(path: Path, kind: str) -> datetime | None:
    ...

def _batch_last_seen(spec: dict[str, Any]) -> datetime | None:
    ...

def _unknown_loaded_rows(launchd_rows: dict[str, dict[str, Any]], known_labels: set[str]) -> list[dict[str, Any]]:
    ...

def _unknown_launchd_group(label: str, process: dict[str, Any]) -> Literal['always', 'scheduled']:
    """Classify an unregistered label from its local plist without changing it."""
    ...

def _gate_situation(cond: dict[str, Any], ops: Any) -> str:
    """Turn raw numbers into a plain-language 'current situation' sentence."""
    ...

def _gate_checks(conditions: Any, ops: Any=None) -> list[dict[str, Any]] | None:
    """Reshape gate conditions ({key,label,detail,ok}) into the drawer's"""
    ...

def _discovery() -> dict[str, Any] | None:
    """스카우트 깔때기 — weekly reverse-scan / cluster-scan funnel counts."""
    ...

def _discovery_history(scans_dir: Path) -> list[dict[str, Any]]:
    """Last 16 scan-day trend points (fed by weekly_scan._append_scan_history)."""
    ...

def _machines(*, now: datetime) -> list[dict[str, Any]]:
    ...

def _archive_feed_path() -> Path:
    ...

def _archive_rows() -> list[dict[str, Any]]:
    ...

def _invalid_doc_ref() -> HTTPException:
    ...

def _safe_post_path(doc_ref: str) -> tuple[Path, str | None]:
    ...

def _first_heading(markdown: str, fallback: str) -> str:
    ...

def _constitution_section(markdown: str, anchor: str) -> str:
    ...

def _post_metadata(doc_ref: str, path: Path) -> tuple[str, str]:
    ...

class _SystemMapCache:

    def __init__(self) -> None:
        ...

    def get(self) -> dict[str, Any]:
        ...

    def _maybe_refresh_async(self) -> None:
        ...

    def _fill(self) -> dict[str, Any]:
        ...

@router.get('/system-map')
def get_system_map() -> dict[str, Any]:
    """Compose the frozen system-map contract from existing read-side files."""
    ...

def morning_briefing_payload(root: Path=REPO_ROOT) -> dict[str, Any]:
    """Read the composer's latest publication without triggering a refresh."""
    ...

@router.get('/morning-briefing')
def get_morning_briefing() -> dict[str, Any]:
    """Return only the already-published local morning briefing."""
    ...

@router.get('/cohort-list')
def get_cohort_list(page: int=Query(default=1, ge=1), page_size: int=Query(default=LIST_PAGE_SIZE, ge=1, le=500), sort: Literal['wallet', 'copy_count', 'copy_win_rate', 'copy_pnl_usd', 'dominant_category', 'roi_proxy']='roi_proxy', direction: Literal['asc', 'desc']='desc') -> dict[str, Any]:
    """List selected wallets with read-only, per-wallet follow results."""
    ...

@router.get('/wallet-trades')
def get_wallet_trades(address: str=Query(..., min_length=1), limit: int=Query(default=WALLET_TRADES_CAP, ge=1)) -> dict[str, Any]:
    """Return a bounded, read-only slice of one wallet's recent BUY tape."""
    ...

@router.get('/game-history')
def get_game_history(page: int=Query(default=1, ge=1), page_size: int=Query(default=LIST_PAGE_SIZE, ge=1, le=1000), source: Literal['all', 'validation', 'champion']=Query(default='all')) -> dict[str, Any]:
    """Return settled bets newest first. ``source`` filters to real"""
    ...

@router.get('/archive')
def get_archive(tab: Literal['all', 'research', 'rules', 'incidents', 'works']='all', page: int=Query(default=1, ge=1)) -> dict[str, Any]:
    ...

@router.get('/archive/post')
def get_archive_post(doc_ref: str=Query(..., min_length=1)) -> dict[str, Any]:
    ...
