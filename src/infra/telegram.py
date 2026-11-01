
class TelegramNotifier:

    def __init__(self, bot_name: str='', enabled: bool=True, dotenv_path: str | Path | None=None, token: str | None=None, chat_id: str | None=None) -> None:
        ...

    def _prefix(self, message: str) -> str:
        ...

    def send(self, message: str) -> bool:
        ...

    def send_alert(self, level: str, message: str | None=None, data: dict[str, Any] | None=None) -> bool:
        ...
