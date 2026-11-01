
@dataclass
class RealisticSimExecutionEngine:
    book_provider: Any
    order_snapshot_provider: Any | None
    fee_rate: float
    fill_model: FillModel | None
    latency_model: Any | None
    max_price: float
    name: str

    def execute(self, *, order: Order, snapshot: MarketSnapshot, signal: Signal, ctx) -> ExecutionResult:
        ...

    def _signal_ts_ms(self, signal: Signal, snapshot: MarketSnapshot) -> int:
        ...

    def _execute_fill_model(self, *, order: Order, snapshot: MarketSnapshot, signal: Signal, ctx) -> ExecutionResult:
        ...

    def _execute_historical(self, *, order: Order, snapshot: MarketSnapshot, signal: Signal) -> ExecutionResult:
        ...
