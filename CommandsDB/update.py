import mysql.connector
from mysql.connector import Error
from CommandsDB.db import connect_db

# Функции для обновления данных в таблицах
def update_client(client_id, first_name=None, last_name=None, email=None, phone_number=None, address=None):
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        update_query = "UPDATE clients SET "
        params = []

        if first_name:
            update_query += "first_name = %s, "
            params.append(first_name)
        if last_name:
            update_query += "last_name = %s, "
            params.append(last_name)
        if email:
            update_query += "email = %s, "
            params.append(email)
        if phone_number:
            update_query += "phone_number = %s, "
            params.append(phone_number)
        if address:
            update_query += "address = %s, "
            params.append(address)

        update_query = update_query.rstrip(", ")  # Убираем последнюю запятую
        update_query += " WHERE id = %s"
        params.append(client_id)

        cursor.execute(update_query, tuple(params))
        conn.commit()
        conn.close()

def update_worker(worker_id, first_name=None, last_name=None, position=None, salary=None, hire_date=None):
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        update_query = "UPDATE employees SET "
        params = []

        if first_name:
            update_query += "first_name = %s, "
            params.append(first_name)
        if last_name:
            update_query += "last_name = %s, "
            params.append(last_name)
        if position:
            update_query += "position = %s, "
            params.append(position)
        if salary:
            update_query += "salary = %s, "
            params.append(salary)
        if hire_date:
            update_query += "hire_date = %s, "
            params.append(hire_date)

        update_query = update_query.rstrip(", ")  # Убираем последнюю запятую
        update_query += " WHERE id = %s"
        params.append(worker_id)

        cursor.execute(update_query, tuple(params))
        conn.commit()
        conn.close()

def update_assembly(assembly_id, product_name=None, product_description=None, price=None, stock_quantity=None):
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        update_query = "UPDATE computer_builds SET "
        params = []

        if product_name:
            update_query += "product_name = %s, "
            params.append(product_name)
        if product_description:
            update_query += "product_description = %s, "
            params.append(product_description)
        if price:
            update_query += "price = %s, "
            params.append(price)
        if stock_quantity:
            update_query += "stock_quantity = %s, "
            params.append(stock_quantity)

        update_query = update_query.rstrip(", ")  # Убираем последнюю запятую
        update_query += " WHERE id = %s"
        params.append(assembly_id)

        cursor.execute(update_query, tuple(params))
        conn.commit()
        conn.close()

def update_component(component_id, product_name=None, price=None, description=None, stock_quantity=None):
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        update_query = "UPDATE components SET "
        params = []

        if product_name:
            update_query += "product_name = %s, "
            params.append(product_name)
        if price:
            update_query += "price = %s, "
            params.append(price)
        if description:
            update_query += "description = %s, "
            params.append(description)
        if stock_quantity:
            update_query += "stock_quantity = %s, "
            params.append(stock_quantity)

        update_query = update_query.rstrip(", ")  # Убираем последнюю запятую
        update_query += " WHERE id = %s"
        params.append(component_id)

        cursor.execute(update_query, tuple(params))
        conn.commit()
        conn.close()

def update_supplier(supplier_id, supplier_name=None, contact_info=None):
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        update_query = "UPDATE suppliers SET "
        params = []

        if supplier_name:
            update_query += "supplier_name = %s, "
            params.append(supplier_name)
        if contact_info:
            update_query += "contact_info = %s, "
            params.append(contact_info)

        update_query = update_query.rstrip(", ")  # Убираем последнюю запятую
        update_query += " WHERE id = %s"
        params.append(supplier_id)

        cursor.execute(update_query, tuple(params))
        conn.commit()
        conn.close()
