import mysql.connector
from mysql.connector import Error
from CommandsDB.db import connect_db

# Функции для поиска данных в таблицах
def search_client(client_id):
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, first_name, last_name, email, phone_number, address FROM clients WHERE id = %s", (client_id,))
        row = cursor.fetchone()
        conn.close()
        return row

def search_worker(worker_id):
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, first_name, last_name, position, salary, hire_date FROM employees WHERE id = %s", (worker_id,))
        row = cursor.fetchone()
        conn.close()
        return row

def search_assembly(assembly_id):
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, product_name, product_description, price, stock_quantity FROM computer_builds WHERE id = %s", (assembly_id,))
        row = cursor.fetchone()
        conn.close()
        return row

def search_component(component_id):
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, product_name, price, description, stock_quantity FROM components WHERE id = %s", (component_id,))
        row = cursor.fetchone()
        conn.close()
        return row

def search_supplier(supplier_id):
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, supplier_name, contact_info FROM suppliers WHERE id = %s", (supplier_id,))
        row = cursor.fetchone()
        conn.close()
        return row
