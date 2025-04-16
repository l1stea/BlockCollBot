from CommandsDB.list import *  # Импортируем функции для списка

# Обработчики команд для вывода списка
def handle_list_clients(text):
    try:
        response = list_clients()  # Вызов функции для получения списка клиентов
        if not response:
            return "Нет клиентов в базе данных."
        return response
    except Exception as e:
        return f"Ошибка: {str(e)}"

def handle_list_workers(text):
    try:
        response = list_workers()  # Вызов функции для получения списка работников
        if not response:
            return "Нет работников в базе данных."
        return response
    except Exception as e:
        return f"Ошибка: {str(e)}"

def handle_list_assemblies(text):
    try:
        response = list_assemblies()  # Вызов функции для получения списка сборок
        if not response:
            return "Нет сборок в базе данных."
        return response
    except Exception as e:
        return f"Ошибка: {str(e)}"

def handle_list_components(text):
    try:
        response = list_components()  # Вызов функции для получения списка комплектующих
        if not response:
            return "Нет комплектующих в базе данных."
        return response
    except Exception as e:
        return f"Ошибка: {str(e)}"

def handle_list_suppliers(text):
    try:
        response = list_suppliers()  # Вызов функции для получения списка поставщиков
        if not response:
            return "Нет поставщиков в базе данных."
        return response
    except Exception as e:
        return f"Ошибка: {str(e)}"
