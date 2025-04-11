import requests
import config
import time
import mysql.connector
from mysql.connector import Error

# Глобальная переменная для таймаута
timeout = 60

# Функция для подключения к базе данных MySQL
def connect_db():
    try:
        conn = mysql.connector.connect(
            host=config.DB_CONFIG["host"],  # Используем параметры из config.py
            user=config.DB_CONFIG["user"],
            password=config.DB_CONFIG["password"],
            database=config.DB_CONFIG["database"]
        )
        if conn.is_connected():
            return conn
    except Error as e:
        print(f"Ошибка подключения к базе данных: {e}")
        return None

# Функция для создания таблиц, если они не существуют
def create_tables():
    conn = connect_db()
    if conn:
        cursor = conn.cursor()

        # Таблица пользователей
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INT PRIMARY KEY,
            first_name VARCHAR(255),
            username VARCHAR(255),
            last_message TEXT
        )
        ''')

        # Таблица продуктов
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            product_id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            category VARCHAR(255),
            price DECIMAL(10, 2),
            stock_quantity INT
        )
        ''')

        # Таблица заказов
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            order_id INT AUTO_INCREMENT PRIMARY KEY,
            user_id INT,
            product_id INT,
            quantity INT,
            status VARCHAR(50),
            FOREIGN KEY(user_id) REFERENCES users(user_id),
            FOREIGN KEY(product_id) REFERENCES products(product_id)
        )
        ''')

        # Таблица для отслеживания количества товара на складе
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS stock (
            product_id INT,
            quantity INT,
            PRIMARY KEY(product_id),
            FOREIGN KEY(product_id) REFERENCES products(product_id)
        )
        ''')

        conn.commit()
        conn.close()

# Функция для добавления или обновления пользователя в базе данных
def add_or_update_user(user_id, first_name, username, last_message):
    conn = connect_db()
    if conn:
        cursor = conn.cursor()

        # Проверим, существует ли пользователь
        cursor.execute('SELECT * FROM users WHERE user_id = %s', (user_id,))
        user = cursor.fetchone()

        if user:
            # Если пользователь уже существует, обновим его данные
            cursor.execute('''
            UPDATE users 
            SET first_name = %s, username = %s, last_message = %s 
            WHERE user_id = %s
            ''', (first_name, username, last_message, user_id))
        else:
            # Если пользователя нет, добавим его
            cursor.execute('''
            INSERT INTO users (user_id, first_name, username, last_message) 
            VALUES (%s, %s, %s, %s)
            ''', (user_id, first_name, username, last_message))

        conn.commit()
        conn.close()

# Функция для проверки работы бота
def check_telegram_bot():
    url = f"https://api.telegram.org/bot{config.TELEGRAM_TOKEN}/getMe"
    
    try:
        response = requests.get(url, timeout=timeout)
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
        response = requests.get(url, params=params, timeout=timeout)
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

# Функция для постоянного получения обновлений
def run_bot():
    print("Бот запущен.")
    offset = None
    
    while True:
        offset = get_updates(offset)
        time.sleep(1)  # Добавляем задержку для предотвращения перегрузки API

if __name__ == "__main__":
    check_telegram_bot()  # Проверим работу бота
    create_tables()  # Создадим таблицы, если их нет
    run_bot()  # Запускаем бота с постоянным опросом обновлений
