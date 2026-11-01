
@dataclass(frozen=True)
class SafetyLimits:
    max_total_exposure_usd: float
    max_single_position_usd: float
    max_daily_loss_usd: float
    max_staleness_seconds: int
    min_order_shares: int
    kill_switch_file: str

class SafetyGuard:

    def __init__(self, limits: SafetyLimits) -> None:
        ...

    def current_exposure(self, portfolio: PortfolioState) -> float:
        ...

    def check_snapshot(self, snapshot: MarketSnapshot) -> tuple[bool, str]:
        ...

    def check_entry(self, order: Order, portfolio: PortfolioState, snapshot: MarketSnapshot, *, daily_loss_limit: float | None=None, min_order_shares: int | None=None) -> tuple[bool, str]:
        ...
