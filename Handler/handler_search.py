from CommandsDB.search import *

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
def handle_search_client(text):
    return handle_search(
        text,
        search_client,
        "Клиент",
        lambda cid, fname, lname, email, phone, address:
            f"{cid}: {fname} {lname}, {email}, {phone}, {address}"
    )

def handle_search_worker(text):
    return handle_search(
        text,
        search_worker,
        "Работник",
        lambda wid, fname, lname, pos, sal:
            f"{wid}: {fname} {lname}, Должность: {pos}, Зарплата: {sal} руб."
    )

def handle_search_assembly(text):
    return handle_search(
        text,
        search_assembly,
        "Сборка",
        lambda aid, name, desc, price:
            f"{aid}: Название: {name}, Описание: {desc}, Цена: {price} руб."
    )

def handle_search_component(text):
    return handle_search(
        text,
        search_component,
        "Комплектующее",
        lambda cid, name, type_, qty, price:
            f"{cid}: {name}, Тип: {type_}, Кол-во: {qty}, Цена: {price} руб."
    )

def handle_search_supplier(text):
    return handle_search(
        text,
        search_supplier,
        "Поставщик",
        lambda sid, name, email, phone, address:
            f"{sid}: {name}, Email: {email}, Телефон: {phone}, Адрес: {address}"
    )
