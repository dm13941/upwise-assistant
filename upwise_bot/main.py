import os
import telegram
from flask import Flask, request

TOKEN = os.environ.get("BOT_TOKEN")  # безопасно через переменные среды
bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)

@app.route('/')
def index():
    return "Upwise Bot is alive!"

@app.route(f"/{TOKEN}", methods=["POST"])
def respond():
    update = telegram.Update.de_json(request.get_json(force=True), bot)

    chat_id = update.message.chat.id
    message_text = update.message.text

    # Простая реакция
    if message_text.lower() == "/start":
        bot.send_message(chat_id=chat_id, text="Привет! Я бот платформы Upwise 👋")
    else:
        bot.send_message(chat_id=chat_id, text="Вы написали: " + message_text)

    return "ok"

if __name__ == '__main__':
    app.run(debug=False)
