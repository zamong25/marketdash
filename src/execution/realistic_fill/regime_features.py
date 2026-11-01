"""Shared market-regime feature bucketing for realistic-fill effects."""

def spread_bucket(spread: float, edges: tuple[float, float]=DEFAULT_SPREAD_EDGES) -> str:
    ...

def signal_remaining_bucket(remaining_s: int | float, edges: tuple[int, int]=DEFAULT_SIGNAL_REMAINING_EDGES) -> str:
    ...
