"""Pattern 1 — Confident directional entry into near-resolved markets."""

@dataclass(frozen=True)
class P1GateEvaluation:
    passed: bool
    gate: str
    reason: str
    elapsed_s: int
    side: SignalDirection | None
    expensive_price: float | None
    cheap_price: float | None
    btc_move_pct: float | None
    btc_velocity_pct: float | None
    btc_trend_pct: float | None
    confidence: float | None

    def to_audit(self) -> dict[str, Any]:
        ...

    def signal_info(self, *, vel_lookback_s: int, trend_lookback_s: int | None) -> dict[str, Any]:
        ...

def evaluate_p1_confident_direction_gate(snapshot: MarketSnapshot, history: list[MarketSnapshot], portfolio: PortfolioState, params: dict[str, Any], *, dedup_seen: bool=False) -> P1GateEvaluation:
    """Evaluate P1 gates once and return the first blocking gate."""
    ...

@register_strategy(name='p1_confident_direction', capabilities=('btc_price', 'btc_start'), aliases=('p1_confident_direction_live', 'p1_confident_direction_tight', 'p1_confident_direction_tight_live'), emoji='🎯')
class P1ConfidentDirectionStrategy:
    """Buy the confident side of an already-committed 5m market."""

    def __init__(self) -> None:
        ...

    def init(self, params: dict) -> None:
        ...

    def warmup_ticks(self) -> int:
        ...

    def on_tick(self, snapshot: MarketSnapshot, history: list[MarketSnapshot], portfolio: PortfolioState) -> Signal | None:
        ...

    def explain_no_signal(self, snapshot: MarketSnapshot, history: list[MarketSnapshot], portfolio: PortfolioState) -> dict[str, Any]:
        ...
