from typing import Callable, NoReturn

from aiogram import Dispatcher, Bot
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message
from loguru import logger

from app.services.interface import Event


class ChatTransportTelegram:
    def __init__(
            self,
            channel_id: str,
            bot: Bot,
    ):
        self._channel = channel_id
        self._bot = bot
        self._dispatcher = Dispatcher(storage=MemoryStorage())

    def add_handler(self, event: Event, handler: Callable) -> None | NoReturn:
        match event:
            case Event.MESSAGE:
                self._dispatcher.message.register(handler)
                logger.info(f'Handler for message event added - {handler.__name__}')

    @staticmethod
    async def send_message(message: Message, text: str, **_):
        await message.answer(f'{text}: {message.text}')

    async def run(self):
        await self._dispatcher.start_polling(self._bot)

