"""Per-arm loss accounting and brake, for instruments that run several arms at once."""

@dataclass(frozen=True, slots=True)
class ArmPosition:
    """One arm's realised exposure in one window, as the VENUE reports it."""
    arm: str
    op: int
    side: str
    shares: float
    cost: float

    @property
    def is_open(self) -> bool:
        ...

@dataclass(frozen=True, slots=True)
class ArmState:
    """What the brake knows about one arm right now."""
    arm: str
    realised: float
    settled: int
    open_positions: int
    stopped: str | None

def _read_jsonl(path: Path) -> Iterable[dict]:
    ...

def positions_from_ledger(ledger: Path, arms: Sequence[str], fills_by_order: Mapping[str, tuple[str, float, float]], *, since_ts: float=0.0, arm_field: str='sig_arm') -> list[ArmPosition]:
    """Join our ledger's *intent* to the venue's *fills*."""
    ...

def realised_by_arm(positions: Iterable[ArmPosition], winners: Mapping[int, str | None]) -> dict[str, tuple[float, int, int]]:
    """arm -> (realised, settled_count, open_count)."""
    ...

def brake_reason(realised: float | None, limit_usd: float) -> str | None:
    """Why this arm must stop, or None."""
    ...

class ArmBrake:
    """Cached per-arm brake for a live loop."""

    def __init__(self, ledger: Path, arms: Sequence[str], limit_usd: float, *, fills_loader, winner_loader, ttl_s: float=60.0, since_ts: float=0.0, arm_field: str='sig_arm', winner_retry_s: float=300.0, winner_max_tries: int=6) -> None:
        ...

    def _winner(self, op: int) -> str | None:
        """Resolved outcomes are immutable, so cache them forever."""
        ...

    def refresh(self) -> dict[str, ArmState]:
        ...

    def state(self, arm: str, *, refresh_ok: bool=True) -> ArmState:
        """An arm this brake was not built to watch is STOPPED, not allowed."""
        ...

    def cached_state(self, arm: str, *, max_age_s: float) -> ArmState:
        """Return the last refresh without ever calling a loader."""
        ...

    def allows(self, arm: str, *, refresh_ok: bool=True) -> bool:
        ...
