# telegram_bot.py
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from services import get_weather, book_appointment

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hallo! Nutze /wetter [Stadt] oder /termin [Datum] [Zeit]")

async def wetter(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Bitte Stadt angeben: /wetter Berlin")
        return
    city = " ".join(context.args)
    result = get_weather(city)
    await update.message.reply_text(result)

async def termin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) < 2:
        await update.message.reply_text("Format: /termin 2026-03-10 14:00")
        return
    date = context.args[0]
    time = context.args[1]
    result = book_appointment(date, time)
    await update.message.reply_text(result)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("wetter", wetter))
app.add_handler(CommandHandler("termin", termin))

print("Telegram Bot läuft…")
app.run_polling()