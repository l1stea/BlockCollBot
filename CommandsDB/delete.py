import mysql.connector
from mysql.connector import Error
from CommandsDB.db import connect_db

# Функции для удаления данных из таблиц
def delete_client(client_id):
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM clients WHERE id = %s', (client_id,))
        conn.commit()
        conn.close()

def delete_worker(worker_id):
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM employees WHERE id = %s", (worker_id,))
        conn.commit()
        conn.close()

def delete_assembly(assembly_id):
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM computer_builds WHERE id = %s", (assembly_id,))
        conn.commit()
        conn.close()

def delete_component(component_id):
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM components WHERE id = %s", (component_id,))
        conn.commit()
        conn.close()

def delete_supplier(supplier_id):
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM suppliers WHERE id = %s", (supplier_id,))
        conn.commit()
        conn.close()

