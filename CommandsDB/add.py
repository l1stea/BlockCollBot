import mysql.connector
from CommandsDB.db import connect_db

def universal_add(table, fields, values, fk_map=None):
    try:
        conn = connect_db()
        if conn:
            cursor = conn.cursor()
            query = f"INSERT INTO {table} ({', '.join(fields)}) VALUES ({', '.join(['%s'] * len(fields))})"
            cursor.execute(query, tuple(values))
            conn.commit()
            conn.close()
            return True, None
    except mysql.connector.IntegrityError as e:
        error_text = str(e)
        if fk_map:
            for fk_field, fk_text in fk_map.items():
                if fk_text in error_text:
                    return False, fk_field
        return False, str(e)
    except Exception as e:
        return False, str(e)
    return False, None

def add_client(first_name, last_name, email, phone_number, address):
    return universal_add(
        "clients",
        ["first_name", "last_name", "email", "phone_number", "address"],
        [first_name, last_name, email, phone_number, address]
    )

def add_worker(position_id, first_name, last_name, salary, hire_date, chat_id=None):
    return universal_add(
        "employees",
        ["first_name", "last_name", "position_id", "salary", "hire_date", "chat_id"],
        [first_name, last_name, position_id, salary, hire_date, chat_id],
        fk_map={"position_id": "FOREIGN KEY (`position_id`"}
    )

def add_assembly(product_name, product_description, price, stock_quantity):
    return universal_add(
        "computer_builds",
        ["product_name", "product_description", "price", "stock_quantity"],
        [product_name, product_description, price, stock_quantity]
    )

def add_component(product_name, price, description, stock_quantity):
    return universal_add(
        "components",
        ["product_name", "price", "description", "stock_quantity"],
        [product_name, price, description, stock_quantity]
    )

def add_supplier(company_name, contact_name, contact_phone, contact_email):
    return universal_add(
        "suppliers",
        ["company_name", "contact_name", "contact_phone", "contact_email"],
        [company_name, contact_name, contact_phone, contact_email]
    )

def add_sales(employee_id, client_id, product_id, quantity, sale_date, total_price):
    return universal_add(
        "sales",
        ["employee_id", "client_id", "product_id", "quantity", "sale_date", "total_price"],
        [employee_id, client_id, product_id, quantity, sale_date, total_price],
        fk_map={
            "employee_id": "FOREIGN KEY (`employee_id`",
            "client_id": "FOREIGN KEY (`client_id`",
            "product_id": "FOREIGN KEY (`product_id`"
        }
    )

def add_position(position):
    return universal_add(
        "positions",
        ["position"],
        [position]
    )