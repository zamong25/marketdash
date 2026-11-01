"""Startup-time twin configuration equality checks."""

class TwinConfigDivergenceError(Exception):
    """Raised when two sides of a twin pair disagree on a signal param,"""

def signal_param_keys_for_strategy(strategy_key: str) -> set[str]:
    """Resolve a strategy's declared signal params."""
    ...

def validate_twin_configs(paper: StrategyInstanceConfig, live: StrategyInstanceConfig, signal_keys: set[str]) -> None:
    """Assert paper and live twin configs agree on every signal param."""
    ...
