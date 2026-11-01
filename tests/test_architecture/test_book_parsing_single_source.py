"""Nobody re-derives which end of a raw book array is the touch."""

def _module_source(relative_path: str) -> tuple[ast.Module, str]:
    ...

def _canonical_imports(tree: ast.Module) -> set[str]:
    ...

def _indexed_book_sides(tree: ast.AST) -> list[str]:
    """Constant-index subscripts of a name called ``bids`` or ``asks``."""
    ...

def _constant_index(node: ast.expr) -> int | None:
    """``asks[-1]`` is a UnaryOp, not a Constant -- and it was the half we got right."""
    ...

@pytest.mark.parametrize('relative_path', RAW_WIRE_CONSUMERS)
def test_raw_wire_consumer_never_indexes_a_book_side(relative_path: str) -> None:
    ...

@pytest.mark.parametrize('relative_path', RAW_WIRE_CONSUMERS)
def test_raw_wire_consumer_routes_through_the_canonical_parser(relative_path: str) -> None:
    ...

def test_the_canonical_parser_selects_by_price_not_by_index() -> None:
    """Sanity: the exemption is real, so the guard above is not vacuous."""
    ...

def test_guard_detects_the_original_defect() -> None:
    """The guard must fail on the code that actually shipped."""
    ...
