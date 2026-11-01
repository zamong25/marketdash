
def _as_float(value: Any, default: float=0.0) -> float:
    ...

def _as_int(value: Any, default: int=0) -> int:
    ...

def _side_name(direction: SignalDirection | str) -> str:
    ...

@dataclass(frozen=True)
class MarketSnapshot:
    """Point-in-time market state. Immutable. Built from data/live/realtime/latest.json."""
    ts: datetime
    window_slug: str
    up_price: float
    best_bid: float
    best_ask: float
    bid_size: float
    ask_size: float
    last_price: float
    events_per_sec: float
    btc_price: float
    btc_start: float
    btc_volume: float
    btc_trade_count: int
    btc_taker_buy_volume: float
    btc_oi_change_pct: float
    btc_long_short_ratio: float
    btc_taker_buy_ratio_15m: float
    btc_liq_long_usd_1m: float
    btc_liq_short_usd_1m: float
    btc_liq_long_usd_5m: float
    btc_liq_short_usd_5m: float
    remaining_s: int
    down_price: float
    spread: float
    leading_side: str
    leading_price: float
    leading_ask: float
    leading_depth: float
    btc_lead_pct: float
    btc_direction: str
    btc_oi_change_pct_1h: float
    btc_ls_change_1h: float
    down_mid: float
    down_best_bid: float
    down_best_ask: float
    down_bid_size: float
    down_ask_size: float
    down_last_price: float
    features: Dict[str, float]
    meta: Dict[str, Any]

    @property
    def ts_unix(self) -> int:
        ...

    @property
    def window_start_ts(self) -> int:
        ...

    @property
    def window_end_ts(self) -> int:
        ...

    @property
    def elapsed_s(self) -> int:
        ...

    @property
    def cheap_side(self) -> str:
        ...

    @property
    def cheap_price(self) -> float:
        ...

    @property
    def cheap_ask(self) -> float:
        ...

    @property
    def cheap_depth(self) -> float:
        ...

    def price_for_direction(self, direction: SignalDirection | str) -> float:
        ...

    def ask_for_direction(self, direction: SignalDirection | str) -> float:
        ...

    def same_side_ask_for_direction(self, direction: SignalDirection | str) -> float:
        ...

    def depth_for_direction(self, direction: SignalDirection | str) -> float:
        ...

    def same_side_depth_for_direction(self, direction: SignalDirection | str) -> float:
        ...

    @classmethod
    def from_latest_json(cls, data: Mapping[str, Any]) -> 'MarketSnapshot':
        ...

@dataclass(frozen=True)
class Signal:
    """Strategy output. Immutable."""
    ts: datetime
    direction: SignalDirection
    confidence: float
    trade_shares: int
    reason: str
    info: Dict[str, Any]

@dataclass(frozen=True)
class Order:
    """Order intent. Immutable."""
    side: str
    token_id: str
    shares: float
    price: float
    order_type: str
    info: Dict[str, Any]

@dataclass(frozen=True)
class Fill:
    """Execution report. Immutable."""
    ts: datetime
    order_id: str
    side: str
    shares: float
    price: float
    cost_usd: float
    fee: float
    info: Dict[str, Any]

@dataclass(frozen=True)
class SettlementResult:
    """5-minute window settlement outcome. ``shares_held`` is float to"""
    window_slug: str
    outcome: str
    shares_held: float
    pnl_usd: float
    info: Dict[str, Any]

@dataclass
class PortfolioState:
    """Mutable portfolio state. Only runner modifies this."""
    cash: float
    positions: Dict[str, float]
    avg_entry: Dict[str, float]
    pending_settlement: Optional[str]
    daily_pnl: float
    daily_trades: int
    info: Dict[str, Any]
