import config
import mysql.connector
from mysql.connector import Error

def connect_db():
    try:
        conn = mysql.connector.connect(
            host=config.DB_CONFIG["host"],
            user=config.DB_CONFIG["user"],
            password=config.DB_CONFIG["password"],
            database=config.DB_CONFIG["database"]
        )
        if conn.is_connected():
            return conn
    except Error as e:
        print(f"Ошибка подключения к базе данных: {e}")
        return None

TABLES_SQL = [
    # Таблица клиентов
    '''CREATE TABLE IF NOT EXISTS clients (
        client_id INT AUTO_INCREMENT PRIMARY KEY,
        first_name VARCHAR(255),
        last_name VARCHAR(255),
        email VARCHAR(255),
        phone_number VARCHAR(15),
        address TEXT
    )''',
    # Таблица должностей
    '''CREATE TABLE IF NOT EXISTS positions (
        position_id INT AUTO_INCREMENT PRIMARY KEY,
        position VARCHAR(255) NOT NULL UNIQUE
    )''',
    # Таблица работников
    '''CREATE TABLE IF NOT EXISTS employees (
        employee_id INT AUTO_INCREMENT PRIMARY KEY,
        first_name VARCHAR(255),
        last_name VARCHAR(255),
        position_id INT,
        salary DECIMAL(10, 2),
        hire_date DATE,
        chat_id INT,
        FOREIGN KEY (position_id) REFERENCES positions(position_id)
    )''',
    # Таблица сборок
    '''CREATE TABLE IF NOT EXISTS computer_builds (
        product_id INT AUTO_INCREMENT PRIMARY KEY,
        product_name VARCHAR(255),
        product_description TEXT,
        price DECIMAL(10, 2),
        stock_quantity INT
    )''',
    # Таблица комплектующих
    '''CREATE TABLE IF NOT EXISTS components (
        component_id INT AUTO_INCREMENT PRIMARY KEY,
        product_name VARCHAR(255),
        price DECIMAL(10, 2),
        description TEXT,
        stock_quantity INT
    )''',
    # Таблица поставщиков
    '''CREATE TABLE IF NOT EXISTS suppliers (
        supplier_id INT AUTO_INCREMENT PRIMARY KEY,
        company_name VARCHAR(255),
        contact_name VARCHAR(255),
        contact_phone VARCHAR(15),
        contact_email VARCHAR(255)
    )''',
    # Связь между сборками и комплектующими
    '''CREATE TABLE IF NOT EXISTS assembly_components (
        id INT AUTO_INCREMENT PRIMARY KEY,
        product_id INT,
        component_id INT,
        FOREIGN KEY(product_id) REFERENCES computer_builds(product_id),
        FOREIGN KEY(component_id) REFERENCES components(component_id)
    )''',
    # Связь между комплектующими и поставщиками
    '''CREATE TABLE IF NOT EXISTS component_suppliers (
        id INT AUTO_INCREMENT PRIMARY KEY,
        component_id INT,
        supplier_id INT,
        supply_date DATE,
        quantity_delivered INT,
        FOREIGN KEY(component_id) REFERENCES components(component_id),
        FOREIGN KEY(supplier_id) REFERENCES suppliers(supplier_id)
    )''',
    # Таблица продаж
    '''CREATE TABLE IF NOT EXISTS sales (
        sale_id INT AUTO_INCREMENT PRIMARY KEY,
        employee_id INT,
        client_id INT,
        product_id INT,
        sale_date DATE,
        quantity INT,
        total_price DECIMAL(10, 2),
        FOREIGN KEY(employee_id) REFERENCES employees(employee_id),
        FOREIGN KEY(client_id) REFERENCES clients(client_id),
        FOREIGN KEY(product_id) REFERENCES computer_builds(product_id)
    )'''
]

def create_tables():
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            for sql in TABLES_SQL:
                cursor.execute(sql)
            conn.commit()
        except Exception as e:
            print(f"Ошибка при создании таблиц: {e}")
        finally:
            cursor.close()
            conn.close()