"""Feature computation for contrarian_taker_fade."""

@dataclass(frozen=True)
class TakerFlowFeatures:
    """Exact feature column set required by the logistic model."""
    aggressive_buy_t0_count_30s: float
    whale_t0_buy_minus_sell_30s: float
    trade_count_ratio_t0: float
    cross_token_t0_buy_share: float
    ofi_buy_minus_sell_30s_t0: float

    def as_dict(self) -> dict[str, float]:
        ...

def _recent(events: Iterable[TakerEvent], now_ms: int, window_s: float) -> list[TakerEvent]:
    ...

def compute_features(events: Iterable[TakerEvent], now_ms: int, token_0: str, token_1: str, *, window_s: float=DEFAULT_FEATURE_WINDOW_S, whale_size_threshold: float=DEFAULT_WHALE_SIZE) -> TakerFlowFeatures:
    """Compute the 5 taker-flow features at ``now_ms`` with lookback ``window_s``."""
    ...
