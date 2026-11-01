"""Era-aware read models built from already-loaded ledger rows."""

def _timestamp(value: Any) -> float | None:
    ...

def _utc(ts: float | None) -> str | None:
    ...

def _row_ts(row: dict[str, Any], fields: Sequence[str]) -> float | None:
    ...

def _metadata(interval: dict[str, Any] | None, *, row_intervals: Iterable[dict[str, Any]]=(), prior: bool=False) -> dict[str, Any]:
    ...

def _book_stats(rows: list[dict[str, Any]], metadata: dict[str, Any]) -> dict[str, Any]:
    ...

def split_book_rows(rows: Iterable[dict[str, Any]], *, now_ts: float) -> dict[str, dict[str, Any]]:
    """Split settled simulation rows by their signal/open era."""
    ...

def _generation_key(interval: dict[str, Any] | None) -> str:
    """Roster-generation identity = the cohort sha256."""
    ...

def _generation_prefix(interval: dict[str, Any] | None) -> str:
    """Cohort-label prefix before the source suffix (ghost detection only)."""
    ...

def _generation_wallet_count(spans: list[dict[str, Any]]) -> int | None:
    """First finite wallet count across a generation's intervals, if any."""
    ...

def book_generations(rows: Iterable[dict[str, Any]], *, now_ts: float) -> list[dict[str, Any]]:
    """Group settled book rows by roster generation (the cohort sha256)."""
    ...

def _validation_partition(rows: list[dict[str, Any]], *, now_ts: float) -> tuple[list[dict[str, Any]], list[dict[str, Any]], dict[str, Any], list[dict[str, Any]]]:
    ...

def _real_stats(metrics: dict[str, Any], metadata: dict[str, Any]) -> dict[str, Any]:
    ...

def split_validation_results(rows: list[dict[str, Any]], *, now_ts: float) -> dict[str, dict[str, Any]]:
    """Return current/prior/total real-copy accounting without changing math."""
    ...

def split_validation_results_by_wallet(rows: list[dict[str, Any]], *, now_ts: float) -> tuple[dict[str, dict[str, Any]], dict[str, dict[str, Any]]]:
    """Return per-wallet current/prior metrics plus the overall split."""
    ...

def era_span(split: dict[str, dict[str, Any]]) -> dict[str, Any]:
    """Describe which eras a displayed sample covers, without altering it."""
    ...
