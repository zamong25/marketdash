"""Double-locked live PURE MIRROR of a copy-radar paper book."""

def data_dir() -> Path:
    ...

def runs_dir() -> Path:
    ...

def live_config_path() -> Path:
    ...

def live_book_path() -> Path:
    ...

def source_ledger_path(source_book: str) -> Path:
    """Append-only ledger of the paper book this executor mirrors (read-only)."""
    ...

def mirror_tail_state_path() -> Path:
    """Executor-owned tail offset file. Never lives in the paper book's dir."""
    ...

def heartbeat_path() -> Path:
    ...

def kill_switch_path() -> Path:
    ...

def validation_stop_path() -> Path:
    ...

def validation_pairs_path() -> Path:
    ...

def validation_ladder_path() -> Path:
    ...

def decision_log_path() -> Path:
    ...

def _utc_date(ts: float) -> str:
    ...

def _to_float(value: Any, default: float=0.0) -> float:
    ...

def _to_int(value: Any, default: int=0) -> int:
    ...

def _to_decimal(value: Any, default: str) -> Decimal:
    ...

def _round_or_none(value: Any, ndigits: int=6) -> float | None:
    ...

def _iso(ts: float | None=None) -> str:
    ...

def _normalize_tick_size(value: Any) -> Decimal:
    ...

def compliant_limit_buy_amounts(stake_usd: Any, limit_price: Any, tick: Any) -> tuple[Decimal, Decimal]:
    """Return maximal SDK-stable BUY shares and an exact cent maker amount."""
    ...

def compliant_limit_sell_shares(position_shares: Any, tick: Any) -> Decimal:
    """Return the largest SDK-stable SELL size not exceeding our held shares."""
    ...

def _floor_to_tick(value: Decimal, tick: Decimal) -> Decimal:
    ...

def _snap_tick_dust(value: Decimal, tick: Decimal) -> Decimal:
    ...

def _aligned_buy_limit(raw_limit: Decimal, tick_size: Decimal) -> Decimal:
    ...

def _json_safe(value: Any) -> Any:
    ...

def _order_status(payload: Any) -> str:
    ...

def _fill_cost_breakdown(*, balance_delta: float, shares_delta: float, submit_response: Any, market_category: str | None=None) -> dict[str, Any]:
    """Split balance-delta all-in cost into CLOB principal and residual fee."""
    ...

def bootstrap_live_config(path: Path | None=None) -> None:
    """Create ``live_config.json`` with ``armed:false`` if it does not exist."""
    ...

class LiveConfigLoader:
    """Hot-reload ``live_config.json`` by mtime; never arms programmatically."""

    def __init__(self, path: Path | None=None) -> None:
        ...

    def load(self) -> dict[str, Any]:
        ...

@dataclass(frozen=True)
class GateVerdict:
    go: bool
    verdict: str
    exit_code: int | None
    source: str
    detail: str
    generated_at: str

    def to_dict(self) -> dict[str, Any]:
        ...

def gate_from_report(report: dict[str, Any], *, source: str, process_rc: int | None=None) -> GateVerdict:
    ...

def run_gate_decision(config: dict[str, Any] | None=None, now_ts: float | None=None) -> GateVerdict:
    """Run or read the latest gate verdict. GO requires process exit 0 and verdict GO."""
    ...

