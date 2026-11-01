"""``/portfolio`` — read-only account/PnL provenance surface."""

@router.get('/status')
def get_portfolio_status() -> dict:
    """Return log-derived portfolio status without touching exchange APIs."""
    ...
