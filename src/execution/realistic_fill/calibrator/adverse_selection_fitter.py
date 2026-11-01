"""Rebuild ``adverse_selection.json`` from a list of PairedFillRecords."""

def _summary_for_horizon(shifts: list[float]) -> dict:
    """Descriptive stats matching the existing JSON schema field names."""
    ...

def _shift_for_horizon(record: PairedFillRecord, horizon_s: int) -> float | None:
    """Extract the ``max(0, fill - future_mid)`` for the given horizon"""
    ...

def fit_adverse_selection(records: Sequence[PairedFillRecord], *, horizons_s: Sequence[int]=_DEFAULT_HORIZONS_S, selected_horizon_s: int=5, generated_at_utc: str | None=None) -> dict:
    """Build a calibration dict ready to ``json.dumps`` to disk."""
    ...
