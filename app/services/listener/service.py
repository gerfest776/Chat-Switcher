from typing import ClassVar

from app.config import ChannelMode, settings
from app.services import ChatTransportTelegram
from app.services.discord.chat_transport import ChatTransportDiscord
from app.services.interface import ChatTransportServiceI, Event


class SimpleBusinessLogic:
    RECEIVED_TEXT: ClassVar[str] = 'Hi! Your message was received'

    def __init__(self, mode: ChannelMode):
        self._transporter: ChatTransportServiceI = self._init_transporter(mode)

    async def listen(self, message) -> None:
        content = self._transporter.extract_text(message)
        await self._transporter.send_message(
            message, text=f'{self.RECEIVED_TEXT}: {content}'
        )

    def _init_transporter(self, mode: ChannelMode) -> ChatTransportServiceI:
        match mode:
            case ChannelMode.TELEGRAM:
                transporter = ChatTransportTelegram(bot=settings.bot)
            case ChannelMode.DISCORD:
                transporter = ChatTransportDiscord(bot_token='YOUR_DISCORD_TOKEN')
            case _:
                raise ValueError(f'Unknown mode - {mode}')
        transporter.add_handler(event=Event.MESSAGE, handler=self.listen)
        return transporter

    async def start(self):
        await self._transporter.run()
