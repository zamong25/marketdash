"""Market-pin signal follower for reviewed, paper-only research drafts."""

@register_strategy(name='market_pin_signal_follow', capabilities=('up_price', 'best_bid', 'best_ask', 'bid_size', 'ask_size'), emoji='🧭')
class MarketPinSignalFollowStrategy:
    """Follow an explicitly reviewed pre-resolution market-pin signal."""

    def __init__(self) -> None:
        ...

    def init(self, params: dict[str, Any]) -> None:
        ...

    def warmup_ticks(self) -> int:
        ...

    def on_tick(self, snapshot: MarketSnapshot, history: list[MarketSnapshot], portfolio: PortfolioState) -> Signal | None:
        ...

    def explain_no_signal(self, snapshot: MarketSnapshot, history: list[MarketSnapshot], portfolio: PortfolioState) -> dict[str, Any]:
        ...

    def _evaluate(self, snapshot: MarketSnapshot, portfolio: PortfolioState) -> dict[str, Any]:
        ...

    def _window_allowed(self, window_slug: str) -> bool:
        ...

    def _control_blocker(self) -> str:
        ...

    def _confidence(self, entry_price: float) -> float:
        ...

def _parse_direction(value: Any) -> SignalDirection | None:
    ...

def _blocked(reason: str, *, direction: SignalDirection | None=None) -> dict[str, Any]:
    ...
