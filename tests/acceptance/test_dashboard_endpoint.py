"""Acceptance test 4: Dashboard endpoint live."""

def test_api_module_exists():
    """Phase E precondition: src/api/server.py exists."""
    ...

def test_api_does_not_import_execution_directly():
    """Boundary: src/api/ files cannot import from src.execution.*"""
    ...

def test_dashboard_endpoint_returns_json():
    """Hit /runtime/status (or equivalent) and verify JSON response."""
    ...
