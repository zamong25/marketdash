"""pm_events source abstraction for contrarian_taker_fade."""

@dataclass(frozen=True)
class TakerEvent:
    """Canonical per-event record for feature computation."""
    ts_ms: int
    event_type: str
    side: str
    price: float
    size: float
    token_id: str

class TakerStream(Protocol):
    """Read-side interface over a window's pm_events."""

    def get_recent(self, window_slug: str, now_ms: int, window_s: float) -> list[TakerEvent]:
        """Return events in (now_ms - window_s * 1000, now_ms]."""
        ...

class ParquetTakerStream:
    """Read pm_events from parquet files under ``events_root``."""

    def __init__(self, events_root: str | Path):
        ...

    def get_recent(self, window_slug: str, now_ms: int, window_s: float) -> list[TakerEvent]:
        ...

    def invalidate(self, window_slug: str) -> None:
        """Drop a window's cache entry (e.g. after settlement)."""
        ...

    def _ensure_window_loaded(self, window_slug: str) -> list[TakerEvent]:
        ...

    def _load_window_from_parquet(self, window_slug: str) -> list[TakerEvent]:
        """Scan the date dirs this window spans and collect its events."""
        ...

def _window_start_ts(slug: str) -> int:
    ...

def _window_date(ts_s: int) -> str:
    ...
