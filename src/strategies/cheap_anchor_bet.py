"""Cheap Anchor Bet — buy the under-priced side in the scan window."""

@register_strategy(name='cheap_anchor_bet', emoji='🏷️')
class CheapAnchorBetStrategy:
    """Buy the cheap side when it sits inside the anchoring sweet spot."""

    def __init__(self) -> None:
        ...

    def init(self, params: dict[str, Any]) -> None:
        ...

    def warmup_ticks(self) -> int:
        ...

    def on_tick(self, snapshot: MarketSnapshot, history: list[MarketSnapshot], portfolio: PortfolioState) -> Signal | None:
        ...

    def _resolve_cheap_side(self, snapshot: MarketSnapshot) -> SignalDirection | None:
        """Return SignalDirection of the side currently priced lowest."""
        ...

    def _confidence(self, entry_price: float) -> float:
        """Scale confidence so cheaper bets report higher confidence —"""
        ...

    def _build_order_info(self, snapshot: MarketSnapshot, direction: SignalDirection, entry_price: float) -> dict[str, Any]:
        ...