@dataclass(frozen=True)
class LockState:
    armed: bool
    gate_go: bool
    kill_switch_absent: bool
    daily_loss_ok: bool
    daily_spend_today_usd: float
    daily_spend_cap_usd: float
    daily_loss_stop_usd: float
    gate: GateVerdict
    validation_mode: bool
    validation_stop_absent: bool
    validation_loss_ok: bool
    validation_open_float_ok: bool
    validation_realized_settled_pnl_usd: float
    validation_open_float_usd: float
    validation_open_float_cap_usd: float
    validation_cumulative_delta_usd: float
    validation_loss_stop_usd: float
    ladder_value: float
    today_credits: float
    daily_budget: float
    today_spend: float
    ladder_last_clean_day: str | None
    ladder_bankroll_usd_at_roll: float | None
    pending_order_clear: bool
    pending_order_count: int

    @property
    def clean(self) -> bool:
        ...

    @property
    def can_reconcile_pending(self) -> bool:
        """Read-only reconciliation may run while money caps block new orders."""
        ...

    @property
    def can_redeem(self) -> bool:
        """Settlement recovery is blocked only by the total-halt kill switch."""
        ...

    @property
    def reasons(self) -> list[str]:
        ...

    def to_dict(self) -> dict[str, Any]:
        ...

class LiveBook:
    """File-backed live mirror book. Keeps the shadow schema plus live deltas."""

    def __init__(self, path: Path | None=None) -> None:
        ...

    def _load(self) -> dict[str, Any]:
        ...

    def _archive_path(self) -> Path:
        ...

    def _compact_skips(self) -> None:
        """Move skip records beyond the window to the archive, keeping their ids."""
        ...

    def persist(self) -> None:
        """Rewrite the book only when its content actually changed."""
        ...

    def _payload(self) -> dict[str, Any]:
        ...

    def seen_ids(self) -> set[str]:
        ...

    def realized_delta_today(self, now_ts: float) -> float:
        ...

    def record_balance(self, balance_usdc: float, now_ts: float) -> dict[str, Any]:
        ...

    def last_balance(self) -> float | None:
        ...

    def record_skip(self, opportunity: dict[str, Any], *, reason: str, now_ts: float, intended_order: dict[str, Any] | None=None, locks: LockState | None=None, mode: str='dry_run') -> dict[str, Any]:
        ...

    def record_pending(self, pending: dict[str, Any]) -> dict[str, Any]:
        ...

    def clear_pending(self, order_id: str) -> None:
        ...

    def record_open(self, opportunity: dict[str, Any], *, now_ts: float, order_id: str, stake_usd: float, shares: float, cost_usd: float, balance_delta_usd: float, entry_price: float, limit_price: float, best_ask_price: float, principal_usd: float | None=None, fee_usd: float=0.0, fee_source: str='principal_unavailable_separately; fee_included_in_balance_delta', validation_mode: bool=False) -> dict[str, Any]:
        ...

    def record_redemption_batch(self, *, now_ts: float, balance_before: float, balance_after: float, results: list[dict[str, Any]]) -> dict[str, Any]:
        ...

    def close_position_by_sale(self, detection_id: str, sale_fields: dict[str, Any]) -> dict[str, Any] | None:
        """Move one open position to settled with mirror mid-sale fields."""
        ...

    def settle_validation_positions(self, settlement_rows: list[dict[str, Any]], *, now_ts: float) -> None:
        """Move forward-era validation positions out of the live open book."""
        ...

def intended_order(opportunity: dict[str, Any], config: dict[str, Any], *, tick_size: Any=DEFAULT_TICK_SIZE, tick_source: str='fallback_no_lookup') -> dict[str, Any]:
    ...

def effective_order_config(config: dict[str, Any]) -> dict[str, Any]:
    """Config used for order construction."""
    ...

def intended_sell_order(position: dict[str, Any], paper_sell_price: Any, config: dict[str, Any], *, tick_size: Any=DEFAULT_TICK_SIZE, tick_source: str='fallback_no_lookup') -> dict[str, Any]:
    """Tick-compliant marketable limit SELL mirroring a paper mid-sale."""
    ...

def mirror_open_opportunity(row: dict[str, Any], source_book: str) -> dict[str, Any]:
    """Shape a paper ``{source_book}_open`` row like the order-path opportunity."""
    ...

def mirror_exit_opportunity(row: dict[str, Any], source_book: str) -> dict[str, Any]:
    """Shape a paper ``{source_book}_exit_sell`` row for the sell order path."""
    ...

def _coerce_epoch_seconds(value: Any) -> float | None:
    ...

