
@dataclass
class BacktestExecutionEngine:
    fee_rate: float
    use_ask_for_entry: bool
    model_depth_slippage: bool
    name: str

    def execute(self, *, order: Order, snapshot: MarketSnapshot, signal: Signal, ctx) -> ExecutionResult:
        ...

    def entry_price(self, snapshot: MarketSnapshot, direction: str, shares: int) -> tuple[float, float]:
        ...
