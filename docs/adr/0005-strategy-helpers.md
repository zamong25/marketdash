# ADR 0005: Strategy Helper Extraction

## Status

Accepted

## Context

Strategy implementations repeated the same guard and data-selection
logic: per-window dedup, inclusive scan windows, daily drawdown stops,
same-window history filtering, BTC move/velocity calculation, and
Venue expensive/cheap side selection. Small fixes then required
multi-file edits and made behavior drift easy.

Phase 6 extracts those primitives into `src/strategies/helpers/` while
keeping `src/core/protocol.py` and `src/core/types.py` unchanged.

## Decision

Add focused helper modules:

- `dedup.py` for `WindowDedupTracker`.
- `gates.py` for scan-window, price-band, and daily drawdown predicates.
- `history.py` for same-window filtering and offset lookup.
- `btc.py` for BTC move, velocity, and direction alignment.
- `book.py` for Venue side selection.

Existing `pm_microstructure.py` remains for current-regime helpers with
fraction-based BTC lead semantics and live-fill order info forwarding.

Strategies keep their public state shape where tests or callers use it
directly. For example, `self.traded_windows` remains the backing set,
while strategy code calls `self._dedup.seen()` and `self._dedup.mark()`.

## Consequences

New strategy code should import these helpers instead of duplicating
their logic. Helper tests cover edge inclusivity, invalid BTC prices,
offset lookup semantics, price-band aliases, and drawdown boundaries.

BTC helper units are explicit:

- `btc_move_pct` and `btc_velocity_pct` return percentage points.
- `pm_microstructure.signed_btc_lead_pct` returns signed fractions for
  strategies whose thresholds are configured as fractions.
