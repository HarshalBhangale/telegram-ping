from flask import Flask, request
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import threading
import asyncio

# Initialize Flask app
app = Flask(__name__)

# Define the welcome message
WELCOME_MESSAGE = (
    "Welcome, traveler! The sands of fate have brought you to a forgotten corner of the ancient world. "
    "Here, whispers of a lost god named Hapet, the Spirit of Fortune, echo through the ruins.\n\n"
    "You stand before a locked human structure ornate chest. Legend speaks of powerful artifacts within, "
    "and perhaps even the key to freeing Hapet himself.\n\n"
    "Are you ready to unlock your destiny?\n\n"
    "This is just the beginning of your journey. As you progress, you'll:\n"
    "- Uncover the secrets of Hapet's imprisonment.\n"
    "- Find his lost artifacts and restore his power.\n"
    "- Maybe even earn a touch of his legendary luck!\n\n"
    "But beware, the path ahead is fraught with challenges. Will you rise as a champion of fortune, or "
    "succumb to the sands of time?\n\n"
    "Let the games begin!"
)

# Initialize Telegram bot
application = ApplicationBuilder().token("7531449555:AAH2Dyvm7LJc93RV-kzGrjHcDYrhXTBHWpw").build()

# Define the start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(WELCOME_MESSAGE)

# Add the start command handler to the application
application.add_handler(CommandHandler("start", start))

# Define a route for the webhook (use this if you want to use webhooks instead of polling)
@app.route('/webhook', methods=['POST'])
async def webhook():
    update = Update.de_json(request.get_json(force=True), application.bot)
    await application.process_update(update)
    return 'ok'

# Define the main route to check if the server is running
@app.route('/')
def index():
    return "Telegram bot is running!"

# Function to run the Flask app
def run_flask():
    app.run(debug=True, use_reloader=False)

if __name__ == '__main__':
    # Start Flask app in a separate thread
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()

    # Run the bot polling in the main thread
    asyncio.run(application.run_polling())

# from telegram import Update
# from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes,  MessageHandler, filters, ContextTypes
# WELCOME_MESSAGE = (
#     "Welcome, traveler! The sands of fate have brought you to a forgotten corner of the ancient world. "
#     "Here, whispers of a lost god named Hapet, the Spirit of Fortune, echo through the ruins.\n\n"
#     "You stand before a locked human structure ornate chest. Legend speaks of powerful artifacts within, "
#     "and perhaps even the key to freeing Hapet himself.\n\n"
#     "Are you ready to unlock your destiny?\n\n"
#     "This is just the beginning of your journey. As you progress, you'll:\n"
#     "- Uncover the secrets of Hapet's imprisonment.\n"
#     "- Find his lost artifacts and restore his power.\n"
#     "- Maybe even earn a touch of his legendary luck!\n\n"
#     "But beware, the path ahead is fraught with challenges. Will you rise as a champion of fortune, or "
#     "succumb to the sands of time?\n\n"
#     "Let the games begin!"
# )

# # async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
# #     await update.message.reply_text(f'Hello {update.effective_user.username}')


# # app = ApplicationBuilder().token("7531449555:AAH2Dyvm7LJc93RV-kzGrjHcDYrhXTBHWpw").build()

# # app.add_handler(CommandHandler("hello", hello))

# # app.run_polling()

# async def send_welcome(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text(WELCOME_MESSAGE)

# app = ApplicationBuilder().token("7531449555:AAH2Dyvm7LJc93RV-kzGrjHcDYrhXTBHWpw").build()

# # Add a MessageHandler that triggers on any text message
# # app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, send_welcome))
# app.add_handler(CommandHandler("start", WELCOME_MESSAGE))
# app.run_polling()