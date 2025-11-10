from telegram.ext import Updater, CommandHandler
import os

TOKEN = os.getenv("BOT_TOKEN") or "TEMP_TOKEN"

def start(update, context):
    update.message.reply_text("✅ Бот работает на Render 24/7!")

def ping(update, context):
    update.message.reply_text("pong ✅")

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("ping", ping))

updater.start_polling()
updater.idle()
