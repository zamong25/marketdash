
@dataclass(frozen=True)
class AdapterOrderErrorDetail:
    raw_detail: str
    kind: AdapterErrorKind
    limit_mode: AdapterLimitMode
    balance_usd: float | None
    order_amount_usd: float | None
    status_code: int | None

def parse_adapter_order_error_detail(detail: str | None) -> AdapterOrderErrorDetail:
    ...
