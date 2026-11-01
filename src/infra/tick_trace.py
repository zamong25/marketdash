
class TickTraceWriter:
    """Append-only trace of runner ticks actually processed live."""

    def __init__(self, path: str | Path) -> None:
        ...

    def write(self, payload: dict[str, Any]) -> None:
        ...

def load_tick_trace_schedule(path: str | Path, *, days: Iterable[str] | None=None, runner: str | None=None) -> dict[str, tuple[int, ...]]:
    """Load a live-observed cadence schedule from a tick-trace JSONL file."""
    ...
