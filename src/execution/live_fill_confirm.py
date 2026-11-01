"""WebSocket fill confirmation helper."""

@dataclass(frozen=True)
class FillConfirmation:
    """Result of a single :meth:`FillConfirmer.confirm` call."""
    shares: float | None
    price: float | None
    source: str
    matched_at_ms: int | None
    mined_at_ms: int | None

class FillConfirmer:
    """Minimal wrapper around the FillBridge register + await protocol."""

    def __init__(self, bridge: 'FillBridge | None', timeout_s: float) -> None:
        ...

    @property
    def bridge(self) -> 'FillBridge | None':
        ...

    @property
    def timeout_s(self) -> float:
        ...

    def confirm(self, *, venue_order_id: str, requested_shares: float, price_hint: float) -> FillConfirmation:
        """Register ``venue_order_id`` with the bridge, wait up to"""
        ...
