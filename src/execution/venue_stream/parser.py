"""Parse raw Venue user-channel WebSocket messages into"""

def parse_message(raw: str | bytes) -> TradeEvent | None:
    """Turn a single WebSocket frame into a :class:`TradeEvent` or"""
    ...

def _extract_fills(*, payload: dict[str, Any], taker_order_id: str, trade_id: str, status: TradeStatus, ts_ms: int) -> list[FillEvent]:
    ...

def _build_fill_id(trade_id: str, maker_order_id: str, ts_ms: int, idx: int) -> str:
    """Generate a unique dedup id for one fill slice."""
    ...

def _as_float(value: object) -> float:
    ...

def _as_int(value: object) -> int:
    ...
