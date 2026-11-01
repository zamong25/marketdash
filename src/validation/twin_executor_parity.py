
def _safe_float(value: object) -> float | None:
    ...

def _median(values: list[float]) -> float | None:
    ...

def _p95(values: list[float]) -> float | None:
    ...

def _decision_paths(log_root: Path, strategy_name: str, date: str) -> tuple[Path, ...]:
    ...

def _iter_rows(paths: Iterable[Path]) -> Iterable[dict[str, Any]]:
    ...

def _classify_pair(paper_type: str | None, live_type: str | None) -> str:
    ...

@dataclass(frozen=True)
class TwinDecisionPair:
    twin_run_id: str
    strategy_name: str
    window_slug: str
    signal_ts: int | None
    direction: str | None
    paper_type: str | None
    live_type: str | None
    paper_rejection_reason: str | None
    live_rejection_reason: str | None
    paper_requested_shares: float | None
    live_requested_shares: float | None
    paper_filled_shares: float | None
    live_filled_shares: float | None
    paper_fill_price: float | None
    live_fill_price: float | None
    classification: str

    @property
    def decision_match(self) -> bool:
        ...

    @property
    def fill_price_abs_diff(self) -> float | None:
        ...

    @property
    def filled_shares_abs_diff(self) -> float | None:
        ...

    def to_dict(self) -> dict[str, Any]:
        ...

@dataclass(frozen=True)
class TwinExecutorParitySummary:
    total_pairs: int
    decision_match_pairs: int
    both_accept: int
    both_reject: int
    paper_accept_live_reject: int
    live_accept_paper_reject: int
    paper_accept_live_missing: int
    live_accept_paper_missing: int
    paper_reject_live_missing: int
    live_reject_paper_missing: int
    unclassified: int
    live_rejection_reasons: dict[str, int]
    paper_rejection_reasons: dict[str, int]
    both_accept_fill_price_median_abs_diff: float | None
    both_accept_fill_price_p95_abs_diff: float | None
    both_accept_filled_shares_median_abs_diff: float | None
    both_accept_filled_shares_p95_abs_diff: float | None

    @property
    def decision_match_pct(self) -> float | None:
        ...

    def to_dict(self) -> dict[str, Any]:
        ...

def load_twin_decision_pairs(log_root: str | Path, strategy_name: str, date: str) -> tuple[TwinDecisionPair, ...]:
    ...

def build_twin_executor_parity_summary(pairs: Iterable[TwinDecisionPair]) -> TwinExecutorParitySummary:
    ...

def twin_executor_parity_markdown_lines(summary: TwinExecutorParitySummary) -> list[str]:
    ...
