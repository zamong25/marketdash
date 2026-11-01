"""Acceptance test 1: One-file strategy add."""

@pytest.fixture
def temporary_strategy(tmp_path):
    """Write a synthetic strategy module into src/strategies/, yield, then remove."""
    ...

def test_register_strategy_decorator_exists():
    """Phase C precondition: src/strategies/registry.py with register_strategy decorator exists."""
    ...

def test_strategy_resolves_via_decorator_only(temporary_strategy):
    """Adding a strategy file with the decorator must make it resolvable."""
    ...

def test_no_loader_or_sidecar_edits_required(temporary_strategy):
    """Adding a strategy must NOT require touching strategy_loader, capability_registry, or emoji map."""
    ...
