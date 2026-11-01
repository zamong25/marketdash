"""Redemption lifecycle tracker."""

@dataclass
class RedemptionState:
    """Current redemption state for a single settlement window."""
    window_slug: str
    condition_id: str
    status: str
    tx_hash: str | None
    proceeds_usd: float | None
    last_updated: float
    error: str
    strategy_name: str
    shares_held: float
    cost_usd: float
    entry_direction: str
    entry_order_id: str | None
    token_id: str
    source: str
    logged: bool
    confirmed: bool

    def snapshot(self) -> dict[str, Any]:
        ...

class RedemptionTracker:
    """Maintain redemption state keyed by window_slug."""

    def __init__(self) -> None:
        ...

    def mark_settled(self, *, window_slug: str, condition_id: str, won: bool, strategy_name: str='', shares_held: float=0.0, cost_usd: float=0.0, entry_direction: str='', entry_order_id: str | None=None, token_id: str='') -> RedemptionState:
        """Record that a window just settled."""
        ...

    def apply_redemption_results(self, results: list[dict[str, Any]]) -> list[str]:
        """Fold adapter.redeem_all() results into tracker state."""
        ...

    def list_pending(self) -> list[RedemptionState]:
        """Return every state still awaiting redemption confirmation."""
        ...

    def mark_confirmed_via_auto_redeemer(self, window_slug: str, *, proceeds_usd: float) -> RedemptionState | None:
        """Transition a pending state to ``redeemed`` without a tx hash."""
        ...

    def get(self, window_slug: str) -> RedemptionState:
        """Return the state for a window (creates an ``n/a`` entry if unseen)."""
        ...

    def has_any_pending(self) -> bool:
        """True if at least one window is still awaiting redemption."""
        ...

    def pop_unlogged_completed(self) -> list[RedemptionState]:
        """Return states that are terminal (redeemed or failed) but haven't"""
        ...

    def pop_unconfirmed(self) -> list[RedemptionState]:
        """Return auto-redeemer-observed states whose"""
        ...
