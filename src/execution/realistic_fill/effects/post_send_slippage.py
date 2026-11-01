"""Post-send slippage effect — models the matcher's submit-to-match drift."""

class PostSendSlippageEffect:
    name: ClassVar[str]

    def __init__(self, samples: list[float] | None=None, seed: int=42) -> None:
        ...

    @classmethod
    def from_path(cls, path: str | Path, seed: int=42) -> 'PostSendSlippageEffect':
        ...

    @classmethod
    def from_payload(cls, payload: dict[str, Any], seed: int=42) -> 'PostSendSlippageEffect':
        ...

    def apply(self, context: 'FillContext', book: 'BookProvider') -> 'FillContext':
        ...
