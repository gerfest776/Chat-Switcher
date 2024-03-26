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
    DISCORD_TOKEN: str
    MODE: ChannelMode


settings = BotSettings()
