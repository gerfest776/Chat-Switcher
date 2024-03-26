from typing import Callable, NoReturn

from aiogram import Dispatcher, Bot

from app.services.interface import Event
from app.services.telegram.exceptions import SendMessagePermissionError


class ChatTransportTelegram:
    def __init__(
            self,
            channel_id: str,
            bot: Bot,
            dispatcher: Dispatcher,
    ):
        self._channel = channel_id
        self._bot = bot
        self._dispatcher = dispatcher

    def add_handler(self, event: Event, handler: Callable) -> None | NoReturn:
        match event:
            case Event.MESSAGE:
                self._check_rights_on_channel()
                self._dispatcher.message.register(handler)

    async def _check_rights_on_channel(self) -> None | NoReturn:
        permissions = await self._bot.get_chat_member(
            chat_id=self._channel,
            user_id=self._bot.id,
        )
        if not permissions.can_post_messages:
            raise SendMessagePermissionError(channel=self._channel)

    async def send_message(self, msg: str):
        await self._bot.send_message(chat_id=self._channel, text=msg)

    async def run(self):
        await self._dispatcher.start_polling()


