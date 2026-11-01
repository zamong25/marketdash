
@dataclass(frozen=True)
class ImportReference:
    module: str | None
    names: tuple[str, ...]
    level: int
    lineno: int
    kind: str

def get_module_layer(module_path: str) -> int:
    ...

def get_imports_from_file(filepath: Path) -> list[ImportReference]:
    ...

def module_path_from_file(filepath: Path, repo_root: Path=REPO_ROOT) -> str:
    ...

def module_exists_in_tree(module_path: str, repo_root: Path=REPO_ROOT) -> bool:
    ...

def module_package(module_path: str, filepath: Path) -> str:
    ...

def resolve_imported_modules(importing_module: str, filepath: Path, reference: ImportReference, repo_root: Path=REPO_ROOT) -> list[str]:
    ...

def iter_python_files(repo_root: Path=REPO_ROOT):
    ...

def collect_layer_violations(repo_root: Path=REPO_ROOT) -> list[str]:
    ...

def collect_l1_core_dependency_violations(repo_root: Path=REPO_ROOT) -> list[str]:
    ...

def test_layer_map_declares_all_plan_layers() -> None:
    ...

def test_layer_violation_detector_catches_synthetic_import(synthetic_repo_builder) -> None:
    ...

def test_l1_ports_rule_catches_synthetic_violation(synthetic_repo_builder) -> None:
    ...

def test_no_layer_imports_above() -> None:
    ...

def test_l1_adapters_only_import_core_ports() -> None:
    ...
