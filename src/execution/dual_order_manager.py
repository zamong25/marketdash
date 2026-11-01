"""Fan-out layer that routes a single Signal to paper + live executors."""

class DualOrderManager:
    """Dispatch one Signal to a paper + live ``OrderManager`` pair."""

    def __init__(self, *, paper_manager: OrderManager, live_manager: OrderManager) -> None:
        ...

    def process_signal(self, strategy_name: str, signal: Signal, snapshot: MarketSnapshot, paper_tracker: PositionTracker, live_tracker: PositionTracker, *, paper_params: dict[str, Any], live_params: dict[str, Any], paper_config_version: str, live_config_version: str, use_fast_path: bool, balance_cache: BalanceCache | None) -> tuple[OrderDecision, OrderDecision]:
        """Fan the signal out to paper and live, returning both decisions."""
        ...

    def _process_one_side(self, manager: OrderManager, *, strategy_name: str, signal: Signal, snapshot: MarketSnapshot, tracker: PositionTracker, params: dict[str, Any], config_version: str, use_fast_path: bool, balance_cache: BalanceCache | None, paper_mode: str) -> OrderDecision:
        ...
