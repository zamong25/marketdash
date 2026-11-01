"""Logistic-regression inference for the contrarian_taker_fade strategy."""

@dataclass(frozen=True)
class LogisticTakerModel:
    """Standalone logistic model with standardized inputs."""
    features: tuple[str, ...]
    coef: tuple[float, ...]
    intercept: float
    scaler_mean: tuple[float, ...]
    scaler_scale: tuple[float, ...]

    @classmethod
    def from_json_file(cls, path: str | Path) -> 'LogisticTakerModel':
        ...

    def predict_posterior(self, features: TakerFlowFeatures) -> float:
        """Return P(token_0 wins) given current features."""
        ...

def _sigmoid(x: float) -> float:
    ...
