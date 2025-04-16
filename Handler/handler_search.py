from CommandsDB.search import *  # Импортируем функции для поиска

# Обработчики команд для поиска
def handle_search_client(text):
    try:
        # Получаем данные после команды /searchclient
        _, search_term = text.split(" ", 1)
        response = search_client(search_term.strip())  # Вызов функции поиска клиента
        if not response:
            return "Клиент не найден."
        return response
    except ValueError:
        return "Ошибка: команда должна быть в формате '/searchclient <search_term>'."
    except Exception as e:
        return f"Ошибка: {str(e)}"

def handle_search_worker(text):
    try:
        # Получаем данные после команды /searchworker
        _, search_term = text.split(" ", 1)
        response = search_worker(search_term.strip())  # Вызов функции поиска работника
        if not response:
            return "Работник не найден."
        return response
    except ValueError:
        return "Ошибка: команда должна быть в формате '/searchworker <search_term>'."
    except Exception as e:
        return f"Ошибка: {str(e)}"

def handle_search_assembly(text):
    try:
        # Получаем данные после команды /searchassembly
        _, search_term = text.split(" ", 1)
        response = search_assembly(search_term.strip())  # Вызов функции поиска сборки
        if not response:
            return "Сборка не найдена."
        return response
    except ValueError:
        return "Ошибка: команда должна быть в формате '/searchassembly <search_term>'."
    except Exception as e:
        return f"Ошибка: {str(e)}"

def handle_search_component(text):
    try:
        # Получаем данные после команды /searchcomponent
        _, search_term = text.split(" ", 1)
        response = search_component(search_term.strip())  # Вызов функции поиска комплектующего
        if not response:
            return "Комплектующее не найдено."
        return response
    except ValueError:
        return "Ошибка: команда должна быть в формате '/searchcomponent <search_term>'."
    except Exception as e:
        return f"Ошибка: {str(e)}"

def handle_search_supplier(text):
    try:
        # Получаем данные после команды /searchsupplier
        _, search_term = text.split(" ", 1)
        response = search_supplier(search_term.strip())  # Вызов функции поиска поставщика
        if not response:
            return "Поставщик не найден."
        return response
    except ValueError:
        return "Ошибка: команда должна быть в формате '/searchsupplier <search_term>'."
    except Exception as e:
        return f"Ошибка: {str(e)}"
