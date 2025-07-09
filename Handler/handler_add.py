from CommandsDB.add import *

def handle_add(text, entity_label, expected_fields, convert_fields, add_func):
    try:
        _, data = text.split(" ", 1)
        parts = [p.strip() for p in data.split(",", len(expected_fields) - 1)]
        if len(parts) != len(expected_fields):
            raise ValueError("count")
        try:
            converted = [conv(p) for conv, p in zip(convert_fields, parts)]
        except Exception:
            raise ValueError("type")
        result, wrong_field = add_func(*converted)
        if result is False:
            return f"Ошибка при добавлении {entity_label.lower()}: проверьте корректность связанных данных ({wrong_field})."
        return f"{entity_label} добавлен!"
    except ValueError as ve:
        fields_str = ", ".join(f"<{f}>" for f in expected_fields)
        if str(ve) == "count":
            return f"Ошибка: команда должна быть в формате '/add{entity_label.lower()} {fields_str}'."
        elif str(ve) == "type":
            return f"Ошибка: неверный тип данных. Проверьте правильность ввода для: {fields_str}."
        else:
            return f"Ошибка: команда должна быть в формате '/add{entity_label.lower()} {fields_str}'."
    except Exception as e:
        return f"Ошибка при добавлении: {e}"

def handle_add_client(text):
    return handle_add(
        text,
        "\"Клиент\"",
        ["first_name", "last_name", "email", "phone_number", "address"],
        [str, str, str, str, str],
        add_client
    )

def handle_add_worker(text):
    return handle_add(
        text,
        "\"Работник\"",
        ["first_name", "last_name", "position", "salary"],
        [str, str, str, float],
        add_worker
    )

def handle_add_assembly(text):
    return handle_add(
        text,
        "\"Сборка\"",
        ["product_name", "product_description", "price", "stock_quantity"],
        [str, str, float, int],
        add_assembly
    )

def handle_add_component(text):
    return handle_add(
        text,
        "\"Комплектующий\"",
        ["product_name", "price", "stock_quantity"],
        [str, float, int],
        add_component
    )

def handle_add_supplier(text):
    return handle_add(
        text,
        "\"Поставщик\"",
        ["supplier_name", "contact_info"],
        [str, str],
        add_supplier
    )

def to_mysql_date(date_str):
    """
    Преобразует дату в формат 'YYYY-MM-DD'.
    Поддерживает форматы:
    'DD.MM.YYYY', 'YYYY-MM-DD', 'DD/MM/YYYY', 'DD-MM-YYYY', 'YYYY/MM/DD', 'YYYY.MM.DD'
    """
    import datetime

    date_str = date_str.strip()
    formats = [
        "%d.%m.%Y",
        "%Y-%m-%d",
        "%d/%m/%Y",
        "%d-%m-%Y",
        "%Y/%m/%d",
        "%Y.%m.%d"
    ]
    for fmt in formats:
        try:
            return datetime.datetime.strptime(date_str, fmt).strftime("%Y-%m-%d")
        except ValueError:
            continue
    raise ValueError("type")  # Для универсальной обработки ошибки в handle_add

def handle_add_sale(text):
    return handle_add(
        text,
        "\"Продажа\"",
        ["employee_id", "client_id", "product_id", "quantity", "sale_date", "total_price"],
        [int, int, int, int, to_mysql_date, float],
        add_sales
    )
