import asyncio
from aiogram import Bot, Dispatcher
from config.settings import TG_TOKEN
from handlers.commands import router
from services.scheduler import setup_scheduler


async def main():
    bot = Bot(token=TG_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)

    setup_scheduler(bot)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
