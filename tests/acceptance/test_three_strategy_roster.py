"""Acceptance test 3: 3 active strategies actually run."""

def test_three_canonical_strategies_resolvable():
    """Phase C precondition: registry knows all 3 active strategy names."""
    ...

def test_three_strategies_instantiate():
    """Each of the 3 active strategies can be loaded + initialized via the registry."""
    ...

def test_three_strategies_reach_on_tick(tmp_path, monkeypatch):
    """Runner builds with synthetic stubs of the 3 strategies, each receives one tick."""
    ...
