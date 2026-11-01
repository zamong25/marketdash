
def _legacy_registry_view() -> dict[str, str]:
    """Build a STRATEGY_REGISTRY-shaped dict from the registry."""
    ...

def __getattr__(attr: str) -> Any:
    ...

def resolve_strategy_family_name(config_name: str, registry: dict[str, str] | None=None) -> str:
    """Resolve a strategy/instance name to its family bucket for calibration."""
    ...

def load_strategy(name: str, params: dict) -> Strategy:
    ...

def use_fast_path_enabled(settings: dict[str, Any], params: dict[str, Any]) -> bool:
    ...

def get_strategy_capabilities(name: str) -> StrategyCapabilityDescriptor:
    ...
