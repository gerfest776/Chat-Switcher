from typing import Callable, NoReturn

from aiogram import Dispatcher, Bot
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message
from loguru import logger

from app.config import settings
from app.services.interface import Event


class ChatTransportTelegram:
    def __init__(self):
        self._bot = Bot(token=settings.BOT_TOKEN)
        self._dispatcher = Dispatcher(storage=MemoryStorage())

    def add_handler(self, event: Event, handler: Callable) -> None | NoReturn:
        match event:
            case Event.MESSAGE:
                self._dispatcher.message.register(handler)
                logger.info(f'Handler for message event added - {handler.__name__}')
            case _:
                raise NotImplementedError(f'Handler for event {event} not implemented')

    @staticmethod
    async def send_message(message: Message, text: str):
        await message.answer(text)

    async def run(self):
        await self._dispatcher.start_polling(self._bot)

    @staticmethod
    def extract_text(message: Message) -> str:
        return message.text

