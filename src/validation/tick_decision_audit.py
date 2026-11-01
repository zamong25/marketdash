
def load_tick_decision_audit_rows(path: str | Path, *, days: Iterable[str] | None=None, runner: str | None=None, strategy: str | None=None) -> list[dict[str, Any]]:
    """Load per-tick decision audit rows from JSONL."""
    ...

@dataclass(frozen=True)
class TickDecisionAuditSummary:
    total_rows: int
    status_counts: dict[str, int]
    reason_counts: dict[str, int]
    accepted_true: int
    accepted_false: int
    paper_accepted_true: int
    paper_accepted_false: int
    live_accepted_true: int
    live_accepted_false: int

    def to_dict(self) -> dict[str, Any]:
        ...

def build_tick_decision_audit_summary(rows: Iterable[dict[str, Any]]) -> TickDecisionAuditSummary:
    ...

def tick_decision_audit_markdown_lines(summary: TickDecisionAuditSummary, *, title: str='Live tick decision audit') -> list[str]:
    ...
