"""``/risk`` — read-only execution posture and safety surface."""

@router.get('/status')
def get_risk_status() -> dict:
    """Return static risk posture without exposing secret values."""
    ...
