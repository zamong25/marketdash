"""Shared helpers used by both :class:`Runner` and :class:`TwinRunner`."""

class _EmojiMap:
    """dict-like view of strategy emojis sourced from the registry."""

    def get(self, key: str, default: str='') -> str:
        ...

    def __getitem__(self, key: str) -> str:
        ...

    def __contains__(self, key: str) -> bool:
        ...

@dataclass(frozen=True)
class DailyStatsSummary:
    """Aggregate output of :func:`aggregate_daily_stats`."""
    wins: int
    losses: int
    daily_pnl: float
    daily_trades: int

def record_mode(rec: dict) -> str:
    """Classify a trade record as ``"paper"``, ``"live"``, or ``"unknown"``."""
    ...

def today_log_path(log_root: Path, strategy_name: str) -> Path:
    """Return the JSONL trade-log path for ``strategy_name`` on today's UTC date."""
    ...

def read_today_records(log_root: Path, strategy_name: str, *, filter_mode: str | None=None) -> list[dict]:
    """Read today's trade log for a single strategy, optionally filtering"""
    ...

def aggregate_daily_stats(records: list[dict]) -> DailyStatsSummary:
    """Aggregate per-window PnL from settlement + redemption records."""
    ...

def find_orphaned_open_position(records: list[dict], *, default_token_prefix: str='paper') -> tuple[TrackedPosition, str] | None:
    """Scan mode-filtered records for the most recent entry that never"""
    ...
