"""Helpers for synthetic snapshot-based fallback books."""

@runtime_checkable
class PointInTimeSnapshotProvider(Protocol):
    """Duck-typed interface for per-second market snapshot lookup."""

    def snapshot(self, slug: str, ts_s: int) -> MarketSnapshot | None:
        ...

def build_snapshot_fallback_book(*, token_id: str, ask_price: float | None, ask_depth: float | None, ts_ms: int | None) -> BookSnapshot | None:
    """Return a 1-level synthetic book from explicit ask/depth values."""
    ...

def build_order_time_snapshot_fallback_book(*, provider: PointInTimeSnapshotProvider | None, window_slug: str, direction: str, token_id: str, attempt_ts_ms: int | None) -> BookSnapshot | None:
    """Resolve a synthetic book from the snapshot nearest ``attempt_ts_ms``."""
    ...
