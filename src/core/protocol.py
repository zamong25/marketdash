from __future__ import annotations

from typing import Protocol, runtime_checkable

from src.core.types import (
    MarketSnapshot,
    PortfolioState,
    SettlementResult,
    Signal,
)


@runtime_checkable
class Strategy(Protocol):
    """Every strategy implements this. Called every second by the runner.

    Required surface (enforced via ``isinstance``):
      - ``name: str`` — canonical identifier.
      - ``init(params: dict)`` — runtime-config injection.
      - ``warmup_ticks() -> int`` — minimum history before first ``on_tick``.
      - ``on_tick(snapshot, history, portfolio) -> Signal | None`` — main loop.

    See :class:`StrategyOptionalSurface` for the optional surface (dedup
    sets, signal-key metadata, settlement hook). Strategies opt into those
    by simply declaring the attribute / method; runners still probe via
    ``hasattr`` for backwards compatibility, but the Protocol now documents
    the contract that decoupling consumers from runners depends on.
    """

    name: str

    def init(self, params: dict[str, object]) -> None: ...

    def warmup_ticks(self) -> int: ...

    def on_tick(
        self,
        snapshot: MarketSnapshot,
        history: list[MarketSnapshot],
        portfolio: PortfolioState,
    ) -> Signal | None: ...


class StrategyOptionalSurface(Protocol):
    """Optional Strategy surface — opt-in.

    A strategy that maintains per-window dedup state, exposes signal
    metadata, or wants to react to settlement events declares one or more
    of these attributes / methods. Runners and replay engines treat them
    as optional via ``hasattr``.
    """

    SIGNAL_PARAM_KEYS: frozenset[str]
    STRATEGY_EMOJI: str

    traded_windows: set[str]
    evaluated_windows: set[str]

    def on_settlement(self, settlement: SettlementResult) -> None: ...
