from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from asyncio import run
import message, callback
from sqldata import default, close_db
from aiogram.client.session.aiohttp import AiohttpSession
dp = Dispatcher()

async def main():
    session = AiohttpSession(proxy="http://proxy.server:3128/")
    bot = Bot(BOT_TOKEN, session=session)
    default()
    dp.include_router(message.router)
    dp.include_router(callback.router)
    await dp.start_polling(bot)
    close_db()

run(main=main())
