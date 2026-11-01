"""Single-process paper/live twin runner."""

@dataclass
class TwinStrategyRuntime:
    """Per-twin mutable state: one strategy instance + two trackers."""
    config: TwinInstanceConfig
    strategy: Strategy
    paper_tracker: PositionTracker
    live_tracker: PositionTracker
    paper_config_version: str
    live_config_version: str
    use_fast_path: bool

class TwinRunner:
    """Tick-driven runner that serves every twin pair in one process."""

    def __init__(self, config: AppConfig, *, dual_order_manager: DualOrderManager, paper_notifier: TelegramNotifier | None=None, live_notifier: TelegramNotifier | None=None, paper_heartbeat_path: str | Path | None=None, live_heartbeat_path: str | Path | None=None, tick_trace_path: str | Path | None=None, decision_audit_path: str | Path | None=None) -> None:
        ...

    def _build_runtimes(self) -> list[TwinStrategyRuntime]:
        ...

    def _start_balance_cache_if_needed(self) -> None:
        ...

    def shutdown(self) -> None:
        ...

    def _track_balance_cache_tokens(self) -> None:
        ...

    def read_snapshot(self) -> MarketSnapshot | None:
        ...

    def _today_log_path(self, strategy_name: str) -> Path:
        ...

    def _log_names_for(self, runtime: TwinStrategyRuntime, mode: str) -> list[str]:
        """Return the list of strategy-log directory names to read for one"""
        ...

    def _read_today_records(self, runtime: TwinStrategyRuntime, mode: str) -> list[dict]:
        """Read today's mode-filtered records from every log alias for the twin."""
        ...

    def _restore_daily_stats(self) -> None:
        ...

    def _restore_open_positions(self) -> None:
        """Re-attach paper_buy/live_buy entries with no matching settlement,"""
        ...

    def _mode_trackers(self, mode: str) -> dict[str, PositionTracker]:
        ...

    def _runtime_for(self, strategy_name: str) -> TwinStrategyRuntime | None:
        ...

    def _emit_redemption_completed_records(self, mode: str) -> None:
        ...

    def _emit_redemption_confirmation_records(self, mode: str) -> None:
        """Auto-redeemer path — only meaningful for the live manager."""
        ...

    def _check_settlements(self, snapshot: MarketSnapshot, mode: str) -> list[tuple[str, Any]]:
        ...

    def _notify_settlement(self, mode: str, strategy_name: str, result: Any) -> None:
        ...

    def _handle_settlements(self, snapshot: MarketSnapshot) -> None:
        ...

    def _signal_portfolio(self, runtime: TwinStrategyRuntime) -> PortfolioState:
        """Return the ``PortfolioState`` passed into ``strategy.on_tick``."""
        ...

    @staticmethod
    def _tracker_state(tracker: PositionTracker) -> dict[str, float | int | bool]:
        ...

    def _runtime_state(self, runtime: TwinStrategyRuntime) -> dict[str, dict[str, float | int | bool]]:
        ...

    def _write_decision_audit(self, *, snapshot: MarketSnapshot, runtime: TwinStrategyRuntime, status: str, reason: str, state_before: dict[str, dict[str, float | int | bool]], signal: Signal | None=None, paper_decision=None, live_decision=None, diagnostic: dict[str, object] | None=None) -> None:
        ...

    @staticmethod
    def _strategy_no_signal_diagnostic(*, runtime: TwinStrategyRuntime, snapshot: MarketSnapshot, history: list[MarketSnapshot], portfolio: PortfolioState) -> dict[str, object] | None:
        ...

    def _notify_entry(self, runtime: TwinStrategyRuntime, signal, snapshot: MarketSnapshot, *, mode: str) -> None:
        ...

    def run_once(self) -> bool:
        """Advance one tick. Returns ``True`` when a snapshot was processed."""
        ...

    def _write_heartbeats(self, snapshot: MarketSnapshot) -> None:
        ...

    def run_forever(self) -> None:
        ...
