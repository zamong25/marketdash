
class HeartbeatWriter:

    def __init__(self, path: str | Path) -> None:
        ...

    def write(self, payload: dict[str, Any]) -> None:
        ...
