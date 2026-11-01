"""``/research`` — read-only project research-memory surfaces."""

@router.get('/memory')
def get_research_memory() -> dict:
    """Return a local index of docs/analysis research artifacts."""
    ...

@router.get('/platform-checklist')
def get_platform_completion_checklist() -> dict:
    """Return a strict read-only platform goal completion checklist."""
    ...

@router.get('/search')
def get_research_search(q: str='') -> dict:
    """Return local full-text search results over research artifacts."""
    ...
