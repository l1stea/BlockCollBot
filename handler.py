from add import *
from link import *

# Функции для обработки сообщений от бота
def handle_message(message):
    text = message["text"].lower()

    # Словарь команд
    command_handlers = {
        "/addclient": handle_add_client,
        "/addworker": handle_add_worker,
        "/addassembly": handle_add_assembly,
        "/addcomponent": handle_add_component,
        "/addsupplier": handle_add_supplier,
        "/linkassemblycomponent": handle_link_assembly_component,
        "/linkcomponentsupplier": handle_link_component_supplier,
        "/start": handle_start,
        "/help": handle_help,
    }

    # Проверяем, есть ли команда в словаре
    for command, handler in command_handlers.items():
        if text.startswith(command):
            return handler(text)
    
    return "Я не понимаю эту команду."


# Обработчики команд
def handle_add_client(text):
    try:
        _, first_name, last_name, email, phone_number, address = text.split(",", 5)
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

def handle_link_assembly_component(text):
    try:
        _, product_id, component_id = text.split(",", 2)
        link_assembly_component(int(product_id.strip()), int(component_id.strip()))
        return "Сборка и комплектующий связаны!"
    except ValueError:
        return "Ошибка: команда должна быть в формате '/linkassemblycomponent <product_id>, <component_id>'."

def handle_link_component_supplier(text):
    try:
        _, component_id, supplier_id = text.split(",", 2)
        link_component_supplier(int(component_id.strip()), int(supplier_id.strip()))
        return "Комплектующий и поставщик связаны!"
    except ValueError:
        return "Ошибка: команда должна быть в формате '/linkcomponentsupplier <component_id>, <supplier_id>'."

def handle_start(text):
    return "Привет! Я ваш новый бот. Используйте команды для добавления данных."

def handle_help(text):
    return (
        "Список команд:\n"
        "/addclient <first_name>, <last_name>, <email>, <phone_number>, <address> - добавить клиента\n"
        "/addworker <first_name>, <last_name>, <position>, <salary> - добавить работника\n"
        "/addassembly <product_name>, <product_description>, <price>, <stock_quantity> - добавить сборку\n"
        "/addcomponent <product_name>, <price>, <stock_quantity> - добавить комплектующий\n"
        "/addsupplier <supplier_name>, <contact_info> - добавить поставщика\n"
        "/linkassemblycomponent <product_id>, <component_id> - связать сборку с комплектующим\n"
        "/linkcomponentsupplier <component_id>, <supplier_id> - связать комплектующий с поставщиком"
    )
