"""Acceptance test 2: Strategy removal isolation."""

def test_strategies_module_imports_with_one_strategy_missing(tmp_path):
    """Simulate removing a strategy file. Other strategies still importable."""
    ...

def test_runner_starts_with_disabled_strategy_in_config(tmp_path, monkeypatch):
    """Mark one strategy disabled in config; runner builds with the rest cleanly."""
    ...
