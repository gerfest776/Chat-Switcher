from enum import Enum

from aiogram import Bot
from dotenv import load_dotenv
from pydantic_settings import BaseSettings


load_dotenv()


class ChannelMode(str, Enum):
    DISCORD = "DISCORD"
    TELEGRAM = "TELEGRAM"


class BotSettings(BaseSettings):
    BOT_TOKEN: str
    ADMIN_ID: int
    MODE: ChannelMode

    TRANSPORT_CHANNEL_ID: str
    TRANSPORT_CHANNEL_TELEGRAM_TOKEN: str

    @property
    def bot(self) -> Bot:
        return Bot(token=self.BOT_TOKEN)

    @property
    def trasnporter_bot(self) -> Bot:
        return Bot(token=self.TRANSPORT_CHANNEL_TELEGRAM_TOKEN)


settings = BotSettings()
