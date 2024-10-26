from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
import message, callback
from sqldata import default, close_db
from aiogram import Bot, Dispatcher
from aiogram.types import Update
from aiogram.webhook.aiohttp_server import SimpleRequestHandler
from flask import Flask, request, jsonify

# Bot token va webhook URL (webhook uchun https kerak)
BOT_TOKEN = "YOUR_BOT_TOKEN"
WEBHOOK_URL = "https://your-domain.com/webhook"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
async def handle_webhook():
    update = Update(**await request.json)
    await dp.feed_update(bot, update)
    return jsonify({"status": "ok"})

async def on_startup():
    await bot.set_webhook(WEBHOOK_URL)

if __name__ == "__main__":
    default()
    dp.include_router(message.router)
    dp.include_router(callback.router)
    dp.startup.register(on_startup)
    SimpleRequestHandler(dp, bot).register(app, "/webhook")
    app.run(host="0.0.0.0", port=8443)
    close_db()


