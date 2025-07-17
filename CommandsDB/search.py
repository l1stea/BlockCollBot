from mysql.connector import Error
from CommandsDB.db import connect_db
from Logging.bot_logging import logging
import re

def parse_search_terms(text):
    # Извлекает пары поле:значение и просто значения
    pattern = r'(\w+):"([^"]+)"|(\w+):(\S+)|"([^"]+)"|(\S+)'
    matches = re.findall(pattern, text)
    fields = {}
    keywords = []
    for m in matches:
        if m[0] and m[1]:  # поле:"значение"
            fields[m[0]] = m[1]
        elif m[2] and m[3]:  # поле:значение
            fields[m[2]] = m[3]
        elif m[4]:  # "значение"
            keywords.append(m[4])
        elif m[5]:  # значение
            keywords.append(m[5])
    return fields, keywords

def universal_search(table, fields, keywords, field_filters=None):
    try:
        connection = connect_db()
        cursor = connection.cursor()
        where_clauses = []
        params = []

        # Поиск по конкретным полям
        if field_filters:
            for field, value in field_filters.items():
                where_clauses.append(f"{field} LIKE %s")
                params.append(f"%{value}%")

        # Поиск по всем полям
        if keywords:
            for kw in keywords:
                where_clauses.append(
                    "(" + " OR ".join(f"{field} LIKE %s" for field in fields) + ")"
                )
                params.extend([f"%{kw}%"] * len(fields))

        query = f"SELECT * FROM {table}"
        if where_clauses:
            query += " WHERE " + " AND ".join(where_clauses)

        cursor.execute(query, params)
        return cursor.fetchall()
    except Error as e:
        logging.error(f"Ошибка: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()