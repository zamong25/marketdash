"""Deterministic live-wallet cash reconstruction for sim-vs-live validation."""

def _finite_float(value: Any) -> float | None:
    ...

def _parse_ts_s(value: object) -> int | None:
    ...

def _slug_start_ts(slug: str) -> int:
    ...

def _parse_log_date(path: Path) -> date | None:
    ...

def load_live_wallet_buckets(log_root: str | Path, *, end_date: str, include_quarantine: bool=False, include_unverified: bool=True) -> dict[str, dict[str, Any]]:
    """Load live trade records across strategies into reconstruction buckets."""
    ...

def _trusted_live_buy_meta(bucket: Mapping[str, Any]) -> tuple[dict[str, Any], dict[str, Any]] | None:
    ...

@dataclass(frozen=True)
class LiveCashDeltaEvent:
    ts_s: int
    delta_usd: float
    source: str
    window_slug: str
    event_type: str
    confidence: str

@dataclass(frozen=True)
class LiveCashDriftCheck:
    ts_s: int
    source: str
    observed_cash_usd: float
    reconstructed_cash_usd: float | None
    rel_err_pct: float | None
    within_1pct: bool
    exceeds_5pct: bool

@dataclass(frozen=True)
class ReconstructedLiveAccountCash:
    anchor_ts_s: int | None
    anchor_cash_usd: float | None
    timeline: tuple[tuple[int, float], ...]
    events: tuple[LiveCashDeltaEvent, ...]
    exact_observations: tuple[AccountCashObservation, ...]
    drift_checks: tuple[LiveCashDriftCheck, ...]

    @property
    def within_1pct_count(self) -> int:
        ...

    @property
    def exceeds_5pct_count(self) -> int:
        ...

    @property
    def max_rel_err_pct(self) -> float | None:
        ...

@dataclass(frozen=True)
class LiveCashReconstructionOptions:
    include_estimated_buy_debits: bool
    allow_estimated_buy_anchor: bool
    include_untrusted_buy_observations: bool
    require_open_provenance_for_credit: bool
    reanchor_from_observations: bool

def _reconstructed_cash_at(timeline: tuple[tuple[int, float], ...], ts_s: int) -> float | None:
    ...

def _buy_with_meta(bucket: Mapping[str, Any]) -> tuple[dict[str, Any], dict[str, Any], float, float] | None:
    ...

def reconstruct_live_account_cash_timeline(live_by_slug: Mapping[str, Mapping[str, Any]], *, options: LiveCashReconstructionOptions | None=None) -> ReconstructedLiveAccountCash:
    """Return a deterministic cash tape from trusted live trade events."""
    ...
