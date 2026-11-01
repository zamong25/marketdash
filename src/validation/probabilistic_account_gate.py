
def _quantile_edges(values: list[float]) -> tuple[float, float]:
    ...

def _bucket_three_way(value: float, edges: tuple[float, float], labels: tuple[str, str, str]) -> str:
    ...

def _stable_roll(*, base_seed: int, seed: int, slug: str, ts_s: int, direction: str) -> float:
    ...

@dataclass(frozen=True)
class AccountGateExample:
    strategy_family: str
    cash_ratio: float | None
    observation_age_s: float | None
    rejected: bool
    source_slug: str

@dataclass(frozen=True)
class AccountGateDecision:
    bucket: str
    probability: float
    roll: float
    rejected: bool

@dataclass
class ProbabilisticAccountGate:
    rejection_probs: dict[str, float]
    ratio_edges: tuple[float, float]
    age_edges: tuple[float, float]
    global_rejection_rate: float
    min_total_per_bucket: int
    seed: int

    @classmethod
    def from_examples(cls, examples: Sequence[AccountGateExample], *, min_total_per_bucket: int=5, seed: int=42) -> 'ProbabilisticAccountGate':
        ...

    @classmethod
    def from_path(cls, path: str | Path, *, seed: int=42) -> 'ProbabilisticAccountGate':
        ...

    @classmethod
    def from_payload(cls, payload: dict[str, Any], *, seed: int=42) -> 'ProbabilisticAccountGate':
        ...

    def bucket_for_features(self, *, strategy_family: str | None, cash_ratio: float | None, observation_age_s: float | None) -> str:
        ...

    def reject_probability(self, *, strategy_family: str | None, cash_ratio: float | None, observation_age_s: float | None) -> tuple[str, float]:
        ...

    def decide(self, *, strategy_family: str | None, cash_ratio: float | None, observation_age_s: float | None, seed: int, slug: str, ts_s: int, direction: str) -> AccountGateDecision:
        ...

def fit_probabilistic_account_gate(examples: Sequence[AccountGateExample], *, min_total_per_bucket: int=5) -> dict[str, Any]:
    ...
