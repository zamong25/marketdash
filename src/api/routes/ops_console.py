"""Operations console API."""

class ConfirmBody(BaseModel):
    confirm: str | None

class PromoteBody(ConfirmBody):
    variant: str

class SettingsPatchBody(ConfirmBody):
    updates: dict[str, Any]

def _now() -> datetime:
    ...

def _iso(dt: datetime | None=None) -> str:
    ...

def _read_json(path: Path, default: Any) -> Any:
    ...

def _relative_or_str(path: Path) -> str:
    ...

def _safe_doc_id(raw: str, *, allowed: set[str] | None=None) -> str:
    ...

def _parse_time(value: Any) -> datetime | None:
    ...

def _age_s(value: Any, *, now: datetime | None=None) -> float | None:
    ...

def _live_config_path() -> Path:
    ...

def _shadow_config_path() -> Path:
    ...

def _live_book_path() -> Path:
    ...

def _gate_latest_path() -> Path:
    ...

def _replay_dir() -> Path:
    ...

def _replay_latest_path() -> Path:
    ...

def _replay_pid_path() -> Path:
    ...

def _replay_log_path() -> Path:
    ...

def _arm_audit_path() -> Path:
    ...

def _validation_pairs_path() -> Path:
    ...

def _validation_ladder_path() -> Path:
    ...

def _validation_gap_report_path() -> Path:
    ...

def _delay_gap_report_path() -> Path:
    ...

def _validation_stop_path() -> Path:
    ...

def _latest_review_or_log_path() -> Path:
    ...

def _file_mtime_age(path: Path, *, now: datetime | None=None) -> float | None:
    ...

def _heartbeat(path: Path | None, *, max_age_s: float, mtime_only: bool=False) -> dict[str, Any]:
    ...

def _run_launchctl_list() -> str:
    ...

def _parse_launchctl_list(text: str) -> dict[str, dict[str, Any]]:
    ...

def _launchctl_rows() -> dict[str, dict[str, Any]]:
    ...

def _daemon_status(hb: dict[str, Any], launchd: dict[str, Any], daemon_id: str) -> str:
    ...

def _daemons() -> list[dict[str, Any]]:
    ...

def _gate_process_report(*, timeout_s: float=120.0) -> dict[str, Any]:
    ...

def _gate_report(*, force_refresh: bool=False) -> dict[str, Any]:
    ...

def _gate_age_for_arm(report: dict[str, Any]) -> float | None:
    ...

def _referee() -> dict[str, Any]:
    ...

def _variant_eval_by_key() -> dict[str, dict[str, Any]]:
    ...

def _league() -> dict[str, Any]:
    ...

def _sanitize_error(exc: Exception) -> str:
    ...

def _balance_status(*, force_refresh: bool=False) -> dict[str, Any]:
    ...

def _load_live_config() -> dict[str, Any]:
    ...

def _write_live_config(config: dict[str, Any]) -> None:
    ...

def _live_book_stats() -> dict[str, Any]:
    ...

def _read_jsonl_rows(path: Path) -> list[dict[str, Any]]:
    ...

