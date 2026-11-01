
@dataclass(frozen=True)
class ImportFailure:
    module: str
    exc_type: str
    message: str

@dataclass(frozen=True)
class ImportProbeResult:
    failures: tuple[ImportFailure, ...]
    stdout: str
    stderr: str

    @property
    def ok(self) -> bool:
        ...

def _ensure_package_initializers(root: Path, relative_path: str) -> None:
    ...

@pytest.fixture
def architecture_repo_root() -> Path:
    ...

@pytest.fixture
def synthetic_repo_builder(tmp_path):
    ...

@pytest.fixture
def copied_src_tree(tmp_path):
    ...

@pytest.fixture
def import_probe():
    ...
