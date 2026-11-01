"""Execution-owned inputs shared by realistic fill and research replay."""

def _window_start_ts(window_slug: str) -> int:
    ...

def _touch_index(prices: list[float], *, want_max: bool) -> int | None:
    """Index of the best level, so no caller has to know the ladder's order."""
    ...

def _as_float_list(value: object) -> list[float]:
    ...

@dataclass(frozen=True)
class BookSnapshot:
    """Ladders are sorted best-first, but the accessors do not rely on it (C81)."""
    ts_ms: int
    token_id: str
    ask_prices: list[float]
    ask_sizes: list[float]
    bid_prices: list[float]
    bid_sizes: list[float]

    @property
    def best_ask(self) -> float | None:
        ...

    @property
    def best_ask_size(self) -> float:
        ...

    @property
    def best_bid(self) -> float | None:
        ...

class PmEventsBook:
    """Lazy, per-window cache over processed depth parquet files."""

    def __init__(self, events_root: str | Path):
        ...

    @property
    def root(self) -> Path:
        ...

    def _candidate_dirs(self, window_slug: str) -> list[Path]:
        ...

    def _load_window(self, window_slug: str) -> dict[str, list[BookSnapshot]]:
        ...

    def book_at(self, window_slug: str, token_id: str, ts_ms: int) -> BookSnapshot | None:
        ...

    def tokens_for_window(self, window_slug: str) -> list[str]:
        ...

class TokenMapper:
    """Map ``(window_slug, direction)`` to a pm_events token id."""

    def __init__(self, book: PmEventsBook):
        ...

    def resolve(self, window_slug: str, signal_ts_ms: int, up_price: float, down_price: float) -> dict[str, str]:
        ...

class LatencyModel:
    """Empirical latency distribution; samples with replacement."""

    def __init__(self, samples_ms: list[float], seed: int=42):
        ...

    @classmethod
    def from_live_log(cls, path: str | Path, stage: str=FAST_PATH_STAGE, seed: int=42) -> LatencyModel:
        ...

    @property
    def samples(self) -> list[float]:
        ...

    @property
    def seed(self) -> int:
        ...

    def sample(self) -> float:
        ...

    def median(self) -> float:
        ...

    def percentile(self, p: float) -> float:
        ...
