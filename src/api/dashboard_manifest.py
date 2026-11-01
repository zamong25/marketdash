"""Structured dashboard surface definition."""

@dataclass(frozen=True)
class DashboardNavItem:
    anchor: str
    label: str
    active: bool

@dataclass(frozen=True)
class DashboardKpi:
    element_id: str
    label: str
    tone: str

@dataclass(frozen=True)
class DashboardFetchJob:
    label: str
    url: str
    renderer: str

def dashboard_manifest() -> dict[str, object]:
    ...
