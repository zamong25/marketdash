"""Paper-only adapter for reviewed hypothesis replay research."""

@register_strategy(name='hypothesis_replay_research', capabilities=('up_price', 'best_bid', 'best_ask', 'bid_size', 'ask_size'), emoji='🔬')
class HypothesisReplayResearchStrategy:
    """Trade only explicitly reviewed hypothesis replay configs in paper mode."""

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

    def _replay_metric_blocker(self) -> str:
        ...

    def _observed_replay_event_count(self) -> int:
        ...

    def _confidence(self, entry_price: float) -> float:
        ...

def _parse_direction(value: Any) -> SignalDirection | None:
    ...

def _blocked(reason: str, *, direction: SignalDirection | None=None) -> dict[str, Any]:
    ...
