import requests
import config
import time
from Handler.handler import handle_message
from CommandsDB.db import *

# Глобальная переменная для таймаута
timeout = 60

# Функция для получения обновлений и обработки сообщений
def get_updates(offset=None):
    url = f"https://api.telegram.org/bot{config.TELEGRAM_TOKEN}/getUpdates"
    params = {"offset": offset, "timeout": 60}
    
    try:
        response = requests.get(url, params=params, timeout=timeout)
        response.raise_for_status()
        updates = response.json()["result"]
        
        for update in updates:
            if "message" in update:
                chat_id = update["message"]["chat"]["id"]
                response_text = handle_message(update["message"])
                send_message(chat_id, response_text)
                
                # Устанавливаем новый offset, чтобы не получать те же сообщения
                offset = update["update_id"] + 1
        return offset
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при получении обновлений: {e}")
        return offset

# Функция для отправки сообщения пользователю
def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{config.TELEGRAM_TOKEN}/sendMessage"
    params = {"chat_id": chat_id, "text": text}
    
    try:
        response = requests.get(url, params=params, timeout=timeout)
        response.raise_for_status()  # Поднимет исключение, если код ответа не 2xx
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при отправке сообщения: {e}")

# Функция для постоянного получения обновлений
def run_bot():
    print("Бот запущен.")
    offset = None
    
    while True:
        offset = get_updates(offset)
        time.sleep(1)  # Добавляем задержку для предотвращения перегрузки API

if __name__ == "__main__":
    create_tables()  # Создадим таблицы, если их нет
    run_bot()  # Запускаем бота с постоянным опросом обновлений