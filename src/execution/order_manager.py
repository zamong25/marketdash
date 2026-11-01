
@dataclass(frozen=True)
class OrderDecision:
    accepted: bool
    reason: str

class OrderManager:

    def __init__(self, *, execution_mode: ExecutionMode, market_meta_client: MarketMetaClient, safety_guard: SafetyGuard, settlement_manager: SettlementManager, paper_executor: PaperExecutionEngine, live_executor=None) -> None:
        ...

    def _executor(self):
        ...

    def _build_ctx(self, strategy_name: str, config_version: str, balance_cache: BalanceCache | None=None, paper_mode: str='snapshot') -> RuntimeContext:
        ...

    def _execute_order_for_strategy(self, ctx: RuntimeContext, order: Order, snapshot: MarketSnapshot, *, use_fast_path: bool, signal: Signal | None=None, signal_price: float | None=None, signal_ts: int | None=None, requested_shares: int | None=None, portfolio: PortfolioState | None=None) -> Fill | None:
        ...

    def log_settlement(self, ctx_or_name, result, *, redemption_status: str='n/a', redemption_proceeds_usd: float | None=None, redemption_tx_hash: str | None=None, redemption_error: str='', entry_order_id: str | None=None) -> None:
        ...

    def log_redemption_completed(self, ctx_or_name, *, window_slug: str, redemption_status: str, proceeds_usd: float | None, cost_usd: float, shares_held: float, entry_direction: str, entry_order_id: str | None, redemption_tx_hash: str | None, redemption_error: str='') -> None:
        ...

    def log_redemption_confirmation(self, ctx_or_name, *, window_slug: str, token_id: str, condition_id: str, shares_redeemed: float, cost_usd: float, proceeds_usd: float, entry_direction: str, entry_order_id: str | None, redemption_tx_hash: str | None, observation_source: str, observed_at_unix: int) -> None:
        ...

    def _emit_rejection(self, ctx: RuntimeContext, snapshot: MarketSnapshot, signal: Signal, signal_price: float, signal_ts: int, reason: str, detail: str='') -> None:
        """Append a live_rejected / paper_rejected record so that failed"""
        ...

    def process_signal(self, strategy_name: str, signal: Signal, snapshot: MarketSnapshot, tracker: PositionTracker, *, daily_loss_limit: float | None=None, config_version: str='unknown', use_fast_path: bool=False, balance_cache: BalanceCache | None=None, min_order_shares: int | None=None, paper_mode: str='snapshot') -> OrderDecision:
        ...
