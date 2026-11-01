
@dataclass(frozen=True)
class GeneralConfig:
    execution_mode: ExecutionMode
    tick_interval_seconds: int
    max_staleness_seconds: int
    log_level: str

@dataclass(frozen=True)
class CollectorConfig:
    btc_ws_url: str
    force_order_ws_url: str
    oi_poll_interval: int
    market_meta_poll_interval: int

@dataclass(frozen=True)
class ExecutionConfig:
    max_total_exposure_usd: float
    max_single_position_usd: float
    max_daily_loss_usd: float
    min_order_shares: int
    redemption_poll_interval: int
    balance_cache_refresh_s: float
    balance_cache_max_age_s: float
    fee_rate: float
    kill_switch_file: Path

@dataclass(frozen=True)
class TelegramConfig:
    enabled: bool

@dataclass(frozen=True)
class StrategyInstanceConfig:
    name: str
    strategy: str
    config_path: Path
    params: dict[str, Any]
    settings: dict[str, Any]

@dataclass(frozen=True)
class TwinInstanceConfig:
    name: str
    strategy: str
    paper_config: StrategyInstanceConfig
    live_config: StrategyInstanceConfig

@dataclass(frozen=True)
class AppConfig:
    root: Path
    general: GeneralConfig
    collector: CollectorConfig
    execution: ExecutionConfig
    telegram: TelegramConfig
    strategies: list[StrategyInstanceConfig]
    twins: list[TwinInstanceConfig]

def _read_toml(path: Path) -> dict[str, Any]:
    ...

def _resolve(path: str | Path, base_dir: Path) -> Path:
    ...

def _execution_mode(value: str | ExecutionMode) -> ExecutionMode:
    ...

def load_strategy_config(path: str | Path, base_dir: str | Path | None=None) -> dict[str, Any]:
    ...

def _load_strategy_instance(*, name: str, strategy: str, strategy_path: Path) -> StrategyInstanceConfig:
    ...

def _require_field(item: dict[str, Any], field: str, *, label: str) -> Any:
    ...

def load_app_config(path: str | Path='config/default.toml', execution_mode: ExecutionMode | None=None) -> AppConfig:
    ...
