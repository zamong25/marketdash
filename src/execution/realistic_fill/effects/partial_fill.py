"""Partial fill effect."""

class PartialFillEffect:
    name: ClassVar[str]

    def __init__(self, calibration_path: str | Path | None=None, *, seed: int=42, allow_zero_fill_ratio: bool=True) -> None:
        ...

    def apply(self, context: 'FillContext', book: 'BookProvider') -> 'FillContext':
        ...

    def _drop_zero_ratio_samples(self) -> None:
        """Remove explicit zero-fill draws from the loaded calibration."""
        ...

    def _select_samples(self, price_bucket: str | None, depth_bucket: str | None, remaining_bucket: str | None, *, book_context: str | None=None) -> tuple[float, ...]:
        ...

def _sanitize_samples(values: list[float] | tuple[float, ...]) -> tuple[float, ...]:
    ...

def _normalize_book_context(raw: object) -> str | None:
    ...

def _coalesce_price(*values: float | None) -> float | None:
    ...

def _bucket_label(value: float | None, edges: tuple[float, ...], labels: tuple[str, ...]) -> str | None:
    ...

def _partial_fill_depth_multiple(snap, requested_shares: float) -> float:
    ...
