"""Parsed Venue WebSocket event types."""

class TradeStatus(str, Enum):

    @classmethod
    def from_raw(cls, value: object) -> 'TradeStatus | None':
        ...

@dataclass(frozen=True)
class FillEvent:
    """A single on-chain matched amount belonging to one order."""
    trade_id: str
    venue_order_id: str
    shares: float
    price: float
    status: TradeStatus
    ts_ms: int

@dataclass(frozen=True)
class TradeEvent:
    """A parsed user-channel TRADE message."""
    status: TradeStatus
    ts_ms: int
    fills: list[FillEvent]

    @property
    def is_finalized(self) -> bool:
        ...
