import asyncio

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from app.config import settings


async def main():
    dp = Dispatcher(storage=MemoryStorage())
    await dp.start_polling(Bot(token=settings.BOT_TOKEN))


if "__main__" == __name__:
    asyncio.run(main())
