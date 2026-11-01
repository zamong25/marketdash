
class PythHermesError(RuntimeError):
    """Raised when a public Pyth Hermes request fails."""

class PythHermesClient:
    """Small read-only wrapper for public Pyth Hermes price endpoints."""

    def __init__(self, *, base_url: str=PYTH_HERMES_BASE_URL, timeout_s: float=10.0, session: requests.Session | None=None) -> None:
        ...

    def price_feeds(self, query: str) -> list[dict[str, Any]]:
        ...

    def latest_price(self, feed_ids: Sequence[str]) -> dict[str, Any]:
        ...

    def _get_json(self, path: str, params: dict[str, Any] | list[tuple[str, str]]) -> Any:
        ...
