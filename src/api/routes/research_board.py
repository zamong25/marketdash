"""Research-board registry and safe report reader."""

@router.get('')
def get_research_board() -> dict:
    ...

@router.get('/report', response_class=PlainTextResponse)
def get_research_report(path: str=Query(..., min_length=1)) -> PlainTextResponse:
    ...
