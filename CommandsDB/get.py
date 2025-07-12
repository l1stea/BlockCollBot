import mysql.connector
from mysql.connector import Error
from CommandsDB.db import connect_db

def get_position_by_chat_id(chat_id):
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