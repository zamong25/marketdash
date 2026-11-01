
class TickDecisionAuditWriter:
    """Append-only per-tick decision audit trail."""

    def __init__(self, path: str | Path) -> None:
        ...

    def write(self, payload: dict[str, Any]) -> None:
        ...
