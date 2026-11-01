"""Load live fills + enrich them into ``PairedFillRecord`` objects."""

@dataclass(frozen=True)
class PairedFillRecord:
    """One live fill, optionally augmented with future-horizon mids and"""
    fill_ts_ms: int
    signal_ts_ms: int
    strategy: str
    window_slug: str
    direction: str
    token_id: str
    signal_price: float
    fill_price: float
    requested_shares: float
    filled_shares: float
    fill_status: str
    cost_source: str
    rejection_reason: str | None
    rejection_detail: str | None
    fak_returned_shares: float | None
    bridge_returned_shares: float | None
    use_fast_path: bool
    strategy_family: str | None
    order_price_ref: float | None
    api_error_kind: str | None
    api_error_family: str | None
    api_error_balance_coverage_ratio: float | None
    api_error_limit_fallback_skipped: bool
    api_error_attempted_order_types: tuple[str, ...]
    ask_price_at_order: float | None
    ask_depth_at_order: float | None
    snapshot_best_ask: float | None
    snapshot_best_bid: float | None
    snapshot_down_best_ask: float | None
    snapshot_down_best_bid: float | None
    ask_depth_top1: float | None
    ask_depth_top5: float | None
    horizon_mid_5s: float | None
    horizon_mid_30s: float | None
    horizon_mid_60s: float | None
    book_context: str | None

    @property
    def preferred_ask_depth(self) -> float | None:
        """Best available "book depth at order send" estimate, preferring"""
        ...

    @property
    def partial_fill_depth_proxy(self) -> float | None:
        """Depth proxy used by the partial-fill calibration/effect."""
        ...

    @property
    def apparent_fill_shares(self) -> float:
        """Best-effort apparent fill count before canonical confirmation."""
        ...

    @property
    def snapshot_ask_for_direction(self) -> float | None:
        """Direction-aware ask reconstructed from ``snapshot_context``."""
        ...

    @property
    def snapshot_spread(self) -> float | None:
        ...

    @property
    def effective_order_price_ref(self) -> float | None:
        ...

    @property
    def order_budget_proxy_usd(self) -> float | None:
        ...

    @property
    def ask_minus_snapshot_ask_for_direction(self) -> float | None:
        ...

    @property
    def signal_remaining_s(self) -> int | None:
        ...

    @property
    def adverse_shift_5s(self) -> float | None:
        """``max(0, fill - mid@fill_ts+5s)`` or ``None`` if horizon is"""
        ...

def _record_from_live_buy(raw: dict) -> PairedFillRecord | None:
    """Parse one ``live_buy`` dict into a record, returning ``None`` when"""
    ...

def _iter_jsonl(path: Path) -> Iterable[dict]:
    ...

def load_rejected_records(paths: Sequence[Path]) -> list[PairedFillRecord]:
    """Load ``live_rejected`` records as PairedFillRecords for the"""
    ...

def _record_from_live_rejected(raw: dict) -> PairedFillRecord | None:
    ...

def resolve_token_ids(records: Sequence[PairedFillRecord], token_map: dict[str, tuple[str, str]]) -> list[PairedFillRecord]:
    """Fill in missing or truncated ``token_id`` fields from ``(slug -> (up, down))``"""
    ...

def load_paired_records(paths: Sequence[Path], *, strict: bool=True) -> list[PairedFillRecord]:
    """Load trusted live fills from the given jsonl trade logs."""
    ...

def _load_token_depth(pm_events_root: Path, day: str, token_id: str) -> pd.DataFrame | None:
    """Return a sorted DataFrame of ``(ts_ms, bid_prices, bid_sizes,"""
    ...

def _load_day_depth_by_token(pm_events_root: Path, day: str, token_ids: Iterable[str]) -> dict[str, pd.DataFrame]:
    """Load one UTC day's pm_depth files once, then split by token."""
    ...

def _resolve_record_token_id(depth_book: PmEventsBook, token_mapper: TokenMapper, record: PairedFillRecord) -> str | None:
    ...

def _looks_like_full_token_id(token_id: str) -> bool:
    """Return True for canonical Venue CTF token ids."""
    ...

def _depth_at(depth_df: pd.DataFrame, ts_ms: int) -> dict | None:
    ...

def _mid_from_depth(book: dict | None) -> float | None:
    ...

def _top1_ask_size(book: dict | None) -> float | None:
    ...

def _topN_ask_size(book: dict | None, n: int=5) -> float | None:
    ...

def _book_context_has_usable_depth(book: dict | None, ts_ms: int) -> bool:
    ...

def _has_historical_book_context(processed_depth: dict[str, pd.DataFrame], raw_depth: dict[str, pd.DataFrame], *, token_id: str, ts_ms: int) -> bool:
    ...

def enrich_with_depth(records: Sequence[PairedFillRecord], *, pm_events_root: Path, horizons_s: Sequence[int]=(5, 30, 60), resolve_token_hints: bool=True) -> list[PairedFillRecord]:
    """Attach depth + horizon mid fields. Unknown slugs / missing files"""
    ...

def enrich_with_book_context(records: Sequence[PairedFillRecord], *, processed_depth_root: Path, raw_depth_root: Path, ts_attr: str='fill_ts_ms', resolve_token_hints: bool=True) -> list[PairedFillRecord]:
    """Label each record with the runtime book provenance it would have seen."""
    ...
