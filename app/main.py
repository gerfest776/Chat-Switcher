import asyncio

from loguru import logger

from app.config import settings
from app.listener import SimpleBusinessLogic


async def main():
    logger.info(f'Listener started with mode - {settings.MODE}')
    service = SimpleBusinessLogic(settings.MODE)
    await service.start()


if "__main__" == __name__:
    asyncio.run(main())
