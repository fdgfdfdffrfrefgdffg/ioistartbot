import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from logging import INFO, basicConfig
from datetime import datetime
from asyncio import run
import message, callback
from sqldata import default, close_db
from aiogram.client.session.aiohttp import AiohttpSession

dp = Dispatcher()

GROUP_ID = -123456789  
async def send_timer_messages(bot: Bot):
    last_message_id = 0
    while True:
        now = datetime.now()

        current_hour = now.hour
        current_minute = now.minute

        if current_hour == 20 and 0 <= current_minute < 30:
            if current_minute in [0, 10, 15, 20, 25, 26, 27, 28, 29]:  
                minutes_left = 30 - current_minute
                if last_message_id != 0: await bot.delete_message(GROUP_ID, last_message_id)
                message = await bot.send_message(GROUP_ID, f"Diqqat! Darsga {minutes_left} daqiqa qoldi.")
                last_message_id = message.message_id
        await asyncio.sleep(60)  

async def main():
    session = AiohttpSession(proxy="http://proxy.server:3128/")
    bot = Bot(BOT_TOKEN, session=session)
    default()
    basicConfig(level=INFO)
    dp.include_router(message.router)
    dp.include_router(callback.router)
    
    asyncio.create_task(send_timer_messages(bot))

    close_db()

run(main=main())
