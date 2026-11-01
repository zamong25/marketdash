"""Fit the post-send slippage distribution."""

def _usable_records(records: Sequence[PairedFillRecord], *, max_snapshot_ask_gap: float) -> list[PairedFillRecord]:
    """Drop records missing the features or tainted by MultiOutcome inversion."""
    ...

def _shift_for(record: PairedFillRecord) -> float:
    """Compute the nonnegative slippage shift from a clean record."""
    ...

def fit_post_send_slippage(records: Sequence[PairedFillRecord], *, min_fills: int=50, max_snapshot_ask_gap: float=0.05, generated_at_utc: str | None=None) -> dict:
    """Fit an empirical zero-inflated distribution of post-send shifts."""
    ...
