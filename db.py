import config
import mysql.connector
from mysql.connector import Error

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