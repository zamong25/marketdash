
def _side_name(direction: SignalDirection | str) -> str:
    ...

def directional_ask_from_top_of_book(*, best_bid: float | None, best_ask: float | None, direction: SignalDirection | str) -> float | None:
    """Return the traded-side ask implied by an UP-token top-of-book."""
    ...
