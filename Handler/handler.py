from streamlit import text
from Handler.handler_add import *
from Handler.handler_link import *
from Handler.handler_delete import *
from Handler.handler_search import *
from Handler.handler_update import *
from Handler.handler_list import *
from rbac import check_access

# Функции для обработки сообщений от бота
def handle_message(message):
    try:
        chat_id = message["chat"]["id"]
        text_raw = message["text"]

        # Проверка: если текст не начинается с '/', это не команда
        if not text_raw.startswith("/"):
            return "Пожалуйста, используйте команды, начинающиеся с '/'. Например: /help"

        # Определяем команду (например, /add_client -> add_client)
        command = text_raw.split()[0].lstrip("/")

        # Проверяем доступ
        if not check_access(chat_id, command):
            return "У вас нет прав для выполнения этой команды."

       
    except:
        return "Я не понимаю."
    
    text = text_raw.lower()

    # Словарь команд
    command_handlers = {
        "/addclient": handle_add_client,
        "/addworker": handle_add_worker,
        "/addassembly": handle_add_assembly,
        "/addcomponent": handle_add_component,
        "/addsupplier": handle_add_supplier,

        "/deleteclient": handle_delete_client,
        "/deleteworker": handle_delete_worker,
        "/deleteassembly": handle_delete_assembly,
        "/deletecomponent": handle_delete_component,
        "/deletesupplier": handle_delete_supplier,

        "/linkassemblycomponent": handle_link_assembly_component,
        "/linkcomponentsupplier": handle_link_component_supplier,

        "/start": handle_start,
        "/help": handle_help,
        
        "/listclients": handle_list_clients,
        "/listworkers": handle_list_workers,
        "/listassemblies": handle_list_assemblies,
        "/listcomponents": handle_list_components,
        "/listsuppliers": handle_list_suppliers,

        "/searchclient": handle_search_client,
        "/searchworker": handle_search_worker,
        "/searchassembly": handle_search_assembly,
        "/searchcomponent": handle_search_component,
        "/searchsupplier": handle_search_supplier,

        "/updateclient": handle_update_client,
        "/updateworker": handle_update_worker,
        "/updateassembly": handle_update_assembly,
        "/updatecomponent": handle_update_component,
        "/updatesupplier": handle_update_supplier,
    }

    # Проверяем, есть ли команда в словаре
    for command, handler in command_handlers.items():
        if text.startswith(command):
            return handler(text_raw)
    
    return "Я не понимаю эту команду."


def handle_start(text):
    return "Привет! Я ваш новый бот. Используйте команды для редактирования данных."


def handle_help(text):
    return (
        "Список доступных команд:\n\n"
        "Добавление:\n"
        "/addclient <first_name>, <last_name>, <email>, <phone_number>, <address> - добавить клиента\n"
        "/addworker <first_name>, <last_name>, <position>, <salary> - добавить работника\n"
        "/addassembly <product_name>, <product_description>, <price>, <stock_quantity> - добавить сборку\n"
        "/addcomponent <product_name>, <price>, <description>, <stock_quantity> - добавить комплектующее\n"
        "/addsupplier <supplier_name>, <contact_info> - добавить поставщика\n\n"

        "Обновление:\n"
        "/updateclient <client_id> <field> <new_value> - обновить данные клиента\n"
        "/updateworker <worker_id> <field> <new_value> - обновить данные работника\n"
        "/updateassembly <assembly_id> <field> <new_value> - обновить данные сборки\n"
        "/updatecomponent <component_id> <field> <new_value> - обновить данные комплектующего\n"
        "/updatesupplier <supplier_id> <field> <new_value> - обновить данные поставщика\n\n"

        "Удаление:\n"
        "/deleteclient <client_id> - удалить клиента\n"
        "/deleteworker <worker_id> - удалить работника\n"
        "/deleteassembly <assembly_id> - удалить сборку\n"
        "/deletecomponent <component_id> - удалить комплектующее\n"
        "/deletesupplier <supplier_id> - удалить поставщика\n\n"

        "Связи:\n"
        "/linkassemblycomponent <assembly_id>, <component_id> - связать сборку с комплектующим\n"
        "/linkcomponentsupplier <component_id>, <supplier_id> - связать комплектующий с поставщиком\n\n"

        "Списки:\n"
        "/listclients - список клиентов\n"
        "/listworkers - список работников\n"
        "/listassemblies - список сборок\n"
        "/listcomponents - список комплектующих\n"
        "/listsuppliers - список поставщиков\n\n"

        "Поиск:\n"
        "/searchclient <поисковый_текст> - поиск клиента\n"
        "/searchworker <поисковый_текст> - поиск работника\n"
        "/searchassembly <поисковый_текст> - поиск сборки\n"
        "/searchcomponent <поисковый_текст> - поиск комплектующего\n"
        "/searchsupplier <поисковый_текст> - поиск поставщика\n"
    )

