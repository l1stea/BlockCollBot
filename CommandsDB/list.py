import mysql.connector
from mysql.connector import Error
from CommandsDB.db import connect_db

# Функции для получения данных из таблиц

def list_clients():
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT client_id, first_name, last_name, email, phone_number, address FROM clients")
        rows = cursor.fetchall()
        conn.close()
        return rows


def list_workers():
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT employee_id, first_name, last_name, position, salary, hire_date FROM employees")
        rows = cursor.fetchall()
        conn.close()
        return rows


def list_assemblies():
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT product_id, product_name, product_description, price, stock_quantity FROM computer_builds")
        rows = cursor.fetchall()
        conn.close()
        return rows


def list_components():
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT component_id, product_name, price, description, stock_quantity FROM components")
        rows = cursor.fetchall()
        conn.close()
        return rows


def list_suppliers():
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT supplier_id, supplier_name, contact_info FROM suppliers")
        rows = cursor.fetchall()
        conn.close()
        return rows
    
def list_sales():
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT sale_id, employee_id, client_id, product_id, quantity, sale_date FROM sales")
        rows = cursor.fetchall()
        conn.close()
        return rows
