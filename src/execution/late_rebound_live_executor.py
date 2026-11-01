"""Manual last-minute cheap-side rebound execution button."""

def live_enabled() -> bool:
    """True only when the operator has explicitly opted into real orders."""
    ...

def _fee_per_share(price: float) -> float:
    ...

def target_sell_price(entry_price: float, roi_target: float) -> float:
    """Smallest tradable cents price whose net-of-fee ROI over entry >= target."""
    ...

@dataclass
class ButtonResult:
    mode: str
    accepted: bool
    reason: str
    side: str
    token_id: str
    requested_usd: float
    shares: float
    entry_price: float
    target_sell_price: float
    cost_usd: float
    fee: float
    cost_source: str
    buy_order_id: str
    sell_order_id: str
    detail: str
    live_enabled: bool

    def to_dict(self) -> dict[str, Any]:
        ...

@dataclass
class _Session:
    spent_usd: float
    open_positions: int

class LateReboundButton:
    """One manual press = one window. Shadow by default; live is bounded + gated."""

    def __init__(self, adapter: VenueAdapter | None=None, *, log_root: str | Path=DEFAULT_LOG_ROOT, per_order_usd: float=PER_ORDER_USD_CAP, per_session_usd: float=PER_SESSION_USD_CAP, max_concurrent: int=MAX_CONCURRENT, fee_rate: float=FEE_RATE) -> None:
        ...

    @property
    def adapter(self) -> VenueAdapter:
        ...

    def execute(self, decision: dict[str, Any], market: dict[str, Any] | None, *, mode: str, stake_usd: float, snapshot_ts: float | None=None, now_ts: float | None=None) -> ButtonResult:
        ...

    def _shadow(self, decision: dict[str, Any], market: dict[str, Any], stake_usd: float) -> ButtonResult:
        ...

    def _live(self, decision: dict[str, Any], market: dict[str, Any], stake_usd: float, snapshot_ts: float | None, now_ts: float | None) -> ButtonResult:
        ...

    @staticmethod
    def _target(decision: dict[str, Any], market: dict[str, Any]) -> tuple[str, str, float, float]:
        ...

    def _mk(self, mode: str, accepted: bool, reason: str, side: str, token_id: str, usd: float, **kw: Any) -> ButtonResult:
        ...

    def _reject(self, side: str, token_id: str, usd: float, reason: str, *, detail: str='', release: bool=False) -> ButtonResult:
        ...

    def _log(self, event: str, res: ButtonResult, *, extra: dict[str, Any] | None=None) -> None:
        ...

def _source_str(value: Any) -> str:
    ...

def _num(value: Any) -> float | None:
    ...

def _pos(value: Any) -> float:
    ...
