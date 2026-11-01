
class BalanceAdapter(Protocol):

    def get_balance(self) -> float:
        ...

    def get_token_balance(self, token_id: str) -> float:
        ...

@dataclass(frozen=True)
class BalanceEntry:
    value: float
    refreshed_at: float | None
    age_s: float

    @property
    def is_refreshed(self) -> bool:
        ...

class BalanceCache:

    def __init__(self, *, clock: Callable[[], float] | None=None, max_age_s: float=10.0) -> None:
        ...

    @property
    def last_refresh_at(self) -> float | None:
        ...

    @property
    def last_error(self) -> str:
        ...

    def track_token(self, token_id: str) -> None:
        ...

    def refresh(self, adapter: BalanceAdapter) -> None:
        ...

    def refresh_sync_for_token(self, adapter: BalanceAdapter, token_id: str) -> None:
        ...

    def force_refresh_after_fill(self, adapter: BalanceAdapter, token_id: str) -> None:
        """Unconditional post-trade refresh of USDC + the given token balance."""
        ...

    def usdc(self) -> BalanceEntry:
        ...

    def token(self, token_id: str) -> BalanceEntry:
        ...

    def is_fresh(self, max_age_s: float | None=None) -> bool:
        ...

    def start_background_refresher(self, adapter: BalanceAdapter, *, interval_s: float=5.0, logger: logging.Logger | None=None) -> None:
        ...

    def ensure_background_refresher(self) -> None:
        ...

    def stop_background_refresher(self, timeout_s: float=2.0) -> None:
        ...

    def is_background_running(self) -> bool:
        ...

    def _apply_refresh_under_lock(self, *, refreshed_at: float, usdc_value: float | None=None, token_values: dict[str, float] | None=None) -> None:
        ...

    def _entry(self, value: float, refreshed_at: float | None) -> BalanceEntry:
        ...

    def _is_stale_under_lock(self, refreshed_at: float | None, max_age_s: float) -> bool:
        ...

    def _refresh_loop(self) -> None:
        ...
