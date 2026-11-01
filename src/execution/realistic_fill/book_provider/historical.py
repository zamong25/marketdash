"""Historical book provider for realistic replay / simulation."""

@dataclass(frozen=True)
class _RepairedBook:
    """A snapshot's ladders after the phantom crossed levels are matched off."""
    ts_ms: int
    token_id: str
    ask_prices: list[float]
    ask_sizes: list[float]
    bid_prices: list[float]
    bid_sizes: list[float]
    was_crossed: bool

def _uncross(snap) -> _RepairedBook:
    """Auction-uncross one token's ladder, mirroring ``session_cube.clean.uncross``."""
    ...

@dataclass(frozen=True)
class _BookCandidate:
    snap: Any
    age_ms: int

class HistoricalBookProvider(BookProvider):

    def __init__(self, processed_depth_root: str | Path, raw_depth_root: str | Path | None=None, *, processed_freshness_ms: int=5000, max_snapshot_age_ms: int=30000, min_complement_ask_sum: float=0.95, max_complement_bid_sum: float=1.05) -> None:
        ...

    @staticmethod
    def _wrap(snap) -> BookSnapshot | None:
        ...

    @staticmethod
    def _best_bid(snap) -> float | None:
        ...

    @classmethod
    def _repair(cls, snap) -> _RepairedBook | None:
        """Uncross ``snap``; ``None`` when nothing tradeable survives the repair."""
        ...

    @staticmethod
    def _age_ms(snap, ts_ms: int) -> int:
        ...

    def _candidate(self, snap, ts_ms: int) -> _BookCandidate | None:
        ...

    @staticmethod
    def _other_token_ids(book: PmEventsBook, window_slug: str, token_id: str) -> list[str]:
        ...

    def _sibling_candidates(self, window_slug: str, token_id: str, ts_ms: int) -> list[_BookCandidate]:
        ...

    def _passes_complement_sanity(self, candidate: _BookCandidate, siblings: list[_BookCandidate]) -> bool:
        ...

    def book_at(self, window_slug: str, token_id: str, ts_ms: int) -> BookSnapshot | None:
        ...
