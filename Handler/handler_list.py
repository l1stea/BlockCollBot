from CommandsDB.list import *  # Импортируем функции для списка

# Обработчики команд для вывода списка
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


def handle_list_workers(text):
    try:
        workers = list_workers()
        if not workers:
            return "Нет работников в базе данных."
        response = "\n".join(
            f"{worker_id}: {first_name} {last_name}, {position}, {salary} руб."
            for worker_id, first_name, last_name, position, salary in workers
        )
        return response
    except Exception as e:
        return f"Ошибка: {str(e)}"


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


def handle_list_components(text):
    try:
        components = list_components()
        if not components:
            return "Нет комплектующих в базе данных."
        response = "\n".join(
            f"{component_id}: {product_name}, {price} руб., {stock_quantity} шт."
            for component_id, product_name, price, stock_quantity in components
        )
        return response
    except Exception as e:
        return f"Ошибка: {str(e)}"


def handle_list_suppliers(text):
    try:
        suppliers = list_suppliers()
        if not suppliers:
            return "Нет поставщиков в базе данных."
        response = "\n".join(
            f"{supplier_id}: {supplier_name}, {contact_info}"
            for supplier_id, supplier_name, contact_info in suppliers
        )
        return response
    except Exception as e:
        return f"Ошибка: {str(e)}"
    
def handle_list_sales(text):
    try:
        sales = list_sales()
        if not sales:
            return "Нет продаж в базе данных."
        response = "\n".join(
            f"{sale_id}: Работник {employee_id}, Клиент {client_id}, Продукт {product_id}, Количество {quantity}, Дата {sale_date}"
            for sale_id, employee_id, client_id, product_id, quantity, sale_date in sales
        )
        return response
    except Exception as e:
        return f"Ошибка: {str(e)}"
