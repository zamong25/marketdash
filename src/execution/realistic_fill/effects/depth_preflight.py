"""Depth preflight — mirrors live's first-attempt ask-depth gate."""

class DepthPreflightEffect:
    name: ClassVar[str]

    def apply(self, context: 'FillContext', book: 'BookProvider') -> 'FillContext':
        ...
