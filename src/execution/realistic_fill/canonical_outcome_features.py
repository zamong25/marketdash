"""Shared feature bucketing for canonical-outcome calibration/effects."""

def ask_delta_bucket(delta: float, edges: tuple[float, float, float]=DEFAULT_ASK_DELTA_EDGES) -> str:
    ...

def ask_delta_is_eligible(delta: float, bounds: tuple[float, float] | None=DEFAULT_ASK_DELTA_ELIGIBILITY_BOUNDS) -> bool:
    """Return True when ``delta`` lies inside the calibrated runtime band."""
    ...
