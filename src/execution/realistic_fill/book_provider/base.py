"""Orderbook snapshot + provider abstraction."""

def _touch_index(prices: list[float], *, want_max: bool) -> int | None:
    """Index of the best level, so no caller has to know the ladder's order."""
    ...

@dataclass(frozen=True)
class BookSnapshot:
    """Immutable point-in-time depth view for a single token."""
    ts_ms: int
    token_id: str
    ask_prices: list[float]
    ask_sizes: list[float]
    bid_prices: list[float]
    bid_sizes: list[float]

    @property
    def best_ask(self) -> float | None:
        ...

    @property
    def best_ask_size(self) -> float:
        ...

    @property
    def best_bid(self) -> float | None:
        ...

    @property
    def best_bid_size(self) -> float:
        ...

class BookProvider(Protocol):
    """Return the most recent book snapshot for ``(window, token, ts_ms)``."""

    def book_at(self, window_slug: str, token_id: str, ts_ms: int) -> BookSnapshot | None:
        ...
