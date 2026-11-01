"""``/runtime/status`` — current runtime snapshot built from heartbeat files."""

def _read_heartbeat(path: Path) -> dict | None:
    ...

def _is_fresh(hb: dict | None) -> bool:
    ...

def _last_jsonl_line(path: Path) -> dict | None:
    ...

@router.get('/status')
def get_status() -> dict:
    """Aggregate runtime status."""
    ...
