
@dataclass(frozen=True)
class AdapterErrorDetail:
    raw: str
    kind: str
    family: str
    families: tuple[str, ...]
    attempted_order_types: tuple[str, ...]
    limit_fallback_skipped: bool
    available_balance_micro: int | None
    required_order_amount_micro: int | None
    balance_coverage_ratio: float | None

def _segment_family(detail: str) -> str:
    ...

def _primary_kind(detail: str) -> str:
    ...

def _decorate_kind(base_kind: str, *, normalized: str, limit_fallback_skipped: bool) -> str:
    ...

def classify_adapter_error_detail(detail: str | None) -> AdapterErrorDetail:
    ...
