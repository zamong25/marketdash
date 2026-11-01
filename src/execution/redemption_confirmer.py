"""Auto-redeemer observation → ``redemption_confirmation`` record emitter."""

class _TokenBalanceReader(Protocol):
    """Minimal adapter contract the confirmer needs."""

    def get_token_balance(self, token_id: str) -> float:
        ...

@dataclass(frozen=True)
class ConfirmationEvent:
    """One pending state that transitioned to ``redeemed`` this tick."""
    state: RedemptionState
    proceeds_usd: float
    observation_source: str

class RedemptionConfirmer:
    """Scan pending redemptions for auto-redeemer transitions."""

    def __init__(self, adapter: _TokenBalanceReader, tracker: RedemptionTracker, *, min_poll_interval_s: float=5.0, clock: 'callable[[], float] | None'=None) -> None:
        ...

    def confirm(self, *, force: bool=False) -> list[ConfirmationEvent]:
        """Advance any pending states whose tokens have been burnt."""
        ...
