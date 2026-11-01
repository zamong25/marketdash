"""Fit the ``market_impact.json`` coefficient."""

def _usable_records(records: Sequence[PairedFillRecord]) -> list[PairedFillRecord]:
    """Drop records missing the features the linear model needs."""
    ...

def _ols_slope_zero_intercept(xs: list[float], ys: list[float]) -> float:
    """Least-squares slope of ``y = alpha * x`` (no intercept)."""
    ...

def fit_market_impact(records: Sequence[PairedFillRecord], *, min_fills: int=50, generated_at_utc: str | None=None) -> dict:
    """Fit ``alpha`` in ``shift = alpha * (shares / ask_depth_top1)``."""
    ...
