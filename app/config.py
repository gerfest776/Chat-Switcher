from enum import Enum

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


settings = BotSettings()
