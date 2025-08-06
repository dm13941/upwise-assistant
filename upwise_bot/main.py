import os
import telegram
from flask import Flask, request

# Получаем токен из переменных окружения
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")  # ключевой момент: точное имя переменной

if not TOKEN:
    raise ValueError("❌ Переменная окружения TELEGRAM_BOT_TOKEN не установлена.")

bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)

@app.route('/')
def index():
    return "✅ Upwise Bot is running."

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)

    chat_id = update.message.chat.id
    text = update.message.text or ""

    if text.strip().lower() == "/start":
        bot.send_message(chat_id=chat_id, text="Привет! Я бот платформы Upwise 👋")
    else:
        bot.send_message(chat_id=chat_id, text=f"Вы написали: {text}")

    return "ok"

if __name__ == '__main__':
    app.run(debug=False)
