"""Compatibility shim for strategy capability lookup."""

class UnsupportedSimulationCapabilityError(RuntimeError):
    """Raised when a strategy/runtime pairing is known to be unsupported."""

def strategy_capabilities_for_strategy(strategy_key: str) -> StrategyCapabilityDescriptor:
    ...
