from CommandsDB.update import *  # Импортируем функции для обновления
from Handler.commands import *

# Обработчик для обновления сущностей
def handle_update(text, entity_name, update_func, entity_label):
    try:
        parts = text.strip().split()
        if len(parts) < 4 or len(parts[2:]) % 2 != 0:
            return f"Ошибка: команда должна быть в формате '/update{entity_name} <id> <field> <value> [<field> <value> ...]'."

        entity_id = int(parts[1])
        updates = parts[2:]

        field_dict = {
            updates[i]: updates[i + 1] for i in range(0, len(updates), 2)
        }

        response = update_func(entity_id, **field_dict)
        if response is True:
            return f"{entity_label.capitalize()} обновлен!"
        elif isinstance(response, str):
            return f"Ошибка: {response}"
        else:
            return f"Ошибка: не удалось обновить {entity_label}."
    except ValueError:
        return f"Ошибка: ID должен быть числом. Формат: '/update{entity_name} <id> <field> <value> ...'."
    except Exception as e:
        return f"Ошибка: {str(e)}"

# Конкретные обработчики
@command("/updateclient")
def handle_update_client(text):
    return handle_update(text, "client", update_client, "клиент")

# Обработчик для обновления работников
@command("/updateworker")
def handle_update_worker(text):
    return handle_update(text, "worker", update_worker, "работник")

# Обработчик для обновления сборок
@command("/updateassembly")
def handle_update_assembly(text):
    return handle_update(text, "assembly", update_assembly, "сборка")

# Обработчик для обновления комплектующих
@command("/updatecomponent")
def handle_update_component(text):
    return handle_update(text, "component", update_component, "комплектующий")

# Обработчик для обновления поставщиков
@command("/updatesupplier")
def handle_update_supplier(text):
    return handle_update(text, "supplier", update_supplier, "поставщик")
