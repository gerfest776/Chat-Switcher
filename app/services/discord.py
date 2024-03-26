from typing import Callable, Coroutine, Any

import discord
from discord import Message
from loguru import logger

from app.config import settings
from app.services.interface import Event


class ChatTransportDiscord:
    def __init__(self):
        self._client = discord.Client(
            intents=discord.Intents.default()
        )

    @staticmethod
    def extract_text(message: Message) -> str:
        return message.content

    @staticmethod
    async def send_message(message: Message, text: str):
        await message.channel.send(text)

    def add_handler(self, event: Event, handler: Callable[[Any], Coroutine]):
        match event:
            case Event.MESSAGE:
                @self._client.event
                async def on_message(message: Message):
                    if message.author == self._client.user:
                        return
                    await handler(message)
                logger.info(f'Handler for message event added - {handler.__name__}')
            case _:
                raise NotImplementedError(f'Handler for event {event} not implemented')

    async def run(self):
        await self._client.start(settings.DISCORD_TOKEN)
