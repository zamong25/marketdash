"""Execution-owned trust filters for trade-log calibration inputs."""

def is_realistic_paper_buy(record: dict) -> bool:
    """Return whether a paper buy came from the realistic-fill executor."""
    ...

def is_trusted_live_buy(record: dict, strict: bool=True) -> bool:
    """Return whether a live buy has ground-truth cost accounting."""
    ...

def is_clean_record(record: dict, strict: bool=True) -> bool:
    """Return whether a trade-log record is safe for aggregate analysis."""
    ...
