"""CLOB adapter factory — explicit version selection with fail-fast bootstrap."""

def _load_repo_env() -> None:
    """Load the repo ``.env`` before credentials are read."""
    ...

def _edge_execution_requested(version: object | None) -> bool:
    """Should orders leave through the the remote edge gateway rather than this process?"""
    ...

def _build_edge_client() -> CLOBClient:
    """The remote execution adapter, with a LOCAL adapter kept for books."""
    ...

def build_clob_client(version: object | None=None) -> CLOBClient:
    """Construct a CLOBClient adapter for the requested SDK version."""
    ...

def validate_clob_bootstrap(client: CLOBClient) -> None:
    """Make exactly one balance call to confirm the adapter can authenticate."""
    ...
