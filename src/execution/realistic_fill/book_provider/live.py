"""Live book provider — reads ``data/raw/pm_events/live_book.json`` for"""

class LiveBookProvider(BookProvider):

    def __init__(self, live_book_path: str | Path, *, stale_threshold_s: float=DEFAULT_STALE_THRESHOLD_S, now_ms_fn=None, logger: logging.Logger | None=None) -> None:
        ...

    def book_at(self, window_slug: str, token_id: str, ts_ms: int) -> BookSnapshot | None:
        ...

    def _read_current(self) -> dict | None:
        ...

    def _maybe_warn(self, message: str, throttle_s: float=60.0) -> None:
        ...

def _as_float_list(value: object) -> list[float]:
    ...
