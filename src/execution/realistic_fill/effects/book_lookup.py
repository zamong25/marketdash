"""Book lookup effect — fetches the latest book snapshot at or before"""

class BookLookupEffect:
    name: ClassVar[str]

    @staticmethod
    def _signal_snapshot_fallback_book(context: 'FillContext') -> 'BookSnapshot | None':
        ...

    def apply(self, context: 'FillContext', book: 'BookProvider') -> 'FillContext':
        ...
