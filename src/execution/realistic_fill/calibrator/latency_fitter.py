"""Fit realistic-fill latency from the *order-submit* clock."""

def _coerce_positive_ms(value: object) -> float | None:
    ...

def extract_live_fill_latencies(log_paths: Sequence[Path], *, strict: bool=True) -> list[float]:
    """Pull the per-fill ``latency_ms`` values from live trade logs."""
    ...

def extract_order_submit_latencies(log_paths: Sequence[Path], *, stage: str=DEFAULT_FAST_SUBMIT_STAGE, success_only: bool=True) -> list[float]:
    """Extract signal→submit wall times from ``logs/run_live/latency.jsonl``."""
    ...

def fit_latency_calibration(samples: Sequence[float], *, min_fills: int=30, source_label: str=f'logs/run_live/latency.jsonl:{DEFAULT_FAST_SUBMIT_STAGE}.total_elapsed_ms', generated_at_utc: str | None=None) -> dict:
    """Build a JSON-ready calibration dict from raw latency samples."""
    ...

def write_calibration_file(payload: dict, path: Path, *, dry_run: bool=False) -> Path | None:
    """Persist the calibration payload to ``path`` as JSON."""
    ...
