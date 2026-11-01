"""Shared helper features for partial-fill calibration/runtime."""

def _positive_finite(value: float | int | None) -> float | None:
    ...

def topn_ask_depth(ask_sizes: Iterable[float] | None, *, n: int=PARTIAL_FILL_TOPN_LEVELS) -> float | None:
    ...

def blended_partial_fill_depth_proxy(*, top1_depth: float | None, top5_depth: float | None) -> float | None:
    """Blend immediate and shallow near-book liquidity into one proxy."""
    ...

def blended_partial_fill_depth_multiple(ask_sizes: Iterable[float] | None, requested_shares: float) -> float:
    ...
