from CommandsDB.search import *
from Handler.commands import *

# Универсальный обработчик для поиска по базе данных
def handle_search(text, table, fields, format_result):
    try:
        _, search_part = text.split(" ", 1)
        field_filters, keywords = parse_search_terms(search_part)
        results = universal_search(table, fields, keywords, field_filters)
        if not results:
            return ("text", f"{table.capitalize()} не найдены.")
        lines = [format_result(*row) for row in results]
        return ("text", "\n".join(lines))
    except ValueError:
        return ("text", f"Ошибка: команда должна быть в формате '/search{table.lower()} <search_term>'.")
    except Exception as e:
        return ("text", f"Ошибка: {str(e)}")

@command("/searchclient", description="Поиск клиента. Поля: first_name:(str) last_name:(str) email:(str) phone_number:(str) address:(str)\nПример: /searchclient Иван")
def handle_search_client(text):
    return handle_search(
        text,
        "clients",
        ["first_name", "last_name", "email", "phone_number", "address"],
        lambda cid, fname, lname, email, phone, address: f"{cid}: {fname} {lname}, Email: {email}, Телефон: {phone}, Адрес: {address}"
    )

@command("/searchworker", description="Поиск работника. Поля: first_name:(str) last_name:(str) email:(str) phone_number:(str) position_id:(int) chat_id:(int)\nПример: /searchworker Иван")
def handle_search_worker(text):
    return handle_search(
        text,
        "employees",
        ["first_name", "last_name", "position_id", "salary", "hire_date", "chat_id"],
        lambda cid, fname, lname, pos_id, salary, hire_date, chat_id: f"{cid}: {fname} {lname}, Должность ID: {pos_id}, Зарплата: {salary} руб., Дата найма: {hire_date}, ChatID: {chat_id}"
    )

@command("/searchassembly", description="Поиск сборки. Поля: product_name:(str) product_description:(str) price:(float) stock_quantity:(int)\nПример: /searchassembly 1")
def handle_search_assembly(text):
    return handle_search(
        text,
        "computer_builds",
        ["product_name", "product_description", "price", "stock_quantity"],
        lambda aid, name, desc, price, qty: f"{aid}: Название: {name}, Описание: {desc}, Цена: {price} руб., Кол-во: {qty}"
    )

@command("/searchcomponent", description="Поиск комплектующего. Поля: product_name:(str) price:(float) description:(str) stock_quantity:(int)\nПример: /searchcomponent 1")
def handle_search_component(text):
    return handle_search(
        text,
        "components",
        ["product_name", "price", "description", "stock_quantity"],
        lambda cid, name, price, desc, qty: f"{cid}: {name}, Цена: {price} руб., Описание: {desc}, Кол-во: {qty}"
    )

@command("/searchsupplier", description="Поиск поставщика. Поля: company_name:(str) contact_name:(str) contact_phone:(str) contact_email:(str)\nПример: /searchsupplier 1")
def handle_search_supplier(text):
    return handle_search(
        text,
        "suppliers",
        ["company_name", "contact_name", "contact_phone", "contact_email"],
        lambda sid, company, contact, phone, email: f"{sid}: {company}, Контакт: {contact}, Телефон: {phone}, Email: {email}"
    )