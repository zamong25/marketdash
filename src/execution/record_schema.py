"""Trade log record builders — schema version 2."""

@dataclass(frozen=True)
class RuntimeContext:
    """Passed from Runner → OrderManager → Executor so every record can be"""
    strategy_name: str
    config_version: str
    mode: str
    balance_cache: BalanceCache | None
    paper_mode: str

    @classmethod
    def from_execution_mode(cls, strategy_name: str, config_version: str, execution_mode: ExecutionMode, balance_cache: BalanceCache | None=None, paper_mode: str='snapshot') -> 'RuntimeContext':
        ...

def _now_iso() -> str:
    ...

def _build_envelope(record_type: str, ctx: RuntimeContext, window_slug: str) -> dict[str, Any]:
    ...

def snapshot_to_context(snapshot: MarketSnapshot) -> dict[str, Any]:
    """Serialize a MarketSnapshot into a jsonl-friendly dict."""
    ...

def portfolio_to_context(portfolio: PortfolioState) -> dict[str, Any]:
    ...

def build_entry_payload(*, ctx: RuntimeContext, order: Order, snapshot: MarketSnapshot, fill: Fill, signal: Signal, signal_price: float, signal_ts: int, fill_status: str, requested_shares: int, portfolio: PortfolioState | None, live_meta: dict[str, Any] | None=None) -> dict[str, Any]:
    """Build a paper_buy / live_buy record."""
    ...

def build_rejection_payload(*, ctx: RuntimeContext, snapshot: MarketSnapshot, direction: str, requested_shares: int, signal_price: float, signal_ts: int, rejection_reason: str, rejection_detail: str='', diagnostics: dict[str, Any] | None=None) -> dict[str, Any]:
    """Build a live_rejected record — an order that never actually filled."""
    ...

def build_settlement_payload(*, ctx: RuntimeContext, result: SettlementResult, redemption_status: str='n/a', redemption_proceeds_usd: float | None=None, redemption_tx_hash: str | None=None, redemption_error: str='', entry_order_id: str | None=None) -> dict[str, Any]:
    """Build a paper_settlement / live_settlement record."""
    ...

def build_redemption_confirmation_payload(*, ctx: RuntimeContext, window_slug: str, token_id: str, condition_id: str, shares_redeemed: float, cost_usd: float, proceeds_usd: float, entry_direction: str, entry_order_id: str | None, redemption_tx_hash: str | None, observation_source: str, observed_at_unix: int) -> dict[str, Any]:
    """Build a ``redemption_confirmation`` record."""
    ...

def build_redemption_completed_payload(*, ctx: RuntimeContext, window_slug: str, redemption_status: str, proceeds_usd: float | None, cost_usd: float, shares_held: float, entry_direction: str, entry_order_id: str | None, redemption_tx_hash: str | None, redemption_error: str='') -> dict[str, Any]:
    """Build a redemption_completed record."""
    ...
