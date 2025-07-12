import mysql.connector
from mysql.connector import Error
from CommandsDB.db import connect_db

def link_table(table, fields, values):
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        query = f"INSERT INTO {table} ({', '.join(fields)}) VALUES ({', '.join(['%s'] * len(fields))})"
        cursor.execute(query, tuple(values))
        conn.commit()
        conn.close()

def link_assembly_component(assembly_id, component_id):
    return link_table("assembly_components", ["assembly_id", "component_id"], [assembly_id, component_id])

def link_component_supplier(component_id, supplier_id):
    return link_table("component_suppliers", ["component_id", "supplier_id"], [component_id, supplier_id])