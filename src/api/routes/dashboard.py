"""React dashboard serving routes and read-only dashboard contracts."""

@router.get('/dashboard', include_in_schema=False)
def dashboard() -> FileResponse:
    """Serve the built React dashboard."""
    ...

@router.get('/dashboard/manifest')
def dashboard_manifest_endpoint() -> dict[str, object]:
    """Return the dashboard UI contract consumed by the React shell."""
    ...

@router.get('/dashboard/status')
def dashboard_status_endpoint() -> dict[str, object]:
    """Return the active dashboard serving mode without placing orders."""
    ...

@router.get('/dashboard/react', include_in_schema=False)
def react_dashboard() -> FileResponse:
    """Serve the built React dashboard."""
    ...

@router.get('/dashboard/react/{path:path}', include_in_schema=False)
def react_dashboard_spa(path: str) -> FileResponse:
    """Serve React dashboard assets or fall back to the SPA index."""
    ...

@router.get('/assets/{path:path}', include_in_schema=False)
def react_dashboard_root_asset(path: str) -> FileResponse:
    """Serve Vite production assets referenced by the built React index."""
    ...

def _react_dashboard_index() -> FileResponse:
    ...

def _react_dashboard_build_available() -> bool:
    ...

def _react_dashboard_index_path() -> Path:
    ...

def _react_dashboard_asset(path: str) -> FileResponse:
    ...
