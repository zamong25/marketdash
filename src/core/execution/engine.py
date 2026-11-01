
class ExecutionContext(Protocol):
    """Minimum runtime context consumed by execution engines."""
    strategy_name: str
    config_version: str
    mode: str
    paper_mode: str

@dataclass(frozen=True)
class ExecutionResult:
    engine_name: str
    status: ExecutionStatus
    order_id: str | None
    side: str
    requested_shares: float
    actual_shares: float
    cost_usd: float
    fill_price: float | None
    fee_usd: float
    latency_ms: int
    rejection_reason: str | None
    rejection_detail: str
    fill: Fill | None
    meta: dict[str, Any]

    @property
    def success(self) -> bool:
        ...

    @classmethod
    def from_fill(cls, *, engine_name: str, status: ExecutionStatus, requested_shares: float, fill: Fill, latency_ms: int, rejection_reason: str | None=None, rejection_detail: str='', meta: dict[str, Any] | None=None) -> 'ExecutionResult':
        ...

    @classmethod
    def rejected(cls, *, engine_name: str, side: str, requested_shares: float, latency_ms: int, rejection_reason: str, rejection_detail: str='', fill_price: float | None=None, meta: dict[str, Any] | None=None, order_id: str | None=None, fill: Fill | None=None) -> 'ExecutionResult':
        ...

class ExecutionEngine(Protocol):
    name: str

    def execute(self, *, order: Order, snapshot: MarketSnapshot, signal: Signal, ctx: ExecutionContext) -> ExecutionResult:
        ...
