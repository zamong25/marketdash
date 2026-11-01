"""History selection helpers shared by strategies."""

def same_window_history(history: list[MarketSnapshot], slug: str) -> list[MarketSnapshot]:
    """Return snapshots from ``history`` that belong to ``slug``."""
    ...

def history_at_offset(history: list[MarketSnapshot], now_ts: int, offset_s: int) -> MarketSnapshot | None:
    """Return the latest snapshot at or before ``now_ts - offset_s``."""
    ...
