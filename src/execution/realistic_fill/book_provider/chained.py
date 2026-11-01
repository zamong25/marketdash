"""Composable book provider chain."""

class ChainedBookProvider(BookProvider):

    def __init__(self, providers: Sequence[tuple[str, BookProvider]]) -> None:
        ...

    def book_at(self, window_slug: str, token_id: str, ts_ms: int) -> BookSnapshot | None:
        ...
