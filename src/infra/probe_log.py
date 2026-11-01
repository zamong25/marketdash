"""One shot-log for every live probe, so a logging fix lands once."""

class ProbeLog:
    """Append-only JSONL writer with the probe conventions baked in."""

    def __init__(self, path: Path | str, sym: str | None=None) -> None:
        ...

    def __call__(self, **kw: Any) -> None:
        ...

def order_id_of(resp: Any) -> str:
    """The venue order id from a post_order reply, or "" when there is none."""
    ...
