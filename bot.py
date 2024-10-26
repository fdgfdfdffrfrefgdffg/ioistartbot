import logging
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Update
from flask import Flask, request, jsonify
from config import BOT_TOKEN
import message, callback
from sqldata import default, close_db

# Webhook URL'ni to‘g‘ri yo‘nalish bilan sozlash
WEBHOOK_URL = "https://ioistart.pythonanywhere.com/webhook"

# Bot va dispatcher obyektlarini yaratish
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Flask serverini yaratish
app = Flask(__name__)

# Webhook uchun endpoint
@app.route("/webhook", methods=["POST"])
def handle_webhook():
    json_data = request.get_json()
    update = Update(**json_data)
    asyncio.run(dp.feed_update(bot, update))  # Asinxron funksiyani sinxron tarzda bajarish
    return jsonify({"status": "ok"})

# Webhook va botni sozlash uchun on_startup funksiyasi
async def on_startup():
    await bot.send_message(chat_id=5165396993, text="Bot ishga tushdi!")
    await bot.set_webhook(WEBHOOK_URL)

if __name__ == "__main__":
    # DB funksiyalarini boshlash va tozalash
    default()
    dp.include_router(message.router)
    dp.include_router(callback.router)
    
    # Flask serverni ishga tushirish
    from werkzeug.serving import run_simple
    run_simple("0.0.0.0", 8443, app)
    
    close_db()
