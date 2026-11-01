"""``/copy-engine`` — read-only copy-engine results surface for the dashboard."""

def _open() -> sqlite3.Connection:
    """Open a read-side connection, creating the schema if the DB is brand new."""
    ...

def _scorecard_value(raw: dict[str, Any], feature: str) -> float | None:
    """Read one feature value from a score_run ``raw`` payload (None if absent)."""
    ...

def _headline(raw: dict[str, Any]) -> dict[str, float | None]:
    """Pull the condition-6 headline features out of a raw scorecard payload."""
    ...

def _has_real_activity(raw: dict[str, Any]) -> bool:
    """True when the wallet's scorecard shows any real, non-zero behaviour."""
    ...

def _cluster_label(membership: Any, fallback: int | None) -> int | None:
    """Best hard-cluster label for a wallet from its membership payload."""
    ...

def _empty_meta() -> dict[str, Any]:
    """The ``meta`` block shared by list endpoints when no run exists."""
    ...

@router.get('/wallets')
def get_copy_engine_wallets(limit: int=Query(50, ge=1, le=500), offset: int=Query(0, ge=0, le=100000), include: str=Query('copyable')) -> dict:
    """Ranked profitable-wallet leaderboard for the 수익지갑 screen."""
    ...

@router.get('/wallet/{address}')
def get_copy_engine_wallet(address: str) -> dict:
    """Deep-dive for one wallet (지갑 딥다이브 screen)."""
    ...

@router.get('/clusters')
def get_copy_engine_clusters() -> dict:
    """Cluster summary for the 패턴 분석 screen."""
    ...

@router.get('/census-status')
def get_copy_engine_census_status() -> dict:
    """Latest census coverage for the 시장 발굴 screen."""
    ...

@router.get('/collector-status')
def get_trade_collector_status() -> dict:
    """실시간 거래 수집기 현황 — 수익지갑 화면 상단 카드용."""
    ...

@router.get('/live-leaderboard')
def get_live_leaderboard(types: str=Query(''), markets: str=Query(''), limit: int=Query(50, ge=1, le=200), offset: int=Query(0, ge=0), sort: str=Query('pnl'), include: str=Query('profit'), q: str=Query('')) -> dict:
    """실시간 집계 리더보드 — 손익/승률/베팅액/거래수순, 유형·시장 필터(콤마 구분 IN)."""
    ...

@router.get('/live-status')
def get_live_status() -> dict:
    """집계 깔때기 + 집계 데몬 상태 — 파이프라인 플로우(카운트다운·진행률) 화면용."""
    ...

def _read_census_artifact() -> dict[str, Any] | None:
    """Read the optional census coverage artifact, or None if absent/unreadable."""
    ...

def _mean_profile(addresses: list[str], score_rows: dict[str, dict[str, Any]]) -> dict[str, float]:
    """Mean raw-feature vector across the given members of one score run."""
    ...

def _cluster_label_map(conn: sqlite3.Connection, run_id: str) -> dict[int, dict[str, Any]]:
    """Plain-language label for every cluster in a run (keyed by cluster id)."""
    ...

def _diagnose(pnl_row: dict[str, Any] | None) -> dict[str, Any] | None:
    """Plain-language copyability verdict from a ``wallet_pnl`` row (None if absent)."""
    ...

def _realized_pnl(activity: list[dict[str, Any]], scorecard: dict[str, float]) -> float | None:
    """Best-effort realized pnl: scorecard ``pnl`` if present, else from activity."""
    ...
