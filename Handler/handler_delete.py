from CommandsDB.delete import *

def handle_delete_client(text):
    try:
        _, client_id = text.split(" ", 1)
        delete_client(int(client_id.strip()))
        return "Клиент удалён!"
    except ValueError:
        return "Ошибка: команда должна быть в формате '/deleteclient <id>'."

def handle_delete_worker(text):
    try:
        _, worker_id = text.split(" ", 1)
        delete_worker(int(worker_id.strip()))
        return "Работник удалён!"
    except ValueError:
        return "Ошибка: команда должна быть в формате '/deleteworker <id>'."

def handle_delete_assembly(text):
    try:
        _, assembly_id = text.split(" ", 1)
        delete_assembly(int(assembly_id.strip()))
        return "Сборка удалена!"
    except ValueError:
        return "Ошибка: команда должна быть в формате '/deleteassembly <id>'."

def handle_delete_component(text):
    try:
        _, component_id = text.split(" ", 1)
        delete_component(int(component_id.strip()))
        return "Комплектующий удалён!"
    except ValueError:
        return "Ошибка: команда должна быть в формате '/deletecomponent <id>'."

def handle_delete_supplier(text):
    try:
        _, supplier_id = text.split(" ", 1)
        delete_supplier(int(supplier_id.strip()))
        return "Поставщик удалён!"
    except ValueError:
        return "Ошибка: команда должна быть в формате '/deletesupplier <id>'."
