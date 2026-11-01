"""Query the :mod:`src.infra.config_version_log` history."""

@dataclass(frozen=True)
class ConfigVersion:
    """One row of ``runs/config_versions.jsonl``."""
    version_hash: str
    strategy_name: str
    strategy_class: str
    logged_at: str
    params_snapshot: dict

@dataclass(frozen=True)
class ReplayBatch:
    """A group of slugs to replay under one historical params snapshot."""
    version_hash: str | None
    params_snapshot: dict
    slugs: list[str]
    source: str

@dataclass(frozen=True)
class ReplayTimelineEntry:
    """One activation point in the historical config timeline."""
    active_from_ts: int
    params_snapshot: dict
    version_hash: str | None
    source: str

def load_config_versions(path: Path) -> dict[str, ConfigVersion]:
    """Parse the config-versions log into a hash → entry map."""
    ...

def load_config_version_entries(path: Path) -> list[ConfigVersion]:
    """Parse the config-version log into an ordered full timeline."""
    ...

def extract_slug_to_hash_from_trade_log(trade_log_paths: Sequence[Path], *, record_types: frozenset[str]=frozenset({'live_buy', 'live_rejected'})) -> dict[str, str]:
    """For each slug seen in these logs, return its ``config_version``."""
    ...

def build_config_replay_batches(*, day_slugs: Sequence[str], trade_log_paths: Sequence[Path], config_log_path: Path, fallback_params: dict) -> list[ReplayBatch]:
    """Group ``day_slugs`` by the live-recorded config version."""
    ...

def _slug_start_ts(slug: str) -> int:
    ...

def _logged_at_ts(value: str) -> int | None:
    ...

def build_config_replay_timeline(*, day_slugs: Sequence[str], trade_log_paths: Sequence[Path], config_log_path: Path, fallback_params: dict) -> list[ReplayTimelineEntry]:
    """Build a per-runtime params timeline for the requested day slugs."""
    ...

def _iter_jsonl(path: Path) -> Iterable[dict]:
    """Internal helper — tolerant of blank / malformed lines."""
    ...
