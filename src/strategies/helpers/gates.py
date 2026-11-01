"""Shared gate predicates for strategy decision code."""

@dataclass(frozen=True)
class PriceBandRule:
    """Inclusive expensive/cheap side price bounds."""
    min_expensive: float | None
    max_expensive: float | None
    min_cheap: float | None
    max_cheap: float | None

def scan_window_ok(elapsed_s: int, start: int, end: int) -> bool:
    """Return true when ``elapsed_s`` is within the inclusive scan window."""
    ...

def _value(rule: PriceBandRule | Mapping[str, Any], *names: str) -> float | None:
    ...

def price_band_ok(exp_px: float, cheap_px: float, rule: PriceBandRule | Mapping[str, Any]) -> bool:
    """Return true when prices satisfy inclusive bounds in ``rule``."""
    ...

def daily_dd_ok(portfolio: PortfolioState, limit: float | None) -> bool:
    """Return true when the daily drawdown guard has not tripped."""
    ...
