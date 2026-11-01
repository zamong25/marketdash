"""Fill pipeline orchestrator."""

@dataclass
class FillOutcome:
    """Terminal state after FillModel.simulate completes."""
    result_reason: str
    fill_price: float | None
    filled_shares: float
    latency_ms: int
    retries: int
    effects_applied: list[str]
    book_staleness_ms: int | None

@dataclass
class FillContext:
    """Mutable state threaded through the pipeline."""
    signal_ts_ms: int
    direction: str
    requested_shares: float
    token_id: str
    window_slug: str
    min_ask_depth_shares: int
    fak_retry_enabled: bool
    fak_retry_backoff_s: int
    retry_min_remaining_s: int
    signal_price: float | None
    max_retries: int
    min_retry_threshold: float
    snapshot_sanity_enabled: bool
    max_snapshot_ask_gap: float
    use_fast_path: bool
    budget_usd: float | None
    snapshot_fallback_ask_price: float | None
    snapshot_fallback_ask_depth: float | None
    snapshot_fallback_ts_ms: int | None
    snapshot_fallback_source: str | None
    snapshot_best_bid: float | None
    snapshot_best_ask: float | None
    snapshot_spread: float | None
    max_snapshot_sanity_horizon_ms: int
    order_snapshot_provider: 'PointInTimeSnapshotProvider | None'
    strategy_family: str | None
    attempt_ts_ms: int | None
    retries: int
    tentative_fill_price: float | None
    tentative_filled_shares: float | None
    last_book_ts_ms: int | None
    snapshot_sanity_applied: bool
    snapshot_sanity_original_ask: float | None
    snapshot_sanity_original_ts_ms: int | None
    suppress_retry: bool
    api_error_bucket: str | None
    api_error_prob: float | None
    api_error_roll: float | None
    api_error_reason_kind: str | None
    api_error_reason_family: str | None
    partial_fill_price_bucket: str | None
    partial_fill_depth_bucket: str | None
    partial_fill_remaining_bucket: str | None
    partial_fill_sample_count: int | None
    partial_fill_sampled_ratio: float | None
    canonical_outcome_applied: bool
    canonical_outcome_reason: str | None
    canonical_outcome_prob: float | None
    canonical_outcome_source: str | None
    canonical_outcome_signal_remaining_bucket: str | None
    canonical_apparent_filled_shares: float | None
    canonical_apparent_fill_price: float | None
    accumulated_filled_shares: float
    accumulated_notional_usd: float
    book_lookup_source: str | None
    result_reason: str | None
    effects_applied: list[str]

    @property
    def window_start_s(self) -> int:
        ...

    @property
    def window_end_s(self) -> int:
        ...

    def remaining_s_at_ms(self, ts_ms: int | None) -> int:
        ...

    @property
    def signal_remaining_s(self) -> int:
        ...

    @property
    def attempt_remaining_s(self) -> int | None:
        ...

    def accumulate_attempt_fill(self) -> None:
        ...

    def finalize_accumulated_fill(self) -> None:
        ...

@dataclass
class FillModel:
    effects: list['Effect']

    def simulate(self, context: FillContext, book: 'BookProvider') -> FillContext:
        """Run the pipeline. Handles retry_requested sentinel at the top"""
        ...

def calibration_root_from(base: str | Path | None=None) -> Path:
    """Resolve the default calibration directory, overridable in tests."""
    ...

class CalibrationError(RuntimeError):
    """Raised when a requested calibration file is missing or uncalibrated."""

def _manifest_calibration_overrides(calibration_root: Path) -> dict[str, Path]:
    ...

def resolve_calibration_path(calibration_root: Path, effect_slug: str, overrides: Phase3CalibrationOverrides | None=None) -> Path:
    """Return the calibration JSON path for ``effect_slug``."""
    ...

def build_default_effects(execution_config: dict, latency_model, calibration_root: Path, *, seed: int=42, calibration_overrides: Phase3CalibrationOverrides | None=None) -> list['Effect']:
    """Assemble the effect pipeline from ``[execution.realistic]`` flags."""
    ...

def _p3_enabled(execution_config: dict, calibration_root: Path, effect_slug: str, flag_key: str, *, calibration_overrides: Phase3CalibrationOverrides | None=None) -> bool:
    ...
