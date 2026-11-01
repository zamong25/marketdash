
@dataclass(frozen=True)
class ValidationResult:
    ok: bool
    reason: str
    sanitized: dict[str, Any] | None

class TradeLogValidator:
    """Validate trade-log records before they are committed to disk."""

    def __init__(self, log_root: str | Path | None=None, *, tolerance: float=_TOLERANCE) -> None:
        ...

    def validate(self, record: dict[str, Any]) -> ValidationResult:
        ...

    def _ok(self, record: Mapping[str, Any]) -> ValidationResult:
        ...

    def _fail(self, reason: str) -> ValidationResult:
        ...

    def _validate_common_shape(self, record_type: str, record: Mapping[str, Any]) -> ValidationResult:
        ...

    def _validate_envelope(self, record: Mapping[str, Any], *, expected_mode: str | None) -> str | None:
        ...

    def _expected_mode(self, record_type: str) -> str | None:
        ...

    def _float_field(self, record: Mapping[str, Any], field: str) -> tuple[float | None, str | None]:
        ...

    def _nested_mapping(self, record: Mapping[str, Any], field: str) -> Mapping[str, Any] | None:
        ...

    def _decimal_field(self, record: Mapping[str, Any], field: str) -> tuple[Decimal | None, str | None]:
        ...

    def _approx_equal(self, left: float, right: float) -> bool:
        ...

    def _validate_numeric_fields(self, record: Mapping[str, Any], fields: list[str]) -> str | None:
        ...

    def _validate_required_fields(self, record: Mapping[str, Any], fields: list[str]) -> str | None:
        ...

    def _validate_paper_record(self, record_type: str, record: Mapping[str, Any]) -> ValidationResult:
        ...

    def _validate_rejection(self, record: Mapping[str, Any], mode: str) -> ValidationResult:
        ...

    def _validate_live_buy(self, record: Mapping[str, Any]) -> ValidationResult:
        ...

    def _validate_live_settlement(self, record: Mapping[str, Any]) -> ValidationResult:
        ...

    def _validate_live_redemption_confirmation(self, record: Mapping[str, Any]) -> ValidationResult:
        ...

    def _validate_live_redemption_completed(self, record: Mapping[str, Any]) -> ValidationResult:
        ...

    def _find_matching_live_buy(self, record: Mapping[str, Any]) -> dict[str, Any] | None:
        ...
