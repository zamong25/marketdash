"""Microstructure helpers shared by pm_btc_disagree, start_hug_extended,"""

def signed_btc_lead_pct(snapshot: MarketSnapshot) -> float:
    """BTC distance from window start as a signed fraction."""
    ...

def within_scan_window(snapshot: MarketSnapshot, low: int, high: int) -> bool:
    """True iff ``snapshot.remaining_s`` is in the inclusive range"""
    ...

def daily_dd_hit(portfolio: PortfolioState, limit: float) -> bool:
    """True if the portfolio daily PnL has crossed the negative"""
    ...

def live_fill_order_info(params: Mapping[str, Any]) -> dict[str, Any]:
    """Live fill-rate guard subset to thread through ``order.info``."""
    ...
