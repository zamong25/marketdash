
@dataclass(frozen=True)
class MarketMetaMarket:
    slug: str
    condition_id: str
    up_token: str
    down_token: str
    closed: bool
    outcome_prices: tuple[float, float]

@dataclass(frozen=True)
class SettlementStatus:
    slug: str
    settled: bool
    outcome: str | None
    outcome_prices: tuple[float, float]
    condition_id: str

class MarketMetaClient:

    def __init__(self, base_url: str='https://market_meta-api.venue.com', rate_limit_seconds: float=0.2, timeout_seconds: float=10.0, retries: int=3, backoff_multiplier: float=2.0, backoff_max_seconds: float | None=None, user_agent: str='venue-btc-5min/1.0', latency_sink: Callable[[VenueLatencyRecord], None] | None=None) -> None:
        ...

    def _sleep_for_rate_limit(self) -> None:
        ...

    def _retry_delay_seconds(self, attempt: int, response: requests.Response | None=None) -> float:
        ...

    def _request_json(self, path: str, params: dict[str, Any] | None=None) -> Any:
        ...

    def _market_from_response(self, slug: str, payload: Any) -> MarketMetaMarket:
        ...

    def _emit_latency(self, *, start_wall_ms: int, start_monotonic: float, endpoint: str, success: bool, error: str, payload_key: str) -> None:
        """Record a completed call's RTT. Always updates ``last_latency_ms``;"""
        ...

    def get_market(self, slug: str) -> MarketMetaMarket:
        ...

    def list_markets(self, *, active: bool | None=None, closed: bool | None=None, limit: int=1000, offset: int=0) -> list[dict[str, Any]]:
        ...

    def list_events(self, *, active: bool | None=None, closed: bool | None=None, query: str | None=None, tag_id: int | str | None=None, related_tags: bool | None=None, order: str | None=None, ascending: bool | None=None, limit: int=40, offset: int=0, end_date_min: str | None=None, end_date_max: str | None=None, series_id: int | str | None=None) -> list[dict[str, Any]]:
        ...

    def get_market_by_slug(self, slug: str) -> dict[str, Any]:
        ...

    def get_event_by_slug(self, slug: str) -> dict[str, Any]:
        ...

    def get_event_by_id(self, event_id: str | int) -> dict[str, Any]:
        ...

    def public_search(self, query: str, *, limit_per_type: int=10, page: int=1, search_profiles: bool=False, optimized: bool=True) -> dict[str, Any]:
        ...

    def get_active_btc_5min_market(self, slug: str | None=None) -> MarketMetaMarket:
        ...

    def get_settlement_status(self, slug: str) -> SettlementStatus:
        ...
