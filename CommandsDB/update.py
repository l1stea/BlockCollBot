import mysql.connector
from mysql.connector import Error
from CommandsDB.db import connect_db

# Общая функция для обновления данных в таблицах
def update_table(table_name, record_id, **fields):
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        update_query = f"UPDATE {table_name} SET "
        params = []

        for field, value in fields.items():
            update_query += f"{field} = %s, "
            params.append(value)

        # Убираем последнюю запятую и добавляем условие WHERE
        update_query = update_query.rstrip(", ")
        update_query += f" WHERE {table_name[:-1]}_id = %s"  # Подставляем id таблицы
        params.append(record_id)

        cursor.execute(update_query, tuple(params))
        conn.commit()
        conn.close()
        return True  # <-- добавьте возврат True
    return False

# Функции для обновления данных в различных таблицах
def update_client(client_id, **fields):
    return update_table("clients", client_id, **fields)

def update_worker(worker_id, **fields):
    return  update_table("employees", worker_id, **fields)

def update_assembly(assembly_id, **fields):
    return update_table("computer_builds", assembly_id, **fields)

def update_component(component_id, **fields):
    return update_table("components", component_id, **fields)

def update_supplier(supplier_id, **fields):
    return update_table("suppliers", supplier_id, **fields)
