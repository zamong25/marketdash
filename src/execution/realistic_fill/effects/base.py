"""Effect protocol — a single step in the fill pipeline."""

class Effect(Protocol):
    name: ClassVar[str]

    def apply(self, context: 'FillContext', book: 'BookProvider') -> 'FillContext':
        ...
