
@dataclass
class StrategyRuntime:
    config: StrategyInstanceConfig
    strategy: Strategy
    tracker: PositionTracker
    config_version: str
    use_fast_path: bool

class Runner:

    def __init__(self, config: AppConfig, *, order_manager: OrderManager, notifier: TelegramNotifier | None=None, heartbeat_path: str | Path | None=None, tick_trace_path: str | Path | None=None, decision_audit_path: str | Path | None=None) -> None:
        ...

    def _build_runtimes(self) -> list[StrategyRuntime]:
        ...

    def _start_balance_cache_if_needed(self) -> None:
        ...

    def shutdown(self) -> None:
        ...

    def _track_balance_cache_tokens(self) -> None:
        ...

    def read_snapshot(self) -> MarketSnapshot | None:
        ...

    def _trackers(self) -> dict[str, PositionTracker]:
        ...

    @staticmethod
    def _tracker_state(tracker: PositionTracker) -> dict[str, float | int | bool]:
        ...

    def _write_decision_audit(self, *, snapshot: MarketSnapshot, runtime: StrategyRuntime, status: str, reason: str, state_before: dict[str, float | int | bool], signal=None, accepted: bool | None=None, diagnostic: dict[str, object] | None=None) -> None:
        ...

    @staticmethod
    def _strategy_no_signal_diagnostic(*, runtime: StrategyRuntime, snapshot: MarketSnapshot, history: list[MarketSnapshot]) -> dict[str, object] | None:
        ...

    def _emit_redemption_confirmation_records(self) -> None:
        """For each auto-redeemer-observed transition this tick, append a"""
        ...

    def _emit_redemption_completed_records(self) -> None:
        """For each redemption that just reached a terminal state"""
        ...

    def _today_log_path(self, strategy_name: str) -> Path:
        ...

    def _read_today_records(self, strategy_name: str, filter_mode: str | None=None) -> list[dict]:
        ...

    def _restore_daily_stats(self) -> None:
        ...

    def _restore_open_positions(self) -> None:
        """Re-attach any paper_buy/live_buy that has no matching settlement yet."""
        ...

    def run_once(self) -> bool:
        ...

    def run_forever(self) -> None:
        ...
