from enum import Enum
from typing import Protocol, Callable


class Event(str, Enum):
    MESSAGE = "MESSAGE"


class ChatTransportServiceI(Protocol):
    def add_handler(self, event: Event, handler: Callable) -> None:
        ...

    async def send_message(self, text, *args, **kwargs) -> None:
        ...

    async def run(self) -> None:
        ...
