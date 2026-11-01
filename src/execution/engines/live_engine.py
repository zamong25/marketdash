
class LiveExecutionEngine:

    def __init__(self, adapter: VenueAdapter, log_root: str | Path, fee_rate: float=0.072, *, book_provider: 'BookProvider | None'=None, fill_bridge: 'FillBridge | None'=None, fill_confirm_timeout_s: float=DEFAULT_FILL_CONFIRM_TIMEOUT_S) -> None:
        ...

    def _log_path(self, strategy_name: str) -> Path:
        ...

    def _latency_path(self) -> Path:
        ...

    def _log_latency(self, *, ctx: RuntimeContext | None, snapshot: MarketSnapshot | None, stage: str, stage_start: float, total_start: float | None, attempt: int=1, success: bool, extra: dict | None=None) -> None:
        ...

    def _resolve_ctx(self, ctx_or_name) -> RuntimeContext:
        ...

    def _confirm_fill_via_bridge(self, *, venue_order_id: str, requested_shares: float, price_hint: float, adapter_filled_shares: float | None) -> FillConfirmation:
        """Thin delegate to :class:`FillConfirmer`."""
        ...

    def _preflight_ask_depth(self, token_id: str, *, ctx: RuntimeContext | None=None, snapshot: MarketSnapshot | None=None, total_start: float | None=None, attempt: int=1, stage_prefix: str='') -> tuple[float, float]:
        """Re-read the order book just before submission to check that the"""
        ...

    def _preflight_from_book_provider(self, token_id: str, *, ctx: RuntimeContext | None, snapshot: MarketSnapshot, total_start: float | None, attempt: int, stage_prefix: str) -> tuple[float, float]:
        """WebSocket-backed preflight via ``realistic_fill.LiveBookProvider``."""
        ...

    def _submit_fak(self, token_id: str, side: str, amount: float, *, ctx: RuntimeContext | None=None, snapshot: MarketSnapshot | None=None, total_start: float | None=None, attempt: int=1, stage_prefix: str=''):
        """Submit one FAK market order and return the adapter result or an"""
        ...

    def _post_balance_delta(self, token_id: str, usdc_before: float, token_before: float, *, ctx: RuntimeContext | None=None, snapshot: MarketSnapshot | None=None, total_start: float | None=None, attempt: int=1) -> tuple[float, float, float] | None:
        """Read balances 2 seconds after a submission and return"""
        ...

    def execute(self, *, order: Order, snapshot: MarketSnapshot, signal: Signal, ctx: RuntimeContext) -> ExecutionResult:
        ...

    def execute_order(self, ctx_or_name, order: Order, snapshot: MarketSnapshot, *, signal: Signal | None=None, signal_price: float | None=None, signal_ts: int | None=None, requested_shares: int | None=None, portfolio: PortfolioState | None=None) -> Fill | None:
        ...

    def fast_execute_order(self, ctx_or_name, order: Order, snapshot: MarketSnapshot, *, signal: Signal | None=None, signal_price: float | None=None, signal_ts: int | None=None, requested_shares: int | None=None, portfolio: PortfolioState | None=None) -> Fill | None:
        ...

    def log_settlement(self, ctx_or_name, result: SettlementResult, *, redemption_status: str='pending', redemption_proceeds_usd: float | None=None, redemption_tx_hash: str | None=None, redemption_error: str='', entry_order_id: str | None=None) -> None:
        ...

    def log_redemption_completed(self, ctx_or_name, *, window_slug: str, redemption_status: str, proceeds_usd: float | None, cost_usd: float, shares_held: float, entry_direction: str, entry_order_id: str | None, redemption_tx_hash: str | None, redemption_error: str='') -> None:
        ...

    def log_redemption_confirmation(self, ctx_or_name, *, window_slug: str, token_id: str, condition_id: str, shares_redeemed: float, cost_usd: float, proceeds_usd: float, entry_direction: str, entry_order_id: str | None, redemption_tx_hash: str | None, observation_source: str, observed_at_unix: int) -> None:
        """Emit a ``redemption_confirmation`` record."""
        ...

def _synthetic_signal(order: Order, snapshot: MarketSnapshot):
    ...
