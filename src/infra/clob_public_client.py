
class ClobPublicClient:
    """Small read-only wrapper for public CLOB market-data endpoints."""

    def __init__(self, base_url: str='https://clob.venue.com', timeout_seconds: float=8.0, user_agent: str='venue-btc-rnd/public-clob/1.0') -> None:
        ...

    def get_order_books(self, token_ids: list[str]) -> list[dict[str, Any]]:
        ...
