"""DEX router adapter — abstracts the QuickSwap V2 swap path."""

@dataclass(frozen=True)
class SwapPlan:
    """The pre-built calldata for a swap, plus expected output."""
    router_address: str
    approve_calldata: str
    swap_calldata: str
    token_in: str
    token_out: str
    amount_in: int
    min_amount_out: int

@dataclass(frozen=True)
class SwapResult:
    success: bool
    approve_tx: Any
    swap_tx: Any
    error: str

class DexRouter(Protocol):
    """Single-hop ERC20 swap via a DEX router."""

    def build_swap_plan(self, token_in: str, token_out: str, amount_in: int, min_amount_out: int, recipient: str, deadline_offset_s: int=600) -> SwapPlan:
        ...

    def execute_swap(self, plan: SwapPlan) -> SwapResult:
        ...

class QuickSwapV2Router:
    """QuickSwap V2 router on Polygon (concrete DexRouter implementation)."""

    def __init__(self, gasless_client: Any) -> None:
        """``gasless_client`` is a ``VenueGaslessWeb3Client`` (avoiding the"""
        ...

    @property
    def router_address(self) -> str:
        ...

    def build_swap_plan(self, token_in: str, token_out: str, amount_in: int, min_amount_out: int, recipient: str, deadline_offset_s: int=600) -> SwapPlan:
        ...

    def execute_swap(self, plan: SwapPlan) -> SwapResult:
        """Approve token_in to router, then submit the swap. Both gasless."""
        ...

class UniswapV3Router:
    """Uniswap V3 SwapRouter02 on Polygon (preferred for stable pairs)."""

    def __init__(self, gasless_client: Any, *, fee_tier: int=UNISWAP_V3_FEE_001PCT) -> None:
        ...

    @property
    def router_address(self) -> str:
        ...

    def build_swap_plan(self, token_in: str, token_out: str, amount_in: int, min_amount_out: int, recipient: str, deadline_offset_s: int=600) -> SwapPlan:
        ...

    def execute_swap(self, plan: SwapPlan) -> SwapResult:
        """Approve + swap, both gasless via the redeemer."""
        ...
