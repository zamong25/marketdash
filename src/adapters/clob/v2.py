"""V2 CLOB adapter — wraps ``venue-sdk-v2`` (vendored at ``vendor/venue-sdk-v2/``)."""

def _patch_v2_httpx_timeout() -> None:
    """Replace venue-sdk-v2's shared httpx client with a longer-timeout one. Idempotent."""
    ...

def _extract_filled_shares(result: Any) -> float | None:
    ...

def _post_orders_args(signed: Any, order_type: Any) -> Any:
    """The batch arg wrapper matching the signed order's exchange version."""
    ...

def _batch_rows(raw: Any, n: int) -> list[Any] | None:
    """The venue's per-order results, or None if they cannot be identified."""
    ...

def _response_error(result: Any) -> str:
    """Classify an HTTP-200 matcher rejection without discarding its body."""
    ...

def _order_book_levels(raw: Any, side: str) -> tuple[OrderBookLevel, ...]:
    ...

def _first_env(*names: str) -> str:
    ...

def _env_signature_type() -> int:
    ...

def _env_funder(signature_type: int) -> str | None:
    ...

def _api_creds_from_env():
    ...

def _is_invalid_api_key_error(error: Exception) -> bool:
    ...

class V2CLOBAdapter:
    """Concrete V2 CLOBClient. Lazily builds the underlying venue-sdk-v2.ClobClient."""

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

    def _call_with_env_credential_retry(self, operation):
        ...

    def get_balance(self) -> float:
        ...

    def get_token_balance(self, token_id: str) -> float:
        ...

    def get_balance_allowance_snapshot(self, *, asset_kind: str, token_id: str | None=None) -> dict[str, Any]:
        """Return raw read-only balance/allowance fields for sanitized snapshots."""
        ...

    def place_order(self, request: OrderRequest) -> OrderResult:
        ...

    def _place_limit(self, request: OrderRequest) -> OrderResult:
        """Place a limit order, optionally as a maker-only or expiring order."""
        ...

    def place_orders(self, requests: Sequence[OrderRequest]) -> list[OrderResult]:
        """Submit several limit orders in ONE request, in the order given."""
        ...

    def _place_market(self, request: OrderRequest) -> OrderResult:
        ...

    def cancel_order(self, order_id: str) -> bool:
        """Cancel one resting order.  Returns whether the venue accepted it."""
        ...

    def get_order(self, order_id: str) -> Any:
        ...

    def cancel_all(self) -> bool:
        ...

    def get_open_orders(self, token_id: str | None=None) -> list[Any]:
        ...

    def get_open_orders_strict(self, token_id: str | None=None) -> list[Any]:
        """Open orders, or a raise. Never `[]` for a read that did not happen."""
        ...

    def get_tick_size(self, token_id: str) -> float:
        ...

    def get_order_book(self, token_id: str) -> OrderBook | None:
        ...
