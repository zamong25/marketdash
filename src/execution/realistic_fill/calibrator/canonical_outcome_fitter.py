"""Fit the ``canonical_outcome.json`` hidden-zero table."""

def _base_feature_tuple(record: PairedFillRecord, *, spread_edges: tuple[float, float], ask_delta_edges: tuple[float, float, float], ask_delta_eligibility_bounds: tuple[float, float] | None) -> tuple[str, str, str] | None:
    ...

def _signal_remaining_label(record: PairedFillRecord, *, signal_remaining_edges: tuple[int, int]) -> str | None:
    ...

def _bucket_entry(*, confirmed: int, dropped: int, min_samples: int | None, fallback_prob: float, prior_samples: float, source: str, fallback_source: str) -> dict:
    ...

def fit_canonical_outcome(filled_records: Sequence[PairedFillRecord], rejected_records: Sequence[PairedFillRecord], *, spread_edges: tuple[float, float]=DEFAULT_SPREAD_EDGES, ask_delta_edges: tuple[float, float, float]=DEFAULT_ASK_DELTA_EDGES, ask_delta_eligibility_bounds: tuple[float, float] | None=DEFAULT_ASK_DELTA_ELIGIBILITY_BOUNDS, signal_remaining_edges: tuple[int, int]=DEFAULT_SIGNAL_REMAINING_EDGES, min_joint_samples: int=4, min_pair_samples: int=6, min_joint_time_samples: int=3, min_pair_time_samples: int=4, min_signal_remaining_samples: int=8, joint_time_prior_samples: float=10.0, joint_prior_samples: float=12.0, pair_time_prior_samples: float=14.0, pair_prior_samples: float=16.0, signal_remaining_prior_samples: float=20.0, marginal_prior_samples: float=24.0, actionable_probability_floor: float=0.3, positive_rejection_reasons: tuple[str, ...]=('fak_zero_fill',), generated_at_utc: str | None=None) -> dict:
    """Fit ``p(canonical_zero | book state, signal timing)``."""
    ...
