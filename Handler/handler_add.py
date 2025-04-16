from CommandsDB.add import *

# Обработчики команд
def handle_add_client(text):
    try:
        # Сначала делим по первому пробелу
        _, rest = text.split(" ", 1)
        # Теперь делим оставшееся по запятым
        first_name, last_name, email, phone_number, address = rest.split(",", 4)
        add_client(first_name.strip(), last_name.strip(), email.strip(), phone_number.strip(), address.strip())
        return "Клиент добавлен!"
    except ValueError:
        return "Ошибка: команда должна быть в формате '/addclient <first_name>, <last_name>, <email>, <phone_number>, <address>'."

def handle_add_worker(text):
    try:
        _, first_name, last_name, position, salary = text.split(",", 4)
        add_worker(first_name.strip(), last_name.strip(), position.strip(), float(salary.strip()))
        return "Работник добавлен!"
    except ValueError:
        return "Ошибка: команда должна быть в формате '/addworker <first_name>, <last_name>, <position>, <salary>'."

def handle_add_assembly(text):
    try:
        _, product_name, product_description, price, stock_quantity = text.split(",", 4)
        add_assembly(product_name.strip(), product_description.strip(), float(price.strip()), int(stock_quantity.strip()))
        return "Сборка добавлена!"
    except ValueError:
        return "Ошибка: команда должна быть в формате '/addassembly <product_name>, <product_description>, <price>, <stock_quantity>'."

def handle_add_component(text):
    try:
        _, product_name, price, stock_quantity = text.split(",", 3)
        add_component(product_name.strip(), float(price.strip()), int(stock_quantity.strip()))
        return "Комплектующий добавлен!"
    except ValueError:
        return "Ошибка: команда должна быть в формате '/addcomponent <product_name>, <price>, <stock_quantity>'."

def handle_add_supplier(text):
    try:
        _, supplier_name, contact_info = text.split(",", 2)
        add_supplier(supplier_name.strip(), contact_info.strip())
        return "Поставщик добавлен!"
    except ValueError:
        return "Ошибка: команда должна быть в формате '/addsupplier <supplier_name>, <contact_info>'."