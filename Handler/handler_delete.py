from CommandsDB.delete import *
from Handler.commands import *

# Универсальный обработчик удаления
def make_delete_handler(entity_name, delete_func, description):
    @command(f"/delete{entity_name}", description=description)
    def handler(text):
        try:
            _, entity_id = text.split(" ", 1)
            result = delete_func(int(entity_id.strip()))
            if result is True:
                return f"{entity_name.capitalize()} удалён!"
            elif result is False:
                return f"{entity_name.capitalize()} с таким ID не найден."
            else:
                return result  # Например, "Связанные данные: удаление невозможно"
        except ValueError:
            return f"Ошибка: команда должна быть в формате '/delete{entity_name} <id>'."
    return handler

# Регистрируем обработчики для всех сущностей
make_delete_handler("client", delete_client, "Удалить клиента. Поля: id (int)\nПример: /deleteclient 1")
make_delete_handler("worker", delete_worker, "Удалить работника. Поля: id (int)\nПример: /deleteworker 1")
make_delete_handler("assembly", delete_assembly, "Удалить сборку. Поля: id (int)\nПример: /deleteassembly 1")
make_delete_handler("component", delete_component, "Удалить комплектующее. Поля: id (int)\nПример: /deletecomponent 1")
make_delete_handler("supplier", delete_supplier, "Удалить поставщика. Поля: id (int)\nПример: /deletesupplier 1")