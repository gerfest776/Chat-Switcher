import asyncio

from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from app.config import settings
from app.services.listener.service import SimpleBusinessLogic


async def on_startup(*args, **kwargs):
    service = SimpleBusinessLogic(settings.MODE)
    await service.start()


async def main():
    dp = Dispatcher(storage=MemoryStorage())
    dp.startup.register(on_startup)
    await dp.start_polling(settings.bot)


if "__main__" == __name__:
    asyncio.run(main())
