import mysql.connector
from mysql.connector import Error
from db import connect_db

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