"""Acceptance-test isolation for the wallet-analytics persistent cache (WP-13)."""

@pytest.fixture(autouse=True)
def _isolate_wallet_analytics_cache(tmp_path, monkeypatch):
    ...
