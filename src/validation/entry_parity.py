
def _series(df: pd.DataFrame, column: str) -> pd.Series:
    ...

def _sim_entry_mask(df: pd.DataFrame) -> pd.Series:
    ...

def _live_entry_mask(df: pd.DataFrame) -> pd.Series:
    ...

def _sim_only_live_reject_mask(df: pd.DataFrame, bucket: str) -> pd.Series:
    ...

@dataclass(frozen=True)
class EntryParityBreakdown:
    """Entry-count focused parity summary."""
    total_rows: int
    live_entries: int
    sim_entries: int
    overlapping_entries: int
    sim_only_entries: int
    live_only_entries: int
    sim_only_no_live_event: int
    sim_only_live_execution_reject: int
    sim_only_live_safety_reject: int
    sim_only_live_account_reject: int
    sim_only_live_infra_reject: int
    sim_only_live_other_reject: int
    sim_only_live_unknown_reject: int

    @property
    def projected_sim_entries_without_account_safety(self) -> int:
        ...

    @property
    def projected_sim_entries_without_live_rejections(self) -> int:
        ...

    @property
    def entry_recall_pct(self) -> float | None:
        ...

    @property
    def entry_precision_pct(self) -> float | None:
        ...

    def to_dict(self) -> dict[str, Any]:
        ...

def build_entry_parity_breakdown(df: pd.DataFrame) -> EntryParityBreakdown:
    ...

def entry_parity_markdown_lines(breakdown: EntryParityBreakdown) -> list[str]:
    ...
