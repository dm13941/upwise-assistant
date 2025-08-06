from flask import Flask, request
import requests
import os

app = Flask(__name__)

TELEGRAM_BOT_TOKEN = '7211128542:AAHS5pOPucvsRT0512ca1d3VTMVecez32zI'
TELEGRAM_API_URL = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}'

@app.route('/', methods=['POST'])
def telegram_webhook():
    data = request.get_json()

    if 'message' in data:
        chat_id = data['message']['chat']['id']
        message_text = data['message'].get('text', '')

        if message_text.startswith('/'):
            handle_command(chat_id, message_text)
        else:
            send_message(chat_id, f"Вы написали: {message_text}")

    return '', 200

def handle_command(chat_id, command):
    if command == '/status':
        send_message(chat_id, "✅ Бот работает. Upwise Assistant на связи.")
    elif command == '/help':
        send_message(chat_id, "📋 Доступные команды:\n/status — проверить статус\n/help — список команд")
    else:
        send_message(chat_id, f"Неизвестная команда: {command}")

def send_message(chat_id, text):
    url = f'{TELEGRAM_API_URL}/sendMessage'
    payload = {'chat_id': chat_id, 'text': text}
    requests.post(url, json=payload)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
