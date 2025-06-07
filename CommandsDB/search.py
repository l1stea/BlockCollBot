import mysql.connector
from mysql.connector import Error
from CommandsDB.db import connect_db

# Функции для поиска данных в таблицах (по подстроке)
def search_client(keywords):
    try:
        connection = connect_db()
        cursor = connection.cursor()
        query = "SELECT * FROM clients WHERE " + " AND ".join(
            "(first_name LIKE %s OR last_name LIKE %s OR email LIKE %s OR phone_number LIKE %s OR address LIKE %s)"
            for _ in keywords
        )
        params = []
        for kw in keywords:
            like_kw = f"%{kw}%"
            params.extend([like_kw] * 5)
        cursor.execute(query, params)
        return cursor.fetchall()
    except Error as e:
        print(f"Ошибка: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


def search_worker(keywords):
    try:
        connection = connect_db()
        cursor = connection.cursor()
        query = "SELECT * FROM workers WHERE " + " AND ".join(
            "(first_name LIKE %s OR last_name LIKE %s OR position LIKE %s)"
            for _ in keywords
        )
        params = []
        for kw in keywords:
            like_kw = f"%{kw}%"
            params.extend([like_kw] * 3)
        cursor.execute(query, params)
        return cursor.fetchall()
    except Error as e:
        print(f"Ошибка: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


def search_assembly(keywords):
    try:
        connection = connect_db()
        cursor = connection.cursor()
        query = "SELECT * FROM assemblies WHERE " + " AND ".join(
            "(name LIKE %s OR description LIKE %s)"
            for _ in keywords
        )
        params = []
        for kw in keywords:
            like_kw = f"%{kw}%"
            params.extend([like_kw] * 2)
        cursor.execute(query, params)
        return cursor.fetchall()
    except Error as e:
        print(f"Ошибка: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


def search_component(keywords):
    try:
        connection = connect_db()
        cursor = connection.cursor()
        query = "SELECT * FROM components WHERE " + " AND ".join(
            "(name LIKE %s OR type LIKE %s)"
            for _ in keywords
        )
        params = []
        for kw in keywords:
            like_kw = f"%{kw}%"
            params.extend([like_kw] * 2)
        cursor.execute(query, params)
        return cursor.fetchall()
    except Error as e:
        print(f"Ошибка: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


def search_supplier(keywords):
    try:
        connection = connect_db()
        cursor = connection.cursor()
        query = "SELECT * FROM suppliers WHERE " + " AND ".join(
            "(name LIKE %s OR email LIKE %s OR phone LIKE %s OR address LIKE %s)"
            for _ in keywords
        )
        params = []
        for kw in keywords:
            like_kw = f"%{kw}%"
            params.extend([like_kw] * 4)
        cursor.execute(query, params)
        return cursor.fetchall()
    except Error as e:
        print(f"Ошибка: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
