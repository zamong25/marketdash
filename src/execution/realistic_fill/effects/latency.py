"""Latency effect — samples network + server latency from the empirical"""

class LatencyEffect:
    name: ClassVar[str]

    def __init__(self, latency_model: LatencyModel) -> None:
        ...

    def apply(self, context: 'FillContext', book: 'BookProvider') -> 'FillContext':
        ...
