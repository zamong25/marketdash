
@dataclass(frozen=True)
class ShareFillWalkResult:
    avg_fill_price: float | None
    filled_shares: float
    levels_used: int
    remaining_shares: float

    @property
    def status(self) -> str:
        ...

@dataclass(frozen=True)
class NotionalFillWalkResult:
    avg_fill_price: float | None
    filled_shares: float
    filled_notional: float
    levels_used: int
    remaining_notional: float
    status: str

def walk_share_levels(prices: list[float], sizes: list[float], requested_shares: float, *, max_price: float | None=None) -> ShareFillWalkResult:
    ...

def walk_notional_levels(prices: list[float], sizes: list[float], requested_notional: float, *, max_price: float | None=None) -> NotionalFillWalkResult:
    ...

def compute_binary_fee(price: float, shares: float, fee_rate: float) -> float:
    ...

def compute_cost_usd(side: str, price: float, shares: float, fee_rate: float) -> tuple[float, float]:
    ...
