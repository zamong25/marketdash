
def _safe_pct(numerator: float, denominator: float) -> float | None:
    ...

def _sim_filled_mask(df: pd.DataFrame) -> pd.Series:
    ...

def _bounded_score(actual: float | None, target: float) -> float:
    ...

def _bounded_inverse_score(actual: float | None, target: float) -> float:
    ...

@dataclass(frozen=True)
class ParityThresholds:
    trigger_recall_pct: float
    trigger_precision_pct: float
    timing_median_abs_s: float
    timing_p95_abs_s: float
    timing_within_1s_pct: float
    entry_recall_pct: float
    entry_precision_pct: float
    execution_decision_match_pct: float
    fill_median_abs_err: float
    fill_p95_abs_err: float
    pnl_day_rel_err_pct: float

@dataclass(frozen=True)
class ParityMetrics:
    total_rows: int
    sim_filled_entries: int
    live_filled_entries: int
    overlapping_filled_entries: int
    trigger_recall_pct: float | None
    trigger_precision_pct: float | None
    trigger_match_rate_pct: float | None
    timing_median_abs_s: float | None
    timing_p95_abs_s: float | None
    timing_within_1s_pct: float | None
    entry_recall_pct: float | None
    entry_precision_pct: float | None
    entry_jaccard_pct: float | None
    execution_decision_match_pct: float | None
    fill_median_abs_err: float | None
    fill_p95_abs_err: float | None
    matched_pnl_rel_err_pct: float | None
    day_total_pnl_rel_err_pct: float | None

@dataclass(frozen=True)
class ScoreBreakdown:
    trigger: float
    timing: float
    execution: float
    fill: float
    pnl: float
    total: float

@dataclass(frozen=True)
class PctMetric:
    pct: float | None

@dataclass(frozen=True)
class TimingMetric:
    abs_median_s: float | None
    abs_p95_s: float | None
    within_1s_pct: float | None

@dataclass(frozen=True)
class FillErrorMetric:
    median: float | None
    p95: float | None

@dataclass(frozen=True)
class PnlErrorMetric:
    relative_error_pct: float | None

@dataclass(frozen=True)
class DeterminismDiff:
    compared_rows: int
    differing_rows: int
    row_match_rate_pct: float
    differing_slugs: tuple[str, ...]
    column_mismatch_counts: dict[str, int]

    def to_dict(self) -> dict[str, Any]:
        ...

@dataclass(frozen=True)
class ParityScorecard:
    metrics: ParityMetrics
    thresholds: ParityThresholds
    trigger_score: float
    timing_score: float
    execution_score: float
    fill_score: float
    pnl_score: float
    weighted_score: float
    floors_passed: bool
    failing_floors: tuple[str, ...]
    failing_gates_90: tuple[str, ...]

    def to_dict(self) -> dict[str, Any]:
        ...

    @property
    def overall_score(self) -> float:
        ...

    @property
    def scores(self) -> ScoreBreakdown:
        ...

    @property
    def passes_hard_floors(self) -> bool:
        ...

    @property
    def passes_85(self) -> bool:
        ...

    @property
    def passes_90(self) -> bool:
        ...

    @property
    def passes_85_gate(self) -> bool:
        ...

    @property
    def passes_90_gate(self) -> bool:
        ...

    @property
    def failed_gates(self) -> tuple[str, ...]:
        ...

    @property
    def sim_filled_entries(self) -> int:
        ...

    @property
    def live_filled_entries(self) -> int:
        ...

    @property
    def overlapping_filled_entries(self) -> int:
        ...

    @property
    def trigger_recall(self) -> PctMetric:
        ...

    @property
    def trigger_precision(self) -> PctMetric:
        ...

    @property
    def actual_entry_recall(self) -> PctMetric:
        ...

    @property
    def actual_entry_precision(self) -> PctMetric:
        ...

    @property
    def actual_entry_overlap_rate(self) -> PctMetric:
        ...

    @property
    def trigger_timing(self) -> TimingMetric:
        ...

    @property
    def fill_price_error(self) -> FillErrorMetric:
        ...

    @property
    def matched_pnl(self) -> PnlErrorMetric:
        ...

    @property
    def total_pnl(self) -> PnlErrorMetric:
        ...

def scorecard_from_dataframe(df: pd.DataFrame, thresholds: ParityThresholds | None=None) -> ParityScorecard:
    ...

def compute_parity_metrics(df: pd.DataFrame) -> ParityMetrics:
    ...

def build_parity_scorecard(df: pd.DataFrame, thresholds: ParityThresholds | None=None) -> ParityScorecard:
    ...

def build_parity_scorecard_from_csv(path: str | Path, thresholds: ParityThresholds | None=None) -> ParityScorecard:
    ...

def compare_runs_for_determinism(left: pd.DataFrame, right: pd.DataFrame, *, key: str='slug', compare_columns: Iterable[str] | None=None) -> DeterminismDiff:
    ...
