import mysql.connector
from mysql.connector import Error
from CommandsDB.db import connect_db

def delete_record(table, id_field, record_id):
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        query = f"DELETE FROM {table} WHERE {id_field} = %s"
        cursor.execute(query, (record_id,))
        conn.commit()
        conn.close()

def delete_client(client_id):
    return delete_record("clients", "client_id", client_id)

def delete_worker(worker_id):
    return delete_record("employees", "employee_id", worker_id)

def delete_assembly(assembly_id):
    return delete_record("computer_builds", "product_id", assembly_id)

def delete_component(component_id):
    return delete_record("components", "component_id", component_id)

def delete_supplier(supplier_id):
    return delete_record("suppliers", "supplier_id", supplier_id)