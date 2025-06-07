import mysql.connector
from mysql.connector import Error
from CommandsDB.db import connect_db

# Функции для удаления данных из таблиц
def delete_client(client_id):
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM clients WHERE client_id = %s', (client_id,))
        conn.commit()
        conn.close()

def delete_worker(worker_id):
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM employees WHERE employee_id = %s", (worker_id,))
        conn.commit()
        conn.close()

def delete_assembly(assembly_id):
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM computer_builds WHERE product_id = %s", (assembly_id,))
        conn.commit()
        conn.close()

def delete_component(component_id):
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM components WHERE component_id = %s", (component_id,))
        conn.commit()
        conn.close()

def delete_supplier(supplier_id):
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM suppliers WHERE supplier_id = %s", (supplier_id,))
        conn.commit()
        conn.close()

