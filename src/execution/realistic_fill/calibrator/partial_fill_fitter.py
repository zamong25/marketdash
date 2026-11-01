"""Fit the ``partial_fill.json`` fill-ratio distribution."""

@dataclass(frozen=True)
class _FillRatioSample:
    entry_price: float
    depth_multiple: float
    fill_ratio: float
    requested_shares: float
    cost_source: str
    book_context: str | None
    rejection_reason: str | None

def _normalize_book_context(raw: object) -> str | None:
    ...

def _entry_price(record: PairedFillRecord) -> float | None:
    ...

def _usable_filled_samples(records: Sequence[PairedFillRecord]) -> tuple[list[_FillRatioSample], int]:
    ...

def _usable_zero_fill_rejection_samples(records: Sequence[PairedFillRecord], *, zero_fill_reasons: tuple[str, ...]) -> tuple[list[_FillRatioSample], int]:
    ...

def _default_edges(values: list[float], *, low: float, high: float | None=None) -> list[float]:
    ...

def _bucket_label(value: float, *, edges: tuple[float, ...], labels: tuple[str, ...]) -> str | None:
    ...

def fit_partial_fill(filled_records: Sequence[PairedFillRecord], rejected_records: Sequence[PairedFillRecord]=(), *, min_samples: int=50, cell_min_samples: int=3, zero_fill_reasons: tuple[str, ...]=_ZERO_FILL_REASONS_DEFAULT, include_book_context: bool=False, price_bucket_edges: tuple[float, float, float, float] | None=None, depth_multiple_edges: tuple[float, float, float, float] | None=None, signal_remaining_edges: tuple[int, int]=DEFAULT_SIGNAL_REMAINING_EDGES, generated_at_utc: str | None=None) -> dict:
    """Fit a bucketed empirical fill-ratio distribution."""
    ...
