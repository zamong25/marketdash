
@dataclass
class TrackedPosition:
    window_slug: str
    direction: SignalDirection
    token_id: str
    shares: float
    entry_price: float
    cost_usd: float
    opened_at: datetime
    hold_model: str
    info: dict[str, Any]

class PositionTracker:

    def __init__(self, name: str, starting_cash: float=100.0) -> None:
        ...

    def in_position(self) -> bool:
        ...

    def current_exposure(self) -> float:
        ...

    def register_entry(self, position: TrackedPosition) -> None:
        ...

    def register_exit(self, fill: Fill) -> float:
        ...

    def apply_settlement(self, result: SettlementResult) -> None:
        ...

    def _clear_position(self) -> None:
        ...
