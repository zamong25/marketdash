"""Book walk effect."""

class BookWalkEffect:
    name: ClassVar[str]

    def apply(self, context: 'FillContext', book: 'BookProvider') -> 'FillContext':
        ...

def _walk(prices: list[float], sizes: list[float], shares: float) -> tuple[float | None, float]:
    ...
