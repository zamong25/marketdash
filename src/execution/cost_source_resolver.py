"""Cost-source resolver for live executor fills."""

class CostSource:
    """Canonical cost-source tag values."""
    BUY_SOURCES_RANKED: tuple[str, ...]

@dataclass(frozen=True)
class CostResolution:
    """Result of resolving a fill's cash accounting."""
    cost_usd: float
    fill_price: float
    fee: float
    cost_source: str

def _result_number(result: Any, *field_names: str) -> float | None:
    """Return the first positive float found across ``field_names`` on ``result``."""
    ...

def _estimated_fee(*, price: float, shares: float, fee_rate: float) -> float:
    """the venue's fee formula: ``rate × price × (1 - price) × shares``."""
    ...

def resolve_buy_cost(result: Any, *, usdc_delta: float, shares_filled: float, ask_price_at_order: float, price_hint: float, fee_rate: float, ws_bridge_price: float | None=None) -> CostResolution:
    """Resolve ``(cost_usd, fill_price, fee, cost_source)`` for a BUY fill."""
    ...

def resolve_sell_proceeds(result: Any, *, usdc_delta: float, shares_filled: float, price_hint: float, fee_rate: float) -> CostResolution:
    """Resolve ``(proceeds_usd, fill_price, fee, cost_source)`` for a SELL fill."""
    ...

def _derive_fee_from_reported_cost(*, reported_cost: float, shares_filled: float, result: Any, fee_rate: float) -> float:
    """Prefer adapter-reported fee; fall back to (cost − notional); lastly formula."""
    ...
