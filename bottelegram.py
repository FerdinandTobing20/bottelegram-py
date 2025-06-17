from telegram import Update
from telegram.ext import CommandHandler, MessageHandler, filters, ApplicationBuilder
import os

# Mengambil API Token dari Environment Variable
TOKEN = os.getenv("8171717792:AAFX9308xlzCN0nquPZrH9rHmaWvHFdeQj8")

async def start(update: Update, context):
    await update.message.reply_text("Hallo! Bot aktif dan siap melayani 😊")

async def echo(update: Update, context):
    await update.message.reply_text(f"Anda mengatakan: {update.message.text}")

def main():
    # Membangun application
    app = ApplicationBuilder().token(TOKEN).build()

    # Menambah handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Menjalankan bot secara polling
    app.run_polling()


if __name__ == '__main__':
    main()
