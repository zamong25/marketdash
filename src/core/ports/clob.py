"""CLOB client port — boundary between business code and concrete SDKs."""

class CLOBError(Exception):
    """Base for all CLOB-side failures surfaced through a port adapter."""

class CLOBAuthError(CLOBError):
    """Auth / signature / API-key derivation failed (HTTP 401, 403)."""

class CLOBNetworkError(CLOBError):
    """Network / timeout / unreachable host (httpx.TimeoutException etc)."""

class CLOBOrderRejected(CLOBError):
    """Order accepted by the wire but rejected by the matcher."""

    def __init__(self, message: str, *, code: str='', classification: str='', raw_response: Any=None) -> None:
        ...

class CLOBVersionError(CLOBError):
    """SDK / endpoint version mismatch (V1 SDK against V2 endpoint, or"""

class CLOBGeoBlocked(CLOBError):
    """Endpoint refused based on caller geography — distinct from auth so"""

@dataclass(frozen=True)
class OrderRequest:
    """Adapter-agnostic order request."""
    token_id: str
    side: str
    shares: float
    price: float | None
    order_type: str
    extras: Mapping[str, Any]

@dataclass(frozen=True)
class OrderResult:
    """Adapter-agnostic order outcome."""
    success: bool
    order_id: str
    error: str
    filled_shares: float | None
    order_type_used: str
    primary_error: str
    raw_response: Any

@dataclass(frozen=True)
class BalanceInfo:
    """Wallet balance snapshot in micro-USDC for collateral, raw for tokens."""
    asset_kind: str
    token_id: str | None
    raw: int

    @property
    def usd(self) -> float:
        """Convenience: convert micro units to USD float (only meaningful for collateral)."""
        ...

@dataclass(frozen=True)
class OrderBookLevel:
    price: float
    size: float

@dataclass(frozen=True)
class OrderBook:
    token_id: str
    bids: tuple[OrderBookLevel, ...]
    asks: tuple[OrderBookLevel, ...]
    raw: Any

class CLOBClient(Protocol):
    """The narrow contract every CLOB SDK adapter must satisfy."""

    @property
    def version(self) -> str:
        """Return ``"v1"`` or ``"v2"`` so factory code can log + the canary"""
        ...

    def get_balance(self) -> float:
        """Return collateral balance in USD."""
        ...

    def get_token_balance(self, token_id: str) -> float:
        """Return conditional-token balance for one outcome token."""
        ...

    def place_order(self, request: OrderRequest) -> OrderResult:
        """Place a single order; raises CLOBError subclass on hard failure."""
        ...

    def get_order(self, order_id: str) -> Any:
        """Return the read-only CLOB order record for ``order_id``."""
        ...

    def cancel_order(self, order_id: str) -> bool:
        ...

    def cancel_all(self) -> bool:
        ...

    def get_open_orders(self, token_id: str | None=None) -> list[Any]:
        ...

    def get_order_book(self, token_id: str) -> OrderBook | None:
        ...
