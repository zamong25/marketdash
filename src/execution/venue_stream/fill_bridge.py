"""Thread-safe bridge between the WebSocket listener and the sync executor."""

@dataclass
class FillResult:
    venue_order_id: str
    cumulative_shares: float
    avg_price: float
    status: TradeStatus | None
    was_timeout: bool
    event_count: int
    first_matched_at_ms: int | None
    first_mined_at_ms: int | None

@dataclass
class _Entry:
    event: threading.Event
    submitted_shares: float
    price_hint: float
    registered_at: float
    last_status: TradeStatus | None
    event_count: int
    first_matched_at_ms: int | None
    first_mined_at_ms: int | None

class FillBridge:

    def __init__(self, *, logger: logging.Logger | None=None, expiry_s: float=ENTRY_EXPIRY_S, preregister_buffer_s: float=PREREGISTER_BUFFER_S, now_s_fn: Callable[[], float] | None=None, wall_now_ms_fn: Callable[[], int] | None=None) -> None:
        ...

    def stop(self) -> None:
        """Wake every waiter so they can observe shutdown and return."""
        ...

    def register(self, venue_order_id: str, submitted_shares: float, price_hint: float) -> None:
        """Announce that an order was submitted. Drains any buffered"""
        ...

    def await_fill(self, venue_order_id: str, timeout_s: float) -> FillResult:
        """Block the calling thread until a finalized event arrives or"""
        ...

    def forget(self, venue_order_id: str) -> None:
        ...

    def on_trade_event(self, event: TradeEvent) -> None:
        """Entry point for the UserChannelClient callback. Iterates the"""
        ...

    def _route_fill(self, fill: FillEvent) -> None:
        ...

    def _apply_fill_locked(self, fill: FillEvent) -> None:
        ...

    def _sweep_expired_locked(self) -> None:
        ...
