"""Executable spec: a lane is scored and traded by the same object."""

def test_scoring_uses_the_registered_lane_object():
    """No second copy of the rules: the scorer resolves from the registry."""
    ...

def test_standing_ask_scorecard_at_the_measured_round_trip():
    ...

def test_missed_fills_are_charged():
    """An evaporated quote is a miss, never a free option."""
    ...

def test_slower_is_strictly_worse():
    """Speed is the lane's main sensitivity; keep it visible."""
    ...

def test_raising_the_edge_floor_trades_less():
    ...

def test_the_live_gate_survives_transcription_into_a_lane():
    """`fresh_dip` is the running probe's gate, so it must still be tradeable."""
    ...

def test_running_both_lanes_beats_either_alone():
    ...

def test_one_fill_per_window_regardless_of_how_many_lanes_want_it():
    """The 5-share venue minimum makes a second ticket unsendable at our size."""
    ...

def test_precedence_does_not_change_the_result_here():
    """Both lanes name the same price on all 20 shared windows."""
    ...
