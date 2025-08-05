from flask import Flask, request
import telegram
import os

TOKEN = os.getenv("BOT_TOKEN")
bot = telegram.Bot(token=TOKEN)
app = Flask(__name__)

@app.route('/')
def index():
    return "Upwise Assistant Bot is running!"

@app.route('/webhook', methods=['POST'])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    text = update.message.text
    bot.send_message(chat_id=chat_id, text=f"Вы написали: {text}")
    return 'ok'

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))