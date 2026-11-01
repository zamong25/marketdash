"""``/quick-trade/copy-console`` — persistent wallet-copy console state."""

class CopyConsoleStateRequest(BaseModel):
    targets: list[dict[str, Any]]
    shadow_ledger: list[dict[str, Any]]
    dismissed_signals: list[str]

class CopyConsoleTargetsRequest(BaseModel):
    targets: list[dict[str, Any]]

class CopyConsoleLedgerRequest(BaseModel):
    entries: list[dict[str, Any]]

class CopyConsoleDismissedRequest(BaseModel):
    ids: list[str]

@router.get('/state')
def get_copy_console_state() -> dict[str, Any]:
    """Return operator-owned copy console state persisted on the backend."""
    ...

@router.post('/state')
def replace_copy_console_state(body: CopyConsoleStateRequest) -> dict[str, Any]:
    """Replace all persisted copy console state in one atomic write."""
    ...

@router.post('/targets')
def replace_copy_console_targets(body: CopyConsoleTargetsRequest) -> dict[str, Any]:
    """Replace persistent copy target configuration."""
    ...

@router.post('/shadow-ledger')
def replace_copy_console_shadow_ledger(body: CopyConsoleLedgerRequest) -> dict[str, Any]:
    """Replace persistent paper-copy ledger records."""
    ...

@router.post('/dismissed-signals')
def replace_copy_console_dismissed_signals(body: CopyConsoleDismissedRequest) -> dict[str, Any]:
    """Replace persistent hidden signal ids."""
    ...
