"""The fleet's Dublin hand: sign, post, cancel — and nothing else."""

def http_status_in(error: str | None) -> int | None:
    """The HTTP status carried inside a stringified SDK exception, if any."""
    ...

def order_failure_outcome(error: str | None) -> str:
    """Did the venue REFUSE this order, or do we simply not know?"""
    ...

class AdapterReadTimeout(CLOBNetworkError):
    """A read did not answer inside the gateway's budget."""

class RateGate:
    """One token bucket, burst 1, shared by every caller of this process."""

    def __init__(self, min_interval_s: float) -> None:
        ...

    def acquire(self) -> float:
        """Block until this caller's slot. Returns the milliseconds waited."""
        ...

class IntentRing:
    """Recent ``(client, intent_id)`` pairs, so a stutter is not a second bet."""

    def __init__(self, ttl_s: float=DEFAULT_INTENT_TTL_S) -> None:
        ...

    def claim(self, client: str, intent_id: str, now: float | None=None) -> bool:
        """True when this pair is NEW (and now remembered); False on a repeat."""
        ...

@dataclass
class GatewayState:
    """Everything the app keeps between requests. No position state here."""
    repo_root: Path
    gate: RateGate
    heartbeat_interval_s: float
    started_at: float
    pid: int
    read_budget_s: float
    requests: int
    orders_posted: int
    cancels: int
    last_warm: dict[str, Any] | None
    last_beat_ts: float
    last_adapter_ok_ts: float
    last_adapter_error_ts: float
    last_adapter_failed: bool
    lock: threading.Lock

    @property
    def ledger_path(self) -> Path:
        ...

    @property
    def heartbeat_path(self) -> Path:
        ...

    @property
    def kill_path(self) -> Path:
        ...

    def adapter_ok(self) -> None:
        ...

    def adapter_failed(self) -> None:
        ...

def killed(state: GatewayState) -> bool:
    """Read the kill file EVERY time."""
    ...

def adapter_looks_dead(state: GatewayState, now: float | None=None) -> bool:
    """Is the heartbeat entitled to claim this gateway is a working hand?"""
    ...

def beat(state: GatewayState) -> bool:
    """Write the heartbeat file unconditionally. Returns whether it landed."""
    ...

def maybe_beat(state: GatewayState) -> bool:
    """Beat only if this process still deserves to look alive."""
    ...

def ledger_write(state: GatewayState, row: dict[str, Any]) -> None:
    """Append one transport row. Never raises, for the same reason as `beat`."""
    ...

async def json_body(request: Request) -> Any:
    """Read + parse the body in the event loop so the HANDLER can be sync."""
    ...

def _order_from_payload(raw: Any) -> OrderRequest:
    ...

def _jsonable(value: Any) -> Any:
    """Whatever the SDK handed back, as something that survives the wire."""
    ...

def _result_payload(result: OrderResult) -> dict[str, Any]:
    ...

def _summarise(results: Iterable[dict[str, Any]]) -> dict[str, Any]:
    ...

def _tag(body: Any) -> tuple[str, str]:
    """``(client, intent_id)`` from a request body, both always strings."""
    ...

def _error_class_name(exc: Exception) -> str:
    """The class name the FAR END should reconstruct."""
    ...

def _error_response(exc: Exception, status: int=502) -> JSONResponse:
    """Venue/adapter failure as a body the remote adapter can re-raise by class."""
    ...

def build_app(adapter: Any, repo_root: Path | str, *, min_order_interval_s: float=DEFAULT_MIN_ORDER_INTERVAL_S, heartbeat_interval_s: float=DEFAULT_HEARTBEAT_INTERVAL_S, read_budget_s: float=DEFAULT_READ_BUDGET_S, auth_token: str | None=None, intent_ttl_s: float=DEFAULT_INTENT_TTL_S) -> FastAPI:
    """Build the gateway around one already-constructed CLOB adapter."""
    ...
