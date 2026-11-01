
@dataclass
class PendingSettlement:
    strategy_name: str
    position: TrackedPosition
    last_poll_at: float

class SettlementManager:
    """Orchestrates settlement detection + redemption lifecycle."""

    def __init__(self, market_meta_client: MarketMetaClient, *, adapter: Any | None=None, settle_poll_seconds: int=5, redeem_idle_poll_seconds: int=300, redeem_fast_poll_seconds: int=5, redemption_tracker: RedemptionTracker | None=None, redemption_confirmer: RedemptionConfirmer | None=None) -> None:
        ...

    def register_pending(self, strategy_name: str, tracker: PositionTracker) -> None:
        ...

    def check_pending(self, current_window_slug: str, trackers: dict[str, PositionTracker]) -> list[tuple[str, SettlementResult]]:
        ...

    def confirm_redemptions(self, *, force: bool=False) -> list[ConfirmationEvent]:
        """Delegate auto-redeemer detection to the confirmer."""
        ...

    def poll_redemptions(self, force: bool=False) -> list[dict[str, Any]]:
        ...
