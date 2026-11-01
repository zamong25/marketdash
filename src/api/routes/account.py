"""``/account`` — read-only account-state display contract."""

@router.get('/state')
def get_account_state() -> dict:
    """Return sanitized account-state status without exchange connectivity."""
    ...

@router.get('/live-readiness')
def get_account_live_readiness() -> dict:
    """Return strict live-readiness gates without exchange connectivity."""
    ...
