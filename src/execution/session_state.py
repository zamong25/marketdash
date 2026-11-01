"""Per-day session state for the simulator."""

@dataclass(frozen=True)
class HeldSimPosition:
    """Lightweight description of an active simulated hold."""
    day: str
    window_slug: str
    direction: str
    shares: float
    expire_ts_s: int
    source_status: str | None

@dataclass(frozen=True)
class ExternalPositionInterval:
    """Position interval observed outside the simulated seed path."""
    window_slug: str
    direction: str
    open_ts_s: int
    close_ts_s: int
    source: str

    def is_open_at(self, ts_s: int) -> bool:
        ...

@dataclass(frozen=True)
class AccountCashObservation:
    """Observed wallet cash point used by validation-only account gating."""
    ts_s: int
    cash_usd: float
    persistence: Literal['carry_forward', 'instant']
    source: str

@dataclass
class SimSession:
    """Tracker factory keyed by UTC day string (``YYYY-MM-DD``)."""
    name: str
    starting_cash: float
    account_cash_usd: float | None
    account_cash_timeline: tuple[tuple[int, float], ...]
    account_cash_observations: tuple[AccountCashObservation, ...]
    external_position_intervals: tuple[ExternalPositionInterval, ...]
    settlement_delay_s: int
    _trackers: dict[str, PositionTracker]

    @classmethod
    def from_strategy_params(cls, *, name: str, params: Mapping[str, object] | None=None, settlement_delay_s: int | None=None, starting_cash: float | None=None, account_cash_usd: float | None=None, account_cash_timeline: Sequence[tuple[int, float]] | None=None, account_cash_observations: Sequence[AccountCashObservation] | None=None, external_position_intervals: Sequence[ExternalPositionInterval] | None=None) -> 'SimSession':
        """Build a session from strategy params with optional overrides."""
        ...

    def tracker_for(self, day: str) -> PositionTracker:
        """Return (and lazily create) the tracker for ``day``."""
        ...

    def _seed_cash_for_day(self, day: str) -> float:
        """Cash a fresh UTC-day tracker should start with."""
        ...

    def _propagate_cash_delta(self, source_day: str, delta: float) -> None:
        """Apply a cash change on ``source_day`` to every later day."""
        ...

    def account_gate_enabled(self) -> bool:
        """True when the sim should enforce actual-wallet cash limits."""
        ...

    def account_cash_at(self, ts_s: int | None=None) -> float | None:
        """Return simulated/observed wallet cash at ``ts_s``."""
        ...

    def account_observation_age_s(self, ts_s: int | None=None) -> float | None:
        """Seconds since the latest exact account-cash observation."""
        ...

    def can_spend_account_cash(self, budget_usd: float, *, ts_s: int | None=None) -> bool:
        """Return whether the simulated wallet can fund an order budget."""
        ...

    def debit_account_cash(self, cost_usd: float | None) -> None:
        """Debit actual-wallet cash after a simulated fill."""
        ...

    def credit_account_cash(self, proceeds_usd: float | None) -> None:
        """Credit actual-wallet cash after simulated redemption/settlement."""
        ...

    def open_positions(self) -> list[TrackedPosition]:
        """Return every currently-open tracked position across all days."""
        ...

    def position_expire_ts_s(self, position: TrackedPosition) -> int:
        """Return when ``position`` stops blocking new entries in sim."""
        ...

    def held_positions(self) -> list[HeldSimPosition]:
        """Return active sim holds with their computed release timestamps."""
        ...

    def blocking_position(self) -> HeldSimPosition | None:
        """Return the currently-active hold that blocks new entries."""
        ...

    def external_blocking_position(self, ts_s: int, *, exclude_slug: str | None=None) -> HeldSimPosition | None:
        """Return an externally-observed hold active at ``ts_s``."""
        ...

    def record_simulated_pnl(self, day: str, pnl: float | None) -> None:
        """Apply a sim-derived PnL delta to the day's tracker."""
        ...

    @staticmethod
    def _window_start_ts(slug: str) -> int:
        ...

    def settle_position_if_due(self, day: str, now_ts_s: int) -> SettlementResult | None:
        """Settle any prior position whose window has closed by ``now_ts_s``."""
        ...

    def expire_position_if_due(self, day: str, now_ts_s: int) -> float | None:
        """Backward-compatible pnl-only wrapper around settlement expiry."""
        ...

    def settle_all_due(self, now_ts_s: int) -> list[SettlementResult]:
        """Run :meth:`settle_position_if_due` across every day's tracker."""
        ...

    def expire_all_due(self, now_ts_s: int) -> None:
        """Backward-compatible wrapper that drains due positions."""
        ...

    def finalize_open_positions(self) -> list[SettlementResult]:
        """Drain any still-open position at the end of a run."""
        ...

    def any_in_position(self) -> bool:
        """True if any day's tracker still holds a position."""
        ...

    def register_simulated_position(self, day: str, slug: str, direction: str, *, shares: float, entry_price: float, cost_usd: float, pending_pnl: float, outcome_winner: str | None=None, opened_at_ts_s: int | None=None, source_status: str | None=None, settlement_release_ts_s: int | None=None) -> None:
        """Open a sim position that will expire at ``window_end``."""
        ...

    @staticmethod
    def _settlement_outcome(direction: str, pnl: float, info: dict | None) -> str:
        """Return the winning outcome name for a settled sim position."""
        ...
