
@dataclass(frozen=True)
class StrategySupportRow:
    config_name: str
    strategy_name: str | None
    status: StrategySupportStatus
    resolution: str
    issues: tuple[str, ...]
    warnings: tuple[str, ...]
    notes: tuple[str, ...]

    def to_dict(self) -> dict[str, object]:
        ...

def _registry_keys(override: Mapping[str, str] | None) -> tuple[str, ...]:
    ...

def resolve_strategy_family(config_name: str, registry: Mapping[str, str] | None=None) -> tuple[str | None, str]:
    ...

def classify_strategy_support(config_name: str, provider: SnapshotProviderCapabilities, registry: Mapping[str, str] | None=None) -> StrategySupportRow:
    ...

def build_strategy_support_rows(config_names: Iterable[str], provider: SnapshotProviderCapabilities, registry: Mapping[str, str] | None=None) -> list[StrategySupportRow]:
    ...

def strategy_support_markdown_lines(rows: Iterable[StrategySupportRow], *, provider_name: str) -> list[str]:
    ...
