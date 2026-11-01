"""API error effect — calibrated API rejection model."""

def _as_list(snapshot, name: str) -> list:
    """Read ``name`` from a book snapshot."""
    ...

def _classify_price_shift(shift: float, edges: tuple[float, float]) -> str:
    ...

def _classify_depth(depth: float, edges: tuple[float, float]) -> str:
    ...

def _classify_three_way(value: float, edges: tuple[float, float], labels: tuple[str, str, str]) -> str:
    ...

def _detect_schema(payload: dict[str, Any], *, bucket_keys: tuple[str, ...]) -> SchemaName:
    ...

def _reason_family_from_kind(kind: str | None) -> str | None:
    ...

@dataclass
class ApiErrorEffect:
    name: ClassVar[str]
    schema: SchemaName
    rejection_probs: dict[str, float]
    spread_edges: tuple[float, float]
    signal_remaining_edges: tuple[int, int]
    price_shift_edges: tuple[float, float]
    depth_edges: tuple[float, float]
    requested_shares_edges: tuple[float, float]
    order_budget_edges: tuple[float, float]
    global_rejection_rate: float
    reason_probs: dict[str, dict[str, float]]
    global_reason_probs: dict[str, float]
    reason_result_reasons: dict[str, str]
    terminal_rejection_reason: str
    reasoned_order_axis: str
    seed: int

    @classmethod
    def from_path(cls, path: str | Path, seed: int=42) -> 'ApiErrorEffect':
        ...

    @classmethod
    def from_payload(cls, payload: dict[str, Any], seed: int=42) -> 'ApiErrorEffect':
        ...

    def _regime_bucket(self, context: 'FillContext') -> str | None:
        ...

    def _reasoned_regime_bucket(self, context: 'FillContext') -> str | None:
        ...

    def _legacy_bucket(self, context: 'FillContext', book: 'BookProvider') -> str | None:
        ...

    def apply(self, context: 'FillContext', book: 'BookProvider') -> 'FillContext':
        ...
