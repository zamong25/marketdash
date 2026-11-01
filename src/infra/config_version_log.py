"""Append-only log of strategy config versions, one jsonl line per change."""

def _diff_params(old: dict[str, Any] | None, new: dict[str, Any]) -> list[dict[str, Any]]:
    """Return a list of {key, before, after} diffs between two param dicts."""
    ...

class ConfigVersionLog:
    """Maintain a jsonl log of strategy config version transitions."""

    def __init__(self, log_path: str | Path) -> None:
        ...

    def _load_last_from_disk(self) -> None:
        ...

    def maybe_record(self, instance) -> str:
        """If the runtime config hash has changed since the last known record"""
        ...
