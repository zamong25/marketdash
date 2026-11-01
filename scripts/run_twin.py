"""Entry point for the paper/live twin runner."""

def _build_safety(config) -> SafetyGuard:
    ...

def _resolve_initial_condition_ids(*, market_meta_client: MarketMetaClient, logger: logging.Logger) -> list[str]:
    ...

def _build_realistic_fill(config, paper_strategy_configs: list[StrategyInstanceConfig]) -> tuple[FillModel | None, LiveBookProvider | None]:
    ...

def _configure_logging() -> None:
    """Route venue_stream + twin startup INFO-level logs into the"""
    ...

def _parse_args() -> 'argparse.Namespace':
    """CLI for running multiple twin instances with different configs +"""
    ...

def _preflight_latest_snapshot(root: Path) -> None:
    ...

def main() -> None:
    ...
