from CommandsDB.add import *

def handle_add(text, entity_label, expected_fields, convert_fields, add_func):
    try:
        _, data = text.split(" ", 1)
        parts = [p.strip() for p in data.split(",", len(expected_fields) - 1)]
        if len(parts) != len(expected_fields):
            raise ValueError
        converted = [conv(p) for conv, p in zip(convert_fields, parts)]
        add_func(*converted)
        return f"{entity_label} добавлен!"
    except ValueError:
        fields_str = ", ".join(f"<{f}>" for f in expected_fields)
        return f"Ошибка: команда должна быть в формате '/add{entity_label.lower()} {fields_str}'."

def handle_add_client(text):
    return handle_add(
        text,
        "Клиент",
        ["first_name", "last_name", "email", "phone_number", "address"],
        [str, str, str, str, str],
        add_client
    )

def handle_add_worker(text):
    return handle_add(
        text,
        "Работник",
        ["first_name", "last_name", "position", "salary"],
        [str, str, str, float],
        add_worker
    )

def handle_add_assembly(text):
    return handle_add(
        text,
        "Сборка",
        ["product_name", "product_description", "price", "stock_quantity"],
        [str, str, float, int],
        add_assembly
    )

def handle_add_component(text):
    return handle_add(
        text,
        "Комплектующий",
        ["product_name", "price", "stock_quantity"],
        [str, float, int],
        add_component
    )

def handle_add_supplier(text):
    return handle_add(
        text,
        "Поставщик",
        ["supplier_name", "contact_info"],
        [str, str],
        add_supplier
    )
