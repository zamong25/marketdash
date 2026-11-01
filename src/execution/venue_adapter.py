"""Venue adapter — thin facade over a CLOB client port."""

@dataclass(frozen=True)
class AdapterOrderResult:
    """Public result type kept for backward compatibility with the existing"""
    success: bool
    order_id: str
    error: str
    filled_shares: float | None
    order_type_used: str
    primary_error: str
    raw_response: Any

    @classmethod
    def from_port_result(cls, result: OrderResult) -> 'AdapterOrderResult':
        ...

class VenueAdapter:
    """High-level operations on top of the CLOB port + the gasless redemption client."""

    def __init__(self, client: Optional[CLOBClient]=None) -> None:
        ...

    @property
    def client(self) -> CLOBClient:
        ...

    def get_balance(self) -> float:
        ...

    def get_token_balance(self, token_id: str) -> float:
        ...

    def place_limit_order(self, token_id: str, side: str, price: float, shares: float, order_type: str='GTC') -> AdapterOrderResult:
        ...

    def place_market_order(self, token_id: str, side: str, amount: float, order_type: str='FAK') -> AdapterOrderResult:
        """Submit a market-style order (FAK by default)."""
        ...

    def cancel_order(self, order_id: str) -> bool:
        ...

    def get_order(self, order_id: str) -> Any:
        ...

    def cancel_all(self) -> bool:
        ...

    def get_open_orders(self, token_id: str | None=None) -> list[Any]:
        ...

    def get_open_orders_strict(self, token_id: str | None=None) -> list[Any]:
        """Open orders, or a raise -- for safety sweeps. See the V2 adapter."""
        ...

    def get_order_book(self, token_id: str) -> Any:
        ...

    def _build_web3_client(self):
        ...

    def _build_data_client(self):
        ...

    def get_redeemable_positions(self) -> list[Any]:
        """Redeemable positions, or `[]` for ANY failure. Screens only."""
        ...

    def get_redeemable_positions_strict(self) -> list[Any]:
        """Redeemable positions, or a raise. `[]` means the venue said none."""
        ...

    def redeem_all(self) -> list[dict[str, Any]]:
        """Redeem every position flagged as redeemable."""
        ...

    @staticmethod
    def _redeem_multi_outcome_v2(*, web3: Any, condition_id: str) -> Any:
        """Redeem a V2 negative-risk position into collateral."""
        ...
