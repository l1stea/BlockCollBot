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

        # Таблица клиентов
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS clients (
            client_id INT AUTO_INCREMENT PRIMARY KEY,
            first_name VARCHAR(255),
            last_name VARCHAR(255),
            email VARCHAR(255),
            phone_number VARCHAR(15),
            address TEXT
        )
        ''')

        # Таблица работников
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            employee_id INT AUTO_INCREMENT PRIMARY KEY,
            first_name VARCHAR(255),
            last_name VARCHAR(255),
            position VARCHAR(255),
            salary DECIMAL(10, 2),
            hire_date DATE
        )
        ''')

        # Таблица сборок
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS computer_builds (
            product_id INT AUTO_INCREMENT PRIMARY KEY,
            product_name VARCHAR(255),
            product_description TEXT,
            price DECIMAL(10, 2),
            stock_quantity INT
        )
        ''')

        # Таблица комплектующих
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS components (
            component_id INT AUTO_INCREMENT PRIMARY KEY,
            product_name VARCHAR(255),
            price DECIMAL(10, 2),
            description TEXT,
            stock_quantity INT
        )
        ''')

        # Таблица поставщиков
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS suppliers (
            supplier_id INT AUTO_INCREMENT PRIMARY KEY,
            supplier_name VARCHAR(255),
            contact_info TEXT
        )
        ''')

        # Связь между сборками и комплектующими
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS assembly_components (
            id INT AUTO_INCREMENT PRIMARY KEY,
            product_id int,
            component_id INT,
            FOREIGN KEY(id) REFERENCES computer_builds(product_id),
            FOREIGN KEY(product_id) REFERENCES computer_builds(product_id)
        )
        ''')

        # Связь между комплектующими и поставщиками
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS component_suppliers (
            id INT AUTO_INCREMENT PRIMARY KEY,
            component_id INT,
            supplier_id INT,
            FOREIGN KEY(component_id) REFERENCES components(component_id),
            FOREIGN KEY(supplier_id) REFERENCES suppliers(supplier_id)
        )
        ''')

        conn.commit()
        conn.close()

# Функции для добавления данных в таблицы

def add_client(first_name, last_name, email, phone_number, address):
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute(''' 
        INSERT INTO clients (first_name, last_name, email, phone_number, address) 
        VALUES (%s, %s, %s, %s, %s)
        ''', (first_name, last_name, email, phone_number, address))
        conn.commit()
        conn.close()


def add_worker(first_name, last_name, position, salary, hire_date):
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO employees (first_name, last_name, position, salary, hire_date) 
        VALUES (%s, %s, %s, %s, %s)
        ''', (first_name, last_name, position, salary, hire_date))
        conn.commit()
        conn.close()


def add_assembly(product_name, product_description, price, stock_quantity):
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO computer_builds (product_name, product_description, price, stock_quantity) 
        VALUES (%s, %s, %s, %s)
        ''', (product_name, product_description, price, stock_quantity))
        conn.commit()
        conn.close()


def add_component(product_name, price, description, stock_quantity):
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO components (product_name, price, description, stock_quantity) 
        VALUES (%s, %s, %s, %s)
        ''', (product_name, price, description, stock_quantity))
        conn.commit()
        conn.close()


def add_supplier(supplier_name, contact_info):
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO suppliers (supplier_name, contact_info) 
        VALUES (%s, %s)
        ''', (supplier_name, contact_info))
        conn.commit()
        conn.close()


# Функции для связи данных
def link_assembly_component(assembly_id, component_id):
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO assembly_components (assembly_id, component_id) 
        VALUES (%s, %s)
        ''', (assembly_id, component_id))
        conn.commit()
        conn.close()

def link_component_supplier(component_id, supplier_id):
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO component_suppliers (component_id, supplier_id) 
        VALUES (%s, %s)
        ''', (component_id, supplier_id))
        conn.commit()
        conn.close()

# Функции для обработки сообщений от бота
def handle_message(message):
    text = message["text"].lower()

    if text.startswith("/addclient"):
        try:
            _, first_name, last_name, email, phone_number, address = text.split(",", 5)
            add_client(first_name.strip(), last_name.strip(), email.strip(), phone_number.strip(), address.strip())
            return "Клиент добавлен!"
        except ValueError:
            return "Ошибка: команда должна быть в формате '/addclient <first_name>, <last_name>, <email>, <phone_number>, <address>'."

    elif text.startswith("/addworker"):
        try:
            _, first_name, last_name, position, salary = text.split(",", 4)
            add_worker(first_name.strip(), last_name.strip(), position.strip(), float(salary.strip()))
            return "Работник добавлен!"
        except ValueError:
            return "Ошибка: команда должна быть в формате '/addworker <first_name>, <last_name>, <position>, <salary>'."

    elif text.startswith("/addassembly"):
        try:
            _, product_name, product_description, price, stock_quantity = text.split(",", 4)
            add_assembly(product_name.strip(), product_description.strip(), float(price.strip()), int(stock_quantity.strip()))
            return "Сборка добавлена!"
        except ValueError:
            return "Ошибка: команда должна быть в формате '/addassembly <product_name>, <product_description>, <price>, <stock_quantity>'."

    elif text.startswith("/addcomponent"):
        try:
            _, product_name, price, stock_quantity = text.split(",", 3)
            add_component(product_name.strip(), float(price.strip()), int(stock_quantity.strip()))
            return "Комплектующий добавлен!"
        except ValueError:
            return "Ошибка: команда должна быть в формате '/addcomponent <product_name>, <price>, <stock_quantity>'."

    elif text.startswith("/addsupplier"):
        try:
            _, supplier_name, contact_info = text.split(",", 2)
            add_supplier(supplier_name.strip(), contact_info.strip())
            return "Поставщик добавлен!"
        except ValueError:
            return "Ошибка: команда должна быть в формате '/addsupplier <supplier_name>, <contact_info>'."

    elif text.startswith("/linkassemblycomponent"):
        try:
            _, product_id, component_id = text.split(",", 2)
            link_assembly_component(int(product_id.strip()), int(component_id.strip()))
            return "Сборка и комплектующий связаны!"
        except ValueError:
            return "Ошибка: команда должна быть в формате '/linkassemblycomponent <product_id>, <component_id>'."

    elif text.startswith("/linkcomponentsupplier"):
        try:
            _, component_id, supplier_id = text.split(",", 2)
            link_component_supplier(int(component_id.strip()), int(supplier_id.strip()))
            return "Комплектующий и поставщик связаны!"
        except ValueError:
            return "Ошибка: команда должна быть в формате '/linkcomponentsupplier <component_id>, <supplier_id>'."

    elif text == "/start":
        return "Привет! Я ваш новый бот. Используйте команды для добавления данных."

    elif text == "/help":
        return (
            "Список команд:\n"
            "/addclient <first_name>, <last_name>, <email>, <phone_number>, <address> - добавить клиента\n"
            "/addworker <first_name>, <last_name>, <position>, <salary> - добавить работника\n"
            "/addassembly <product_name>, <product_description>, <price>, <stock_quantity> - добавить сборку\n"
            "/addcomponent <product_name>, <price>, <stock_quantity> - добавить комплектующий\n"
            "/addsupplier <supplier_name>, <contact_info> - добавить поставщика\n"
            "/linkassemblycomponent <product_id>, <component_id> - связать сборку с комплектующим\n"
            "/linkcomponentsupplier <component_id>, <supplier_id> - связать комплектующий с поставщиком"
        )

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
