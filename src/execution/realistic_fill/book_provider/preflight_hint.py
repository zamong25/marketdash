"""Book provider backed by live preflight book observations."""

@dataclass(frozen=True)
class PreflightBookHint:
    window_slug: str
    token_hint: str
    ts_ms: int
    ask_price: float
    ask_depth: float

class PreflightHintBookProvider(BookProvider):

    def __init__(self, hints: Sequence[PreflightBookHint], *, max_age_ms: int=10000) -> None:
        ...

    @classmethod
    def from_trade_logs(cls, paths: Iterable[str | Path], *, max_age_ms: int=10000) -> 'PreflightHintBookProvider':
        ...

    def book_at(self, window_slug: str, token_id: str, ts_ms: int) -> BookSnapshot | None:
        ...

def _hint_from_trade_row(raw: dict) -> PreflightBookHint | None:
    ...

def _token_matches_hint(token_id: str, token_hint: str) -> bool:
    ...
