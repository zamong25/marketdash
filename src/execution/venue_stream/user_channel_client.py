"""Daemon-thread WebSocket listener for the Venue user channel."""

@dataclass
class UserChannelStats:
    """Lightweight counters for observability — a supervisor can spot a"""
    messages_received: int
    parse_errors: int
    reconnects: int
    last_event_ts_ms: int

class UserChannelClient:
    """Venue user-channel listener."""

    def __init__(self, credentials: UserChannelCredentials, markets: Iterable[str], on_trade: OnTradeCallback, *, ws_url: str=DEFAULT_WS_URL, logger: logging.Logger | None=None, websocket_factory: Callable[..., Any] | None=None) -> None:
        ...

    @property
    def stats(self) -> UserChannelStats:
        ...

    def is_alive(self) -> bool:
        ...

    def start(self) -> None:
        ...

    def stop(self, timeout_s: float=5.0) -> None:
        ...

    def _thread_main(self) -> None:
        ...

    async def _run_forever(self) -> None:
        ...

    async def _connect_and_stream(self) -> None:
        """Open one WebSocket session and dispatch messages until it"""
        ...

    async def _send_subscription(self, ws) -> None:
        """Send the user-channel subscription payload."""
        ...

def _default_websocket_factory():
    """Return the ``websockets.connect`` coroutine lazily so test"""
    ...
