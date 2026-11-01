"""Fill the per-token SDK caches before the order path needs them."""

@dataclass(frozen=True)
class WarmResult:
    """What the warm actually achieved, per token, with the failures kept."""
    requested: int
    warmed: int
    failed: int
    elapsed_ms: float
    errors: tuple[tuple[str, str, str], ...]

    @property
    def ok(self) -> bool:
        """True only when every requested token warmed completely."""
        ...

    def as_dict(self) -> dict[str, Any]:
        """A flat row for a JSONL ledger (the mirror logs it as ``prewarm``)."""
        ...

def resolve_warm_target(client: Any) -> Any | None:
    """The object that actually carries the warm calls, or None."""
    ...

def warm_tokens(client: Any, token_ids: Iterable[str]) -> WarmResult:
    """Pre-call ``get_tick_size`` + ``get_multi_outcome`` for each token id."""
    ...
