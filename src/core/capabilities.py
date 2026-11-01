
class SnapshotSupportLevel(IntEnum):
    """How faithfully a snapshot provider can supply one field."""

@dataclass(frozen=True)
class SnapshotProviderCapabilities:
    """Field-level fidelity declaration for one snapshot provider."""
    provider_name: str
    field_levels: Mapping[str, SnapshotSupportLevel]
    field_notes: Mapping[str, str]
    may_degrade_on_fallback: bool
    exact_live_snapshot_replay: bool
    raw_event_replay: bool

    def level_for(self, field: str) -> SnapshotSupportLevel:
        ...

    def note_for(self, field: str) -> str:
        ...

@dataclass(frozen=True)
class StrategyCapabilityDescriptor:
    """Replay/runtime requirements for one strategy family."""
    strategy_name: str
    required_snapshot_fields: tuple[str, ...]
    minimum_snapshot_level: SnapshotSupportLevel
    execution_profile: str
    notes: tuple[str, ...]

    @property
    def required_futures_aux_fields(self) -> tuple[str, ...]:
        ...

    @property
    def depends_on_btc_anchor(self) -> bool:
        ...

@dataclass(frozen=True)
class StrategyCompatibilityIssue:
    field: str
    required_level: SnapshotSupportLevel
    actual_level: SnapshotSupportLevel
    note: str

@dataclass(frozen=True)
class StrategyCompatibilityReport:
    strategy_name: str
    provider_name: str
    compatible: bool
    issues: tuple[StrategyCompatibilityIssue, ...]
    warnings: tuple[str, ...]

    def summary_lines(self) -> list[str]:
        ...

def validate_strategy_snapshot_compatibility(strategy: StrategyCapabilityDescriptor, provider: SnapshotProviderCapabilities) -> StrategyCompatibilityReport:
    ...

@lru_cache(maxsize=None)
def infer_strategy_snapshot_fields_from_class_name(module_path: str, class_name: str) -> tuple[str, ...]:
    ...

@lru_cache(maxsize=None)
def infer_strategy_snapshot_fields_from_class(cls: type) -> tuple[str, ...]:
    ...

def _best_effort_source(cls: type) -> str:
    ...
