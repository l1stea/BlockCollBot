import mysql.connector
from mysql.connector import Error
from CommandsDB.db import connect_db
from Logging.bot_logging import *
from config import DB_CONFIG

def get_position_by_chat_id(chat_id):
    """
    Получить должность пользователя по его chat_id.

    :param chat_id: int — Telegram chat_id пользователя
    :return: str или None — название должности или None, если не найдено
    """
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT p.position
            FROM employees e
            JOIN positions p ON e.position_id = p.position_id
            WHERE e.chat_id = %s
        """, (chat_id,))
        row = cursor.fetchone()
        conn.close()
        return row[0] if row else None

def get_admin_chat_id_from_db():
    """
    Получить chat_id первого найденного администратора (позиция 'admin').

    :return: int или None — chat_id администратора или None, если не найдено
    """
    conn = connect_db()
    try:
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT c.chat_id
                FROM employees c
                JOIN positions p ON c.position_id = p.position_id
                WHERE p.position = 'admin'
                LIMIT 1
            """)
            result = cursor.fetchone()
            if result:
                return int(result[0])
            else:
                return None
    except mysql.connector.Error as e:
        logging.error(f"Ошибка при получении chat_id администратора: {e}")
        return None
    finally:
        conn.close()

def get_all_admin_chat_ids_from_db():
    """
    Получить chat_id всех администраторов (позиция 'admin').

    :return: list[int] — список chat_id администраторов
    """
    conn = connect_db()
    try:
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT c.chat_id
                FROM employees c
                JOIN positions p ON c.position_id = p.position_id
                WHERE p.position = 'admin'
            """)
            results = cursor.fetchall()
            return [int(row[0]) for row in results]
    except mysql.connector.Error as e:
        logging.error(f"Ошибка при получении chat_id администратора: {e}")
        return None
    finally:
        conn.close()