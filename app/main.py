import asyncio

from app.config import settings
from app.listener import SimpleBusinessLogic


async def main():
    service = SimpleBusinessLogic(settings.MODE)
    await service.start()


if "__main__" == __name__:
    asyncio.run(main())
