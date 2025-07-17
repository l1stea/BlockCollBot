from CommandsDB.update import *  # Импортируем функции для обновления
from Handler.commands import *

# Обработчик для обновления сущностей
def handle_update(text, entity_name, update_func, entity_label):
    try:
        # Сначала делим по первому пробелу
        _, rest = text.split(" ", 1)
        # Теперь делим оставшееся по запятым
        parts = rest.strip().split("|")
        if len(parts) < 3 or len(parts[2:]) % 2 != 1:
            return f"Ошибка: команда должна быть в формате '/update{entity_name} <id> | <field> | <value> [| <field> | <value> ...]'."

        entity_id = int(parts[0])
        updates = parts[1:]

        field_dict = {
            updates[i]: updates[i + 1] for i in range(0, len(updates), 2)
        }

        result, response = update_func(entity_id, **field_dict)
        if result is True:
            return f"{entity_label.capitalize()} обновлен!"
        else:
            return f"Ошибка: {response}"
    except Exception as e:
        return f"Ошибка: {str(e)}"

# Конкретные обработчики
@command("/updateclient", description="Обновить клиента. Поля: email (str) | phone (str) | address (str)\nПример: /updateclient 1 | email | new_email | phone | new_phone")
def handle_update_client(text):
    return handle_update(text, "client", update_client, "клиент")

# Обработчик для обновления работников
@command("/updateworker", description="Обновить работника. Поля: email (str) | phone (str) | position_id (int)\nПример: /updateworker 1 | email | new_email | phone | new_phone")
def handle_update_worker(text):
    return handle_update(text, "worker", update_worker, "работник")

# Обработчик для обновления сборок
@command("/updateassembly", description="Обновить сборку. Поля: name (str) | description (str) | price (float)\nПример: /updateassembly 1 | name | new_name | description | new_description | price | new_price")
def handle_update_assembly(text):
    return handle_update(text, "assembly", update_assembly, "сборка")

# Обработчик для обновления комплектующих
@command("/updatecomponent", description="Обновить комплектующий. Поля: name (str) | price (float) | description (str) | stock_quantity (int)\nПример: /updatecomponent 1 | name | new_name | price | new_price | description | new_description | stock | new_stock")
def handle_update_component(text):
    return handle_update(text, "component", update_component, "комплектующий")

# Обработчик для обновления поставщиков
@command("/updatesupplier", description="Обновить поставщика. Поля: email (str) | phone (str) | address (str)\nПример: /updatesupplier 1 | email | new_email | phone | new_phone | address | new_address")
def handle_update_supplier(text):
    return handle_update(text, "supplier", update_supplier, "поставщик")
