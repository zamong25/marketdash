"""Adverse selection effect."""

class AdverseSelectionEffect:
    name: ClassVar[str]

    def __init__(self, samples: list[float] | None=None, seed: int=42) -> None:
        ...

    @classmethod
    def from_path(cls, path: str | Path, seed: int=42) -> 'AdverseSelectionEffect':
        ...

    @classmethod
    def from_payload(cls, payload: dict[str, Any], seed: int=42) -> 'AdverseSelectionEffect':
        ...

    def apply(self, context: 'FillContext', book: 'BookProvider') -> 'FillContext':
        ...
