"""Fit the ``api_error.json`` bucketed API rejection risk table."""

def _quantile_edges(values: list[float]) -> tuple[float, float]:
    ...

def _requested_shares_edges(values: list[float]) -> tuple[float, float]:
    """Choose discrete-aware edges for requested-share buckets."""
    ...

def _bucket_three_way(value: float, edges: tuple[float, float], labels: tuple[str, str, str]) -> str:
    ...

def _record_budget_anchor(record: PairedFillRecord) -> float | None:
    ...

def _record_reason_kind(record: PairedFillRecord) -> str:
    ...

def _result_reason_for_kind(kind: str) -> str:
    ...

def _uses_reasoned_adapter_schema(modeled_rejection_reasons: tuple[str, ...]) -> bool:
    ...

def _bucket_for(signal_remaining_s: int, spread: float, *, signal_remaining_edges: tuple[int, int], spread_edges: tuple[float, float], book_context: str | None=None) -> str:
    ...

def _record_feature(record: PairedFillRecord) -> tuple[int, float] | None:
    """Extract ``(signal_remaining_s, snapshot_spread)`` from a record."""
    ...

def _bucket_key_for_record(records: Sequence[PairedFillRecord], *, signal_remaining_edges: tuple[int, int], spread_edges: tuple[float, float], include_book_context: bool) -> tuple[list[str], dict[str, int]]:
    """Resolve trustworthy regime features and return skip diagnostics."""
    ...

def _reasoned_bucket_key_for_record(record: PairedFillRecord, *, signal_remaining_edges: tuple[int, int], spread_edges: tuple[float, float], requested_shares_edges: tuple[float, float], order_budget_edges: tuple[float, float], include_book_context: bool) -> str | None:
    ...

def _reasoned_parent_keys(key: str, *, include_book_context: bool) -> tuple[tuple[str, str], ...]:
    ...

def _fit_reasoned_adapter_schema(filled_records: Sequence[PairedFillRecord], rejected_records: Sequence[PairedFillRecord], *, signal_remaining_edges: tuple[int, int], spread_edges: tuple[float, float], min_total_per_bucket: int, modeled_rejection_reasons: tuple[str, ...], include_book_context: bool, generated_at_utc: str | None) -> dict:
    ...

def fit_api_error(filled_records: Sequence[PairedFillRecord], rejected_records: Sequence[PairedFillRecord], *, signal_remaining_edges: tuple[int, int]=DEFAULT_SIGNAL_REMAINING_EDGES, spread_edges: tuple[float, float]=DEFAULT_SPREAD_EDGES, min_total_per_bucket: int=20, modeled_rejection_reasons: tuple[str, ...]=_MODELED_REJECTION_REASONS_DEFAULT, include_book_context: bool=False, generated_at_utc: str | None=None) -> dict:
    """Fit ``p(reject | bucket)`` for each 2-axis bucket."""
    ...
