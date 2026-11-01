"""BTC movement helpers shared by strategies."""

def btc_move_pct(snapshot: MarketSnapshot) -> float:
    """Signed BTC move from window start, expressed in percentage points."""
    ...

def btc_velocity_pct(history: list[MarketSnapshot], snapshot: MarketSnapshot, lookback_s: int) -> float | None:
    """Signed BTC velocity over ``lookback_s``, in percentage points."""
    ...

def btc_range_position_pct(history: list[MarketSnapshot], snapshot: MarketSnapshot, lookback_s: int) -> float | None:
    """Return BTC's current position inside the recent range."""
    ...

def btc_aligned(move: float, direction: SignalDirection | str, threshold: float) -> bool:
    """Return true when signed BTC move agrees with ``direction``."""
    ...
