"""V1 CLOB adapter — wraps ``venue-sdk`` 0.34.6."""

def _patch_venue-sdk_timeout() -> None:
    """Replace venue-sdk's shared httpx client. Idempotent."""
    ...

def _extract_filled_shares(result: Any) -> float | None:
    ...

def _response_error(result: Any) -> str:
    """Classify an HTTP-200 matcher rejection without discarding its body."""
    ...

class V1CLOBAdapter:
    """Concrete V1 CLOBClient. Lazily builds the underlying ClobClient."""

    def __init__(self) -> None:
        ...

    @property
    def version(self) -> str:
        ...

    def _build_client(self):
        ...

    @property
    def client(self):
        ...

    def get_balance(self) -> float:
        ...

    def get_token_balance(self, token_id: str) -> float:
        ...

    def place_order(self, request: OrderRequest) -> OrderResult:
        ...

    def _place_limit(self, request: OrderRequest) -> OrderResult:
        ...

    def _place_market(self, request: OrderRequest) -> OrderResult:
        """Match the legacy adapter's FAK + limit-fallback path."""
        ...

    def cancel_order(self, order_id: str) -> bool:
        ...

    def get_order(self, order_id: str) -> Any:
        ...

    def cancel_all(self) -> bool:
        ...

    def get_open_orders(self, token_id: str | None=None) -> list[Any]:
        ...

    def get_tick_size(self, token_id: str) -> float:
        ...

    def get_order_book(self, token_id: str) -> OrderBook | None:
        ...
