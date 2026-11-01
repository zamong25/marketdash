"""Execution over the tunnel: the same Protocol, a different pair of hands."""

def _order_payload(request: OrderRequest) -> dict[str, Any]:
    ...

def _result_from_payload(raw: Any) -> OrderResult:
    ...

class RemoteExecAdapter:
    """CLOBClient whose execution surface is an HTTP call to the edge gateway."""

    def __init__(self, base_url: str | None=None, *, client_name: str | None=None, timeout_s: float | None=None, book_client: Any | None=None, http_client: Any | None=None, auth_token: str | None=None, kill_switch_path: Path | str | None=None) -> None:
        ...

    @property
    def version(self) -> str:
        """``"edge"`` -- deliberately not ``"v2"``."""
        ...

    @property
    def http(self) -> Any:
        ...

    def close(self) -> None:
        ...

    def _tags(self, intent_id: str | None=None) -> dict[str, str]:
        ...

    def _headers(self) -> dict[str, str] | None:
        ...

    def refuse_if_killed(self, what: str) -> None:
        """Stop a placement HERE if the Mac's kill file exists."""
        ...

    def _raise_for_body(self, response: Any, what: str) -> None:
        ...

    def _request(self, method: str, path: str, *, json_body: dict[str, Any] | None=None, params: dict[str, Any] | None=None, what: str, unknown_outcome: bool=False) -> Any:
        ...

    def get_balance(self) -> float:
        ...

    def get_token_balance(self, token_id: str) -> float:
        ...

    def place_order(self, request: OrderRequest) -> OrderResult:
        ...

    def place_orders(self, requests: Sequence[OrderRequest]) -> list[OrderResult]:
        """Batch placement, in the order given, post_only flags intact."""
        ...

    def get_order(self, order_id: str) -> Any:
        ...

    def cancel_order(self, order_id: str) -> bool:
        ...

    def cancel_all(self) -> bool:
        ...

    def get_open_orders(self, token_id: str | None=None) -> list[Any]:
        """RAISES on a failed read. Yes, even here."""
        ...

    def get_open_orders_strict(self, token_id: str | None=None) -> list[Any]:
        ...

    def get_order_book(self, token_id: str) -> OrderBook | None:
        ...

    def prewarm(self, token_ids: Sequence[str]) -> dict[str, Any]:
        """Ask the gateway to warm its SDK caches for a window's tokens."""
        ...

    def healthz(self) -> dict[str, Any]:
        ...
