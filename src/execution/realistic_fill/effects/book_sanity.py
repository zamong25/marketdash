"""Snapshot sanity effect."""

class SnapshotSanityEffect:
    name: ClassVar[str]

    @staticmethod
    def _snapshot_fallback_book(context: 'FillContext') -> BookSnapshot | None:
        ...

    def apply(self, context: 'FillContext', book: 'BookProvider') -> 'FillContext':
        ...
