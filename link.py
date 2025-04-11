import mysql.connector
from mysql.connector import Error
from db import connect_db

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