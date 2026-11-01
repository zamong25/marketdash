"""Per-order cumulative fill ledger."""

@dataclass
class FillDelta:
    """Result of a single accepted fill: how much was added to the"""
    added_shares: float
    cumulative_shares: float
    avg_price: float

@dataclass
class _TrackedOrder:
    venue_order_id: str
    submitted_shares: float
    price_hint: float
    cumulative_shares: float
    cumulative_cost: float
    closed: bool

class OrderFillTracker:

    def __init__(self, *, dedup_cap: int=DEDUP_CAP) -> None:
        ...

    def register(self, venue_order_id: str, submitted_shares: float, price_hint: float) -> None:
        """Record that an order was submitted. Idempotent — repeat"""
        ...

    def forget(self, venue_order_id: str) -> None:
        ...

    def record_fill(self, venue_order_id: str, trade_id: str, shares: float, price: float) -> FillDelta | None:
        """Accept a fill. Returns a :class:`FillDelta` or ``None`` if"""
        ...

    def snap_fill_qty(self, shares: float, cumulative: float, submitted: float) -> float:
        """Return the fill quantity the tracker should bookkeep."""
        ...

    def cumulative(self, venue_order_id: str) -> float:
        ...

    def avg_price(self, venue_order_id: str) -> float:
        ...

    def submitted(self, venue_order_id: str) -> float:
        ...

    def _evict_dedup(self) -> None:
        ...
