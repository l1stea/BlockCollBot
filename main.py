import requests
import config
import time


# Функция для проверки работы бота
def check_telegram_bot():
    url = f"https://api.telegram.org/bot{config.TELEGRAM_TOKEN}/getMe"
    
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()  # Поднимет исключение, если код ответа не 2xx
        data = response.json()
        
        if data["ok"]:
            print("Бот работает!")
            print(f"Имя бота: {data['result']['first_name']}")
            print(f"Юзернейм бота: {data['result']['username']}")
        else:
            print("Ошибка при запросе информации о боте.")
    except requests.exceptions.RequestException as e:
        print(f"Ошибка запроса: {e}")
    except ValueError as e:
        print(f"Ошибка обработки ответа JSON: {e}")

# Функция для отправки сообщения пользователю
def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{config.TELEGRAM_TOKEN}/sendMessage"
    params = {"chat_id": chat_id, "text": text}
    
    try:
        response = requests.get(url, params=params, timeout=30)
        response.raise_for_status()  # Поднимет исключение, если код ответа не 2xx
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при отправке сообщения: {e}")

# Функция для обработки входящих сообщений
def handle_message(message):
    text = message["text"].lower()
    
    if text == "/start":
        return "Привет! Я ваш новый бот."
    elif text == "/help":
        return "Список команд: /start - начать, /help - помощь."
    else:
        return "Я не понимаю эту команду."

# Функция для получения обновлений и обработки сообщений
def get_updates(offset=None):
    url = f"https://api.telegram.org/bot{config.TELEGRAM_TOKEN}/getUpdates"
    params = {"offset": offset, "timeout": 60}
    
    try:
        response = requests.get(url, params=params, timeout=60)
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

# Функция для постоянного получения обновлений
def run_bot():
    print("Бот запущен.")
    offset = None
    
    while True:
        offset = get_updates(offset)
        time.sleep(1)  # Добавляем задержку для предотвращения перегрузки API

if __name__ == "__main__":
    check_telegram_bot()  # Проверим работу бота
    run_bot()  # Запускаем бота с постоянным опросом обновлений
