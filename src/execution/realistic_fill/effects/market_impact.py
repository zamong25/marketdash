"""Market impact effect."""

@dataclass
class MarketImpactEffect:
    name: ClassVar[str]
    alpha: float

    @classmethod
    def from_path(cls, path: str | Path) -> 'MarketImpactEffect':
        ...

    @classmethod
    def from_payload(cls, payload: dict[str, Any]) -> 'MarketImpactEffect':
        ...

    def apply(self, context: 'FillContext', book: 'BookProvider') -> 'FillContext':
        ...