def _merged_validation_attempts(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Return attempted pair rows with append-only reconciliations applied."""
    ...

def _position_settlement_index() -> dict[str, dict[str, Any]]:
    """Index exact detection IDs from the champion and real-money books."""
    ...

def _validation_cost(real: dict[str, Any]) -> float | None:
    ...

def _short_order_id(value: Any) -> str | None:
    ...

def _detection_to_submit_s(row: dict[str, Any], opportunity: dict[str, Any], real: dict[str, Any]) -> float | None:
    ...

def _attempt_payload(row: dict[str, Any], *, pending: bool, settlements: dict[str, dict[str, Any]]) -> dict[str, Any]:
    ...

def _pending_attempt_payload(pending: dict[str, Any], settlements: dict[str, dict[str, Any]]) -> dict[str, Any]:
    ...

def _validation_lock_skips(rows: list[dict[str, Any]], *, today: str) -> list[dict[str, Any]]:
    ...

def _fill_history_payload() -> dict[str, Any]:
    ...

def _utc_day(value: Any) -> str | None:
    ...

def _finite_float(value: Any) -> float | None:
    ...

def _nonnegative_int(value: Any) -> int:
    ...

def _validation_gap() -> dict[str, Any]:
    ...

def _validation_stats(heartbeat: dict[str, Any]) -> dict[str, Any]:
    ...

def _lock_rows(config: dict[str, Any], heartbeat: dict[str, Any], gate: dict[str, Any]) -> list[dict[str, Any]]:
    ...

def _money(referee: dict[str, Any]) -> dict[str, Any]:
    ...

def _next_weekday_at(now: datetime, *, weekday: int, hour: int, minute: int) -> datetime:
    ...

def _schedule() -> dict[str, Any]:
    ...

def _lessons() -> list[dict[str, str]]:
    ...

def _append_audit(action: str, *, gate: dict[str, Any] | None=None, balance: dict[str, Any] | None=None, details: dict[str, Any] | None=None) -> None:
    ...

def _require_confirm(body: ConfirmBody, expected: str) -> None:
    ...

def _arm_rejection(report: dict[str, Any], *, config: dict[str, Any], heartbeat: dict[str, Any]) -> HTTPException | None:
    ...

def _review_dir() -> Path:
    ...

def _analysis_dir() -> Path:
    ...

def _review_path(review_id: str) -> Path:
    ...

def _analysis_review_path(analysis_id: str) -> Path:
    ...

def _review_title(text: str, fallback: str) -> str:
    ...

def _review_summary(path: Path, *, id_override: str | None=None, title_prefix: str='') -> dict[str, Any]:
    ...

def _analysis_review_summary(path: Path) -> dict[str, Any]:
    ...

def _doc_path(doc_id: str) -> Path:
    ...

def _evaluation_row(variant: str) -> dict[str, Any] | None:
    ...

def _load_shadow_config_raw() -> dict[str, Any]:
    ...

def _write_shadow_config(config: dict[str, Any]) -> None:
    ...

def _settings_fields(config: dict[str, Any], spec: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    ...

def _settings_payload() -> dict[str, Any]:
    ...

def _validate_settings_updates(updates: dict[str, Any], spec: dict[str, dict[str, Any]]) -> dict[str, Any]:
    ...

def _pid_is_running(pid: int) -> bool:
    ...

def _replay_pid_doc() -> dict[str, Any] | None:
    ...

def _replay_status() -> dict[str, Any]:
    ...

def _decay() -> dict[str, Any]:
    ...

@router.get('/overview')
def get_overview() -> dict[str, Any]:
    """Mission-control aggregate, read-only."""
    ...

@router.get('/fill-history')
def get_fill_history() -> dict[str, Any]:
    """Truthful real-money validation attempts, read-only."""
    ...

@router.get('/reviews')
def list_reviews() -> dict[str, Any]:
    """Weekly review and analysis list, newest first."""
    ...

@router.get('/reviews/{review_id}')
def get_review(review_id: str) -> dict[str, Any]:
    """Read one weekly review markdown body."""
    ...

@router.get('/docs/{doc_id}')
def get_ops_doc(doc_id: str) -> dict[str, Any]:
    """Read-only operator docs shown inside mission control."""
    ...

@router.post('/league/promote')
def promote_variant(body: PromoteBody=Body(...)) -> dict[str, Any]:
    ...

@router.post('/league/hold')
def hold_variant(body: PromoteBody=Body(...)) -> dict[str, Any]:
    ...

@router.post('/referee/run')
def run_referee_now() -> dict[str, Any]:
    ...

@router.post('/replay/run')
def run_replay_now() -> dict[str, Any]:
    ...

@router.get('/replay/status')
def replay_status() -> dict[str, Any]:
    ...

@router.get('/settings')
def get_settings() -> dict[str, Any]:
    ...

@router.patch('/settings/config')
def patch_shadow_settings(body: SettingsPatchBody=Body(...)) -> dict[str, Any]:
    ...

@router.patch('/settings/live')
def patch_live_settings(body: SettingsPatchBody=Body(...)) -> dict[str, Any]:
    ...

@router.post('/live/arm')
def arm_live(body: ConfirmBody=Body(...)) -> dict[str, Any]:
    ...

@router.post('/live/disarm')
def disarm_live() -> dict[str, Any]:
    ...

@router.post('/validation/enable')
def enable_validation(body: ConfirmBody=Body(...)) -> dict[str, Any]:
    ...

@router.post('/validation/disable')
def disable_validation() -> dict[str, Any]:
    ...

@router.post('/kill-switch')
def enable_kill_switch(body: ConfirmBody=Body(...)) -> dict[str, Any]:
    ...

@router.delete('/kill-switch')
def disable_kill_switch(body: ConfirmBody=Body(...)) -> dict[str, Any]:
    ...
