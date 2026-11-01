"""Post-fill retry-threshold effect."""

class RetryThresholdEffect:
    name: ClassVar[str]

    def apply(self, context: 'FillContext', book: 'BookProvider') -> 'FillContext':
        ...
