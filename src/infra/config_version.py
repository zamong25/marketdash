"""Compute a stable hash representing a strategy instance's config state."""

def _canonical_params(params: dict[str, Any]) -> str:
    """Serialize params deterministically so equal dicts hash identically."""
    ...

def _strategy_source(strategy_key: str) -> str:
    """Return the source file content of the strategy class; empty string on"""
    ...

def compute_strategy_hash(*, strategy_key: str, runtime_name: str, params: dict[str, Any]) -> str:
    """Compute a deterministic 12-char hex hash for a strategy instance state."""
    ...

def compute_from_instance_config(instance) -> str:
    """Convenience wrapper for ``StrategyInstanceConfig``."""
    ...
