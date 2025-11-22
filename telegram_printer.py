import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = "YOUR_TELEGRAM_BOT_TOKEN_HERE"
DOWNLOAD_DIR = "/home/ilhan/print_queue"

os.makedirs(DOWNLOAD_DIR, exist_ok=True)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def handle_document(update: Update, context: ContextTypes.DEFAULT_TYPE):
    document = update.message.document
    file_name = document.file_name
    file_path = os.path.join(DOWNLOAD_DIR, file_name)

    file = await document.get_file()
    await file.download_to_drive(file_path)
    logging.info(f"Downloaded {file_name}")

    os.system(f'lp "{file_path}"')
    logging.info(f"Printed {file_name}")

    await update.message.reply_text(f"✅ Your file '{file_name}' has been printed.")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(MessageHandler(filters.Document.ALL, handle_document))

    logging.info("Telegram printer bot is running...")
    app.run_polling()
