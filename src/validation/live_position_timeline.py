"""Build live-observed position intervals for sim-vs-live validation."""

def _window_start_ts(slug: str) -> int:
    ...

def _parse_logged_at_ts_s(value: object) -> int | None:
    ...

def _iter_rows(paths: Iterable[Path]) -> Iterable[dict[str, object]]:
    ...

def build_live_position_intervals(trade_log_paths: Iterable[Path], *, fallback_settlement_delay_s: int=300, day_start_ts_s: int | None=None, day_end_ts_s: int | None=None) -> tuple[ExternalPositionInterval, ...]:
    """Return live-observed position intervals from trade logs."""
    ...
