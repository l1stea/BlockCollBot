import mysql.connector
from mysql.connector import Error
from CommandsDB.db import connect_db

def list_table(table, fields):
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        query = f"SELECT {', '.join(fields)} FROM {table}"
        cursor.execute(query)
        rows = cursor.fetchall()
        conn.close()
        return rows

def list_clients():
    return list_table("clients", ["client_id", "first_name", "last_name", "email", "phone_number", "address"])

def list_workers():
    return list_table("employees", ["employee_id", "position_id", "first_name", "last_name", "salary", "hire_date", "chat_id"])

def list_assemblies():
    return list_table("computer_builds", ["product_id", "product_name", "product_description", "price", "stock_quantity"])

def list_components():
    return list_table("components", ["component_id", "product_name", "price", "description", "stock_quantity"])

def list_suppliers():
    return list_table("suppliers", ["supplier_id", "company_name", "contact_name", "contact_phone", "contact_email"])

def list_sales():
    return list_table("sales", ["sale_id", "employee_id", "client_id", "product_id", "sale_date", "quantity", "total_price"])

def list_positions():
    return list_table("positions", ["position_id", "position"])

def list_financials():
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        query = f"SELECT sale_id, employee_id, client_id, product_id, sale_date, quantity, total_price \
        FROM sales \
        WHERE sale_date >= DATE_SUB('2025-07-15', INTERVAL 7 DAY) AND sale_date <= '2025-07-15';"
        cursor.execute(query)
        rows = cursor.fetchall()
        conn.close()
        return rows