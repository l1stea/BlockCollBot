from Handler.commands import *

@command("/start")
def handle_start(text):
    return "Привет! Я ваш новый бот. Используйте команды для редактирования данных."


@command("/help")
def handle_help(text):
    return (
        "Список доступных команд:\n\n"
        "Добавление:\n"
        "/addclient <first_name> | <last_name> | <email> | <phone_number> | <address> - добавить клиента\n"
        "/addworker <position_id> | <first_name> | <last_name> | <salary> | <hire_date> | <chat_id> - добавить работника\n"
        "/addassembly <product_name> | <product_description> | <price> | <stock_quantity> - добавить сборку\n"
        "/addcomponent <product_name> | <price> | <description> | <stock_quantity> - добавить комплектующее\n"
        "/addsupplier <supplier_name> | <contact_info> - добавить поставщика\n\n"

        "Обновление:\n"
        "/updateclient <client_id> | <field> | <new_value> - обновить данные клиента\n"
        "/updateworker <worker_id> | <field> | <new_value> - обновить данные работника\n"
        "/updateassembly <assembly_id> | <field> | <new_value> - обновить данные сборки\n"
        "/updatecomponent <component_id> | <field> | <new_value> - обновить данные комплектующего\n"
        "/updatesupplier <supplier_id> | <field> | <new_value> - обновить данные поставщика\n\n"

        "Удаление:\n"
        "/deleteclient <client_id> - удалить клиента\n"
        "/deleteworker <worker_id> - удалить работника\n"
        "/deleteassembly <assembly_id> - удалить сборку\n"
        "/deletecomponent <component_id> - удалить комплектующее\n"
        "/deletesupplier <supplier_id> - удалить поставщика\n\n"

        "Связи:\n"
        "/linkassemblycomponent <assembly_id> | <component_id> - связать сборку с комплектующим\n"
        "/linkcomponentsupplier <component_id> | <supplier_id> | <supply_date> | <quantity_delivered> - связать комплектующий с поставщиком\n\n"

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
        "/searchsupplier <поисковый_текст> - поиск поставщика"
    )
