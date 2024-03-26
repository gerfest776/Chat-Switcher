from typing import ClassVar

from app.config import ChannelMode, settings
from app.services import ChatTransportTelegram
from app.services.interface import ChatTransportServiceI, Event


class SimpleBusinessLogic:
    RECEIVED_TEXT: ClassVar[str] = 'Hi! Your message was received'

    def __init__(self, mode: ChannelMode):
        self._transporter: ChatTransportServiceI = self._init_transporter(mode)

    async def listen(self, *args, **kwargs) -> None:
        await self._transporter.send_message(
            text=self.RECEIVED_TEXT, *args, **kwargs
        )

    def _init_transporter(self, mode: ChannelMode) -> ChatTransportServiceI:
        match mode:
            case ChannelMode.TELEGRAM:
                transporter = ChatTransportTelegram(
                    channel_id=settings.TRANSPORT_CHANNEL_ID,
                    bot=settings.trasnporter_bot,
                )
                transporter.add_handler(event=Event.MESSAGE, handler=self.listen)
                return transporter

    async def start(self):
        await self._transporter.run()