def _extract_result_fill_ts(result: Any, default_ts: float) -> tuple[float, str]:
    ...

def best_ask_price(book: Any) -> float | None:
    """Return the lowest ask price from port, SDK-raw, or test-dict book shapes."""
    ...

def best_bid_price(book: Any) -> float | None:
    """Return the highest bid price from port, SDK-raw, or test-dict book shapes."""
    ...

class LedgerTail:
    """Forward-only reader for a paper book's append-only ``ledger.jsonl``."""

    def __init__(self, ledger_file: Path, state_file: Path) -> None:
        ...

    def _initial_offset(self) -> int:
        ...

    def poll(self, max_records: int | None=None) -> list[dict[str, Any]]:
        ...

    def persist(self) -> None:
        ...

def build_production_adapter() -> Any:
    """Build the production adapter only after all locks are clean."""
    ...

class CopyRadarLiveExecutor:

    def __init__(self, *, config_loader: LiveConfigLoader | None=None, book: LiveBook | None=None, gate_source: Callable[[dict[str, Any], float], GateVerdict]=run_gate_decision, adapter_factory: Callable[[], Any]=build_production_adapter, source_ledger_file: Path | None=None, mirror_tail_state_file: Path | None=None, heartbeat_file: Path | None=None, kill_switch_file: Path | None=None, validation_stop_file: Path | None=None, validation_pairs_file: Path | None=None, validation_ladder_file: Path | None=None, log_file: Path | None=None, time_fn: Callable[[], float]=time.time, monotonic_fn: Callable[[], float]=time.monotonic, sleep_fn: Callable[[float], None]=time.sleep, reconcile_window_s: float=ORDER_RECONCILE_WINDOW_S, reconcile_poll_interval_s: float=ORDER_RECONCILE_POLL_INTERVAL_S) -> None:
        ...

    @property
    def adapter_constructed(self) -> bool:
        ...

    def _adapter_instance(self) -> Any:
        ...

    def _mirror_tail_for(self, source_book: str) -> LedgerTail:
        ...

    def _source_state_file(self) -> Path | None:
        """The mirrored paper book's ``state.json`` (read-only), if known."""
        ...

    def _validation_pair_rows(self) -> list[dict[str, Any]]:
        ...

    def _validation_metrics(self, now_ts: float | None=None) -> dict[str, Any]:
        ...

    def _validation_cumulative_delta(self) -> float:
        """Compatibility alias: the permanent-stop input is now realized PnL."""
        ...

    def _write_validation_stop(self, *, now_ts: float, cumulative_delta: float, reason: str='validation_realized_settled_loss_stop') -> None:
        ...

    def lock_state(self, config: dict[str, Any], gate: GateVerdict, now_ts: float) -> LockState:
        ...

    def startup_banner(self) -> LockState:
        ...

    def run_cycle(self, now_ts: float | None=None) -> dict[str, Any]:
        ...

    def _redeem(self, adapter: Any, now_ts: float, balance_before: float) -> float:
        ...

    def _process_mirror_open(self, row: dict[str, Any], config: dict[str, Any], locks: LockState, now_ts: float) -> dict[str, Any]:
        """Mirror a paper ``{source_book}_open`` row as a real limit BUY."""
        ...

    @staticmethod
    def _mirror_row_is_stale(opportunity: dict[str, Any], config: dict[str, Any], now_ts: float) -> bool:
        """A paper row older than ``max_mirror_age_s`` must not fire an order."""
        ...

    def _held_mirror_position(self, opportunity: dict[str, Any]) -> dict[str, Any] | None:
        """The live open position mirroring this paper detection, if any."""
        ...

    def _process_mirror_exit(self, row: dict[str, Any], config: dict[str, Any], locks: LockState, now_ts: float) -> dict[str, Any]:
        """Mirror a paper ``{source_book}_exit_sell`` row as a real limit SELL."""
        ...

    def _tick_size_for_token(self, adapter: Any, token_id: str) -> tuple[float, str]:
        ...

    def _shadow_ledger_record(self, detection_id: str) -> tuple[str, dict[str, Any] | None]:
        """Look the paper detection up in the mirrored book's ``state.json``."""
        ...

    def _shadow_prediction(self, opportunity: dict[str, Any], order: dict[str, Any]) -> dict[str, Any]:
        ...

    def _validation_components(self, opportunity: dict[str, Any], order: dict[str, Any], real: dict[str, Any], best_ask: float | None, shadow: dict[str, Any]) -> dict[str, Any]:
        ...

    def _append_validation_pair(self, opportunity: dict[str, Any], order: dict[str, Any], real: dict[str, Any], locks: LockState, *, now_ts: float, best_ask: float | None=None) -> None:
        ...

    def _validation_real_record(self, *, outcome: str, attempted: bool, order: dict[str, Any], submit_ts: float | None=None, fill_ts: float | None=None, fill_ts_source: str | None=None, best_ask: float | None=None, best_bid: float | None=None, fill_price: float | None=None, filled_size: float=0.0, filled_notional: float=0.0, balance_delta: float | None=None, principal_usd: float | None=None, fee_usd: float=0.0, fee_source: str='principal_unavailable_separately; fee_included_in_balance_delta', rejected: bool=False, order_id: str='', clob_order_status: str='', clob_order: Any=None, submit_response: Any=None, error: str='') -> dict[str, Any]:
        ...

    def _read_reconciliation_snapshot(self, adapter: Any, pending: dict[str, Any]) -> dict[str, Any]:
        ...

    def _poll_order_reconciliation(self, adapter: Any, pending: dict[str, Any]) -> tuple[str, dict[str, Any]]:
        ...

    def _finalize_filled_order(self, pending: dict[str, Any], snapshot: dict[str, Any], locks: LockState, now_ts: float, *, reconciled: bool) -> dict[str, Any]:
        ...

    def _finalize_rejected_order(self, pending: dict[str, Any], snapshot: dict[str, Any], locks: LockState, now_ts: float) -> dict[str, Any]:
        ...

    def _reconcile_pending_orders(self, adapter: Any, locks: LockState, now_ts: float) -> None:
        ...

    def _place_fok_buy(self, adapter: Any, opportunity: dict[str, Any], order: dict[str, Any], best_ask: float, now_ts: float, locks: LockState) -> dict[str, Any]:
        ...

    def _place_fok_sell(self, adapter: Any, opportunity: dict[str, Any], position: dict[str, Any], order: dict[str, Any], best_bid: float, now_ts: float, locks: LockState) -> dict[str, Any]:
        """Submit the mirror SELL, structured exactly like the BUY path."""
        ...

    def _finalize_filled_sell(self, pending: dict[str, Any], snapshot: dict[str, Any], locks: LockState, now_ts: float, *, reconciled: bool) -> dict[str, Any]:
        """Move the sold position to settled with balance-delta sale accounting."""
        ...

    def _append_mirror_sell_settlement_credit(self, settled: dict[str, Any], *, order_id: str, credit_usd: float, shares_sold: float, now_ts: float) -> None:
        """Append the sale proceeds as a settlement-credit accounting marker."""
        ...

    def _skip(self, opportunity: dict[str, Any], reason: str, now_ts: float, intended: dict[str, Any], locks: LockState) -> dict[str, Any]:
        ...

    def _append_decision(self, event: dict[str, Any]) -> None:
        ...

    def flush(self, status: str='stopped') -> None:
        ...

class _StopFlag:

    def __init__(self) -> None:
        ...

    def request(self, signum: int, _frame: object) -> None:
        ...

    @property
    def stopped(self) -> bool:
        ...

def _interruptible_sleep(seconds: float, stop: _StopFlag) -> None:
    ...

def run_loop(*, once: bool=False, max_cycles: int | None=None) -> int:
    ...
