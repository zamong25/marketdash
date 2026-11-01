"""Canonical outcome effect."""

def _raw_bucket_table(payload: dict[str, Any], key: str) -> dict[str, dict[str, Any]]:
    ...

def _eligible_bucket_prob(table: dict[str, dict[str, Any]], key: str, *, min_samples: int | None) -> float | None:
    ...

@dataclass
class CanonicalOutcomeEffect:
    name: ClassVar[str]
    spread_edges: tuple[float, float]
    ask_delta_edges: tuple[float, float, float]
    ask_delta_eligibility_bounds: tuple[float, float] | None
    signal_remaining_edges: tuple[int, int]
    global_prob: float
    joint_time_buckets: dict[str, dict[str, Any]]
    joint_buckets: dict[str, dict[str, Any]]
    pair_time_buckets: dict[str, dict[str, Any]]
    pair_buckets: dict[str, dict[str, Any]]
    signal_remaining_buckets: dict[str, dict[str, Any]]
    ask_delta_buckets: dict[str, dict[str, Any]]
    spread_buckets: dict[str, dict[str, Any]]
    joint_min_samples: int
    pair_min_samples: int
    joint_time_min_samples: int
    pair_time_min_samples: int
    signal_remaining_min_samples: int
    actionable_probability_floor: float
    actionable_sources: frozenset[str]
    runtime_source_probability_caps: dict[str, float]
    seed: int
    _rng: random.Random

    def __post_init__(self) -> None:
        ...

    @classmethod
    def from_path(cls, path: str | Path, seed: int=42) -> 'CanonicalOutcomeEffect':
        ...

    @classmethod
    def from_payload(cls, payload: dict[str, Any], seed: int=42) -> 'CanonicalOutcomeEffect':
        ...

    def _lookup_prob(self, *, spread: float, ask_delta: float, direction: str, signal_remaining_s: int | None) -> tuple[float, str]:
        ...

    def apply(self, context: 'FillContext', book: 'BookProvider') -> 'FillContext':
        ...
