from CommandsDB.search import *
from Handler.commands import *

# Обработчик для поиска по базе данных
def handle_search(text, search_func, entity_label, format_result):
    try:
        _, search_terms = text.split(" ", 1)
        terms = [term.strip() for term in search_terms.split()]
        all_results = []
        for term in terms:
            results = search_func(term)
            all_results.extend(results)

        # Убираем дубликаты (если один и тот же результат попал дважды)
        unique_results = list({tuple(r) for r in all_results})

        if not unique_results:
            return f"{entity_label} не найден."

        return "\n".join(format_result(*r) for r in unique_results)
    except ValueError:
        return f"Ошибка: команда должна быть в формате '/search{entity_label.lower()} <search_term>'."  
    except Exception as e:
        return f"Ошибка: {str(e)}"

# Остальные обработчики остаются теми же:
@command("/searchclient", description="Поиск клиента. Пример: /searchclient Иван")
def handle_search_client(text):
    return handle_search(
        text,
        search_client,
        "client",
        lambda cid, fname, lname, email, phone, address:
            f"{cid}: {fname} {lname}, {email}, {phone}, {address}"
    )

# Обработчик для поиска работников
@command("/searchworker", description="Поиск работника. Пример: /searchworker Иван")
def handle_search_worker(text):
    return handle_search(
        text,
        search_worker,
        "worker",
        lambda wid, fname, lname, position_id, salary, hire_date, chat_id:
            f"{wid}: {fname} {lname}, Должность ID: {position_id}, Зарплата: {salary} руб., Дата найма: {hire_date}, ChatID: {chat_id}"
    )

# Обработчик для поиска сборок
@command("/searchassembly", description="Поиск сборки. Пример: /searchassembly 1")
def handle_search_assembly(text):
    return handle_search(
        text,
        search_assembly,
        "assembly",
        lambda aid, name, desc, price:
            f"{aid}: Название: {name}, Описание: {desc}, Цена: {price} руб."
    )

# Обработчик для поиска комплектующих
@command("/searchcomponent", description="Поиск комплектующего. Пример: /searchcomponent 1")
def handle_search_component(text):
    return handle_search(
        text,
        search_component,
        "component",
        lambda cid, name, type_, qty, price:
            f"{cid}: {name}, Тип: {type_}, Кол-во: {qty}, Цена: {price} руб."
    )

# Обработчик для поиска поставщиков
@command("/searchsupplier", description="Поиск поставщика. Пример: /searchsupplier 1")
def handle_search_supplier(text):
    return handle_search(
        text,
        search_supplier,
        "supplier",
        lambda sid, name, email, phone, address:
            f"{sid}: {name}, Email: {email}, Телефон: {phone}, Адрес: {address}"
    )
