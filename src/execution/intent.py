
def _as_float(value: Any, default: float) -> float:
    ...

def _as_int(value: Any, default: int) -> int:
    ...

def _as_bool(value: Any, default: bool) -> bool:
    ...

def resolve_requested_shares(strategy_shares: int | float | None, *, fallback_notional_usd: float, price_anchor: float) -> float:
    """Resolve requested entry size with the same fallback rule everywhere."""
    ...

def resolve_signal_price_from_info(snapshot: MarketSnapshot, direction: str, signal_info: Mapping[str, Any] | None) -> float:
    """Prefer the strategy's explicit expensive-side anchor when present."""
    ...

@dataclass(frozen=True)
class EntryIntent:
    token_id: str
    direction: str
    window_slug: str
    requested_shares: float
    signal_price: float
    signal_ts_s: int
    order_price: float
    reason: str
    max_price: float
    include_fee: bool
    fak_retry_enabled: bool
    fak_retry_backoff_s: float
    fak_max_retries: int
    retry_min_remaining_s: int
    min_ask_depth_shares: float
    min_retry_threshold: float
    snapshot_sanity_enabled: bool
    max_snapshot_ask_gap: float
    use_fast_path: bool
    extra_info: dict[str, Any]

    @property
    def budget_usd(self) -> float:
        ...

    def to_order(self) -> Order:
        ...

def build_entry_intent(*, token_id: str, direction: str, window_slug: str, requested_shares: float, signal_price: float, signal_ts_s: int, order_price: float, reason: str='', signal_info: Mapping[str, Any] | None=None, max_price: float=DEFAULT_MAX_PRICE, use_fast_path: bool=DEFAULT_USE_FAST_PATH) -> EntryIntent:
    ...

def build_entry_intent_from_signal(*, snapshot: MarketSnapshot, signal: Signal, token_id: str, max_price: float=DEFAULT_MAX_PRICE, use_fast_path: bool=DEFAULT_USE_FAST_PATH) -> EntryIntent:
    ...
