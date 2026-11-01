"""Single-strategy paper runner (non-twin)."""

def _build_realistic_fill(config) -> tuple[FillModel | None, LiveBookProvider | None]:
    """Construct the realistic-mode dependencies if any paper strategy"""
    ...

def _parse_args() -> argparse.Namespace:
    """Optional --config lets one runner instance target a trimmed-down"""
    ...

def _positive_int(value: str) -> int:
    ...

def _run_runner(runner: Runner, *, max_ticks: int | None, interval_seconds: int) -> None:
    ...

def _preflight_latest_snapshot(root: Path) -> None:
    ...

def main() -> None:
    ...
