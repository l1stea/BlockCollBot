import mysql.connector
from mysql.connector import Error
from CommandsDB.db import connect_db
from Logging.bot_logging import logging

def universal_search(table, fields, keywords):
    try:
        connection = connect_db()
        cursor = connection.cursor()
        query = f"SELECT * FROM {table} WHERE " + " AND ".join(
            "(" + " OR ".join(f"{field} LIKE %s" for field in fields) + ")"
            for _ in keywords
        )
        params = []
        for kw in keywords:
            like_kw = f"%{kw}%"
            params.extend([like_kw] * len(fields))
        cursor.execute(query, params)
        return cursor.fetchall()
    except Error as e:
        logging.error(f"Ошибка: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


def search_client(keywords):
    return universal_search("clients", ["first_name", "last_name", "email", "phone_number", "address"], keywords)

def search_worker(keywords):
    return universal_search("employees", ["first_name", "last_name", "position_id", "salary", "hire_date", "chat_id"], keywords)

def search_assembly(keywords):
    return universal_search("assemblies", ["product_name", "description", "price", "stock_quantity"], keywords)

def search_component(keywords):
    return universal_search("components", ["product_name", "price", "description", "stock_quantity"], keywords)

def search_supplier(keywords):
    return universal_search("suppliers", ["company_name", "contact_name", "contact_phone", "contact_email"], keywords)