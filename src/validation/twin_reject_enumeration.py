
def _safe_float(value: object) -> float | None:
    ...

def _safe_int(value: object) -> int | None:
    ...

def _safe_str(value: object) -> str | None:
    ...

def _trade_paths(log_root: Path, strategy_name: str, date: str) -> tuple[Path, ...]:
    ...

def _iter_trade_records(paths: Iterable[Path]) -> Iterable[dict[str, Any]]:
    ...

def _parse_logged_at(value: object) -> datetime | None:
    ...

def _event_ts(row: dict[str, Any]) -> float:
    ...

def _dedupe_key(record: dict[str, Any]) -> tuple[object, ...]:
    ...

def _mode_of(record: dict[str, Any]) -> str | None:
    ...

def load_trade_records(log_root: str | Path, strategy_name: str, date: str) -> tuple[dict[str, Any], ...]:
    ...

@dataclass(frozen=True)
class PortfolioCheckpoint:
    logged_at: str | None
    daily_pnl: float | None
    daily_trades: int | None
    open_position_count: int | None
    pending_settlement_slug: str | None

@dataclass(frozen=True)
class PortfolioEstimate:
    checkpoint: PortfolioCheckpoint | None
    settlement_pnl_since_checkpoint: float

    @property
    def estimated_daily_pnl(self) -> float | None:
        ...

@dataclass(frozen=True)
class TwinRejectEnumerationRow:
    classification: str
    twin_run_id: str
    strategy_name: str
    window_slug: str
    logged_at: str | None
    signal_ts: int | None
    signal_direction: str | None
    signal_price: float | None
    order_price: float | None
    order_price_source: str | None
    order_shares: float | None
    live_decision: str | None
    live_rejection_reason: str | None
    live_rejection_detail: str | None
    live_adapter_error_raw: str | None
    diagnostics_order_type_used: str | None
    diagnostics_fak_exception: str | None
    diagnostics_post_trade_refresh_error: str | None
    diagnostics_fak_returned_shares: float | None
    diagnostics_bridge_returned_shares: float | None
    paper_same_signal_decision: str | None
    paper_same_signal_rejection_reason: str | None
    paper_same_signal_rejection_detail: str | None
    paper_same_signal_fill_price: float | None
    paper_same_signal_filled_shares: float | None
    paper_same_signal_reason: str | None
    live_prev_daily_pnl: float | None
    live_prev_daily_trades: int | None
    live_prev_open_position_count: int | None
    live_prev_pending_settlement_slug: str | None
    live_prev_portfolio_logged_at: str | None
    live_estimated_daily_pnl: float | None
    live_settlement_pnl_since_prev_checkpoint: float
    paper_prev_daily_pnl: float | None
    paper_prev_daily_trades: int | None
    paper_prev_open_position_count: int | None
    paper_prev_pending_settlement_slug: str | None
    paper_prev_portfolio_logged_at: str | None
    paper_estimated_daily_pnl: float | None
    paper_settlement_pnl_since_prev_checkpoint: float
    book_best_bid: float | None
    book_best_ask: float | None
    book_bid_size: float | None
    book_ask_size: float | None
    book_leading_depth: float | None
    book_spread: float | None
    book_events_per_sec: float | None
    book_remaining_s: float | None
    snapshot_ts_unix: int | None
    live_ask_depth_at_order: float | None
    live_ask_price_at_order: float | None

    def to_dict(self) -> dict[str, Any]:
        ...

def _portfolio_checkpoint(record: dict[str, Any]) -> PortfolioCheckpoint | None:
    ...

def _settlement_pnl(record: dict[str, Any], *, mode: str) -> float | None:
    ...

def _estimate_portfolio_state(records: Iterable[dict[str, Any]], *, mode: str, cutoff: datetime | None) -> PortfolioEstimate:
    ...

def _resolve_order_price(live_row: dict[str, Any]) -> tuple[float | None, str | None]:
    ...

def build_twin_reject_enumeration_rows(log_root: str | Path, strategy_name: str, date: str, *, classification: str='live_reject_paper_missing') -> tuple[TwinRejectEnumerationRow, ...]:
    ...

def write_twin_reject_enumeration_csv(rows: Iterable[TwinRejectEnumerationRow], path: str | Path) -> Path:
    ...
