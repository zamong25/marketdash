"""Window-level deduplication helpers."""

@dataclass
class WindowDedupTracker:
    """Tracks windows that have already emitted a signal."""
    traded_windows: set[str]

    def seen(self, window_slug: str) -> bool:
        ...

    def mark(self, window_slug: str) -> None:
        ...

    def clear(self) -> None:
        ...

    def add(self, window_slug: str) -> None:
        ...

    def __contains__(self, window_slug: object) -> bool:
        ...
