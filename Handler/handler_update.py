from CommandsDB.update import *  # Импортируем функции для обновления

# Обработчики команд для обновления
def handle_update_client(text):
    try:
        # Получаем данные после команды /updateclient
        _, client_id, field, new_value = text.split(" ", 3)
        client_id = int(client_id.strip())  # Преобразуем ID в целое число
        new_value = new_value.strip()  # Убираем лишние пробелы
        response = update_client(client_id, field.strip(), new_value)
        if not response:
            return "Ошибка: не удалось обновить клиента."
        return "Клиент обновлен!"
    except ValueError:
        return "Ошибка: команда должна быть в формате '/updateclient <client_id> <field> <new_value>'."
    except Exception as e:
        return f"Ошибка: {str(e)}"

def handle_update_worker(text):
    try:
        # Получаем данные после команды /updateworker
        _, worker_id, field, new_value = text.split(" ", 3)
        worker_id = int(worker_id.strip())  # Преобразуем ID в целое число
        response = update_worker(worker_id, field.strip(), new_value.strip())
        if not response:
            return "Ошибка: не удалось обновить работника."
        return "Работник обновлен!"
    except ValueError:
        return "Ошибка: команда должна быть в формате '/updateworker <worker_id> <field> <new_value>'."
    except Exception as e:
        return f"Ошибка: {str(e)}"

def handle_update_assembly(text):
    try:
        # Получаем данные после команды /updateassembly
        _, assembly_id, field, new_value = text.split(" ", 3)
        assembly_id = int(assembly_id.strip())  # Преобразуем ID в целое число
        response = update_assembly(assembly_id, field.strip(), new_value.strip())
        if not response:
            return "Ошибка: не удалось обновить сборку."
        return "Сборка обновлена!"
    except ValueError:
        return "Ошибка: команда должна быть в формате '/updateassembly <assembly_id> <field> <new_value>'."
    except Exception as e:
        return f"Ошибка: {str(e)}"

def handle_update_component(text):
    try:
        # Получаем данные после команды /updatecomponent
        _, component_id, field, new_value = text.split(" ", 3)
        component_id = int(component_id.strip())  # Преобразуем ID в целое число
        response = update_component(component_id, field.strip(), new_value.strip())
        if not response:
            return "Ошибка: не удалось обновить комплектующий."
        return "Комплектующий обновлен!"
    except ValueError:
        return "Ошибка: команда должна быть в формате '/updatecomponent <component_id> <field> <new_value>'."
    except Exception as e:
        return f"Ошибка: {str(e)}"

def handle_update_supplier(text):
    try:
        # Получаем данные после команды /updatesupplier
        _, supplier_id, field, new_value = text.split(" ", 3)
        supplier_id = int(supplier_id.strip())  # Преобразуем ID в целое число
        response = update_supplier(supplier_id, field.strip(), new_value.strip())
        if not response:
            return "Ошибка: не удалось обновить поставщика."
        return "Поставщик обновлен!"
    except ValueError:
        return "Ошибка: команда должна быть в формате '/updatesupplier <supplier_id> <field> <new_value>'."
    except Exception as e:
        return f"Ошибка: {str(e)}"
