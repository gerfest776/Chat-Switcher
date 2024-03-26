from dataclasses import dataclass

from app.services.exceptions import ApplicationException


@dataclass(eq=False)
class SendMessagePermissionError(ApplicationException):
    channel: str

    @property
    def message(self) -> str:
        return f'Bot has no permission to send messages to channel {self.channel}'
