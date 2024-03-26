from enum import Enum
from typing import Protocol


class Event(str, Enum):
    MESSAGE = "MESSAGE"


class ChatTransportServiceI(Protocol):
    def add_handler(self, event: Event) -> None:
        ...

    async def send_message(self, msg: str) -> str:
        ...

    async def run(self) -> None:
        ...
