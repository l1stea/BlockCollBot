from CommandsDB.list import *  # Импортируем функции для списка
from Handler.commands import *

# Обработчики команд для вывода списка
@command("/listclients")
def handle_list_clients(text):
    try:
        clients = list_clients()
        if not clients:
            return "Нет клиентов в базе данных."
        response = "\n".join(
            f"{client_id}: {first_name} {last_name}, {email}, {phone_number}, {address}"
            for client_id, first_name, last_name, email, phone_number, address in clients
        )
        return response
    except Exception as e:
        return f"Ошибка: {str(e)}"

@command("/listworkers")
def handle_list_workers(text):
    try:
        workers = list_workers()
        if not workers:
            return "Нет работников в базе данных."
        response = "\n".join(
            f"{worker_id}: {first_name} {last_name}, {position_id}, {salary} руб., {hire_date}, {chat_id}"
            for worker_id, position_id, first_name, last_name, salary, hire_date, chat_id in workers
        )
        return response
    except Exception as e:
        return f"Ошибка: {str(e)}"

@command("/listassemblies")
def handle_list_assemblies(text):
    try:
        assemblies = list_assemblies()
        if not assemblies:
            return "Нет сборок в базе данных."
        response = "\n".join(
            f"{product_id}: {product_name}, {product_description}, {price} руб., {stock_quantity} шт."
            for product_id, product_name, product_description, price, stock_quantity in assemblies
        )
        return response
    except Exception as e:
        return f"Ошибка: {str(e)}"

@command("/listcomponents")
def handle_list_components(text):
    try:
        components = list_components()
        if not components:
            return "Нет комплектующих в базе данных."
        response = "\n".join(
            f"{component_id}: {product_name}, {price} руб., {description}, {stock_quantity} шт."
            for component_id, product_name, price, description, stock_quantity in components
        )
        return response
    except Exception as e:
        return f"Ошибка: {str(e)}"

@command("/listsuppliers")
def handle_list_suppliers(text):
    try:
        suppliers = list_suppliers()
        if not suppliers:
            return "Нет поставщиков в базе данных."
        response = "\n".join(
            f"{supplier_id}: {company_name}, {contact_name}, {contact_phone}, {contact_email}"
            for supplier_id, company_name, contact_name, contact_phone, contact_email in suppliers
        )
        return response
    except Exception as e:
        return f"Ошибка: {str(e)}"
    
@command("/listsales")  
def handle_list_sales(text):
    try:
        sales = list_sales()
        if not sales:
            return "Нет продаж в базе данных."
        response = "\n".join(
            f"{sale_id}: Работник {employee_id}, Клиент {client_id}, Продукт {product_id}, Количество {quantity}, Дата {sale_date}, Итого {total_price} руб."
            for sale_id, employee_id, client_id, product_id, sale_date, quantity, total_price in sales
        )
        return response
    except Exception as e:
        return f"Ошибка: {str(e)}"
    
@command("/listpositions")
def handle_list_positions(text):
    try:
        positions = list_positions()
        if not positions:
            return "Нет позиций в базе данных."
        response = "\n".join(
            f"{position_id}: {position}"
            for position_id, position in positions
        )
        return response
    except Exception as e:
        return f"Ошибка: {str(e)}"
