from aiogram import Bot, Dispatcher
from os import getenv
from dotenv import load_dotenv
import asyncio
from handlers.routes import router

load_dotenv()
BOT_TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher()

dp.include_router(router)

async def main():
    bot = Bot(token=BOT_TOKEN)
    print('Start...')
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Stop')