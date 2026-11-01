"""Venue Collateral Onramp adapter — wraps USDC / USDC.e → collateral."""

@dataclass(frozen=True)
class WrapPlan:
    """Pre-built calldata for the wrap pipeline (no transactions sent)."""
    native_usdc_balance: int
    usdce_balance: int
    needs_swap: bool
    swap_plan: SwapPlan | None
    approve_calldata: str
    wrap_calldata: str
    wrap_amount_total: int
    recipient: str

    def summary_lines(self) -> list[str]:
        ...

@dataclass
class WrapStepResult:
    name: str
    ok: bool
    detail: str

@dataclass
class WrapResult:
    success: bool
    steps: list[WrapStepResult]
    pre_balance_native_usdc: int
    pre_balance_usdce: int
    pre_balance_pusd: int
    post_balance_pusd: int
    error: str

    def summary_lines(self) -> list[str]:
        ...

def encode_balance_of(owner: str) -> str:
    """ERC20 balanceOf(address) calldata."""
    ...

def encode_approve(spender: str, amount: int) -> str:
    """ERC20 approve(address,uint256) calldata."""
    ...

def encode_wrap(asset: str, recipient: str, amount: int) -> str:
    """Venue onramp wrap(address,address,uint256) calldata."""
    ...

class CollateralOnrampAdapter:
    """Wrap USDC / USDC.e → collateral via the Venue onramp."""

    def __init__(self, *, gasless_client: Any, dex_router: DexRouter, owner_address: str | None=None, slippage_bps: int=30, onramp_address: str=VENUE_ONRAMP) -> None:
        """``owner_address`` is the address whose balance gets wrapped — the"""
        ...

    def _read_token_balance(self, token: str, owner: str) -> int:
        """Read ERC20 balance via the gasless client's underlying web3 instance."""
        ...

    def build_plan(self, recipient: str | None=None) -> WrapPlan:
        """Inspect funder balances + onramp state, build the calldata plan."""
        ...

    def _is_native_usdc_paused(self) -> bool:
        """Probe the onramp for native USDC by simulating a wrap call."""
        ...

    def wrap_all_collateral(self, recipient: str | None=None, *, dry_run: bool=False) -> WrapResult:
        ...

def build_default_onramp_adapter(slippage_bps: int=100, dex: str='v3') -> CollateralOnrampAdapter:
    """Default factory — wires the Venue gasless client + chosen DEX router."""
    ...
