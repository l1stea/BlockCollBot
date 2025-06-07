from CommandsDB.update import *  # Импортируем функции для обновления

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
        if not response:
            return f"Ошибка: не удалось обновить {entity_label}."
        
        return f"{entity_label.capitalize()} обновлен!"
    except ValueError:
        return f"Ошибка: ID должен быть числом. Формат: '/update{entity_name} <id> <field> <value> ...'."
    except Exception as e:
        return f"Ошибка: {str(e)}"

# Конкретные обработчики
def handle_update_client(text):
    return handle_update(text, "client", update_client, "клиент")

def handle_update_worker(text):
    return handle_update(text, "worker", update_worker, "работник")

def handle_update_assembly(text):
    return handle_update(text, "assembly", update_assembly, "сборка")

def handle_update_component(text):
    return handle_update(text, "component", update_component, "комплектующий")

def handle_update_supplier(text):
    return handle_update(text, "supplier", update_supplier, "поставщик")
