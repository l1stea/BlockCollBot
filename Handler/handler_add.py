from CommandsDB.add import *
from Converter.converter import to_mysql_date
from Handler.commands import *

def handle_add(text, entity_label, expected_fields, convert_fields, add_func):
    try:
        _, data = text.split(" ", 1)
        parts = [p.strip() for p in data.split("|", len(expected_fields) - 1)]
        if len(parts) != len(expected_fields):
            raise ValueError("count")
        try:
            converted = [conv(p) for conv, p in zip(convert_fields, parts)]
        except Exception:
            raise ValueError("type")
        result, wrong_field = add_func(*converted)
        if result is False:
            return f"Ошибка при добавлении {entity_label.lower()}: проверьте корректность данных ({wrong_field})."
        return f"{entity_label} добавлен!"
    except ValueError as ve:
        fields_str = " | ".join(f"<{f}>" for f in expected_fields)
        if str(ve) == "count":
            return f"Ошибка: команда должна быть в формате '/add{entity_label.lower()} {fields_str}'."
        elif str(ve) == "type":
            return f"Ошибка: неверный тип данных. Проверьте правильность ввода для: {fields_str}."
        else:
            return f"Ошибка: команда должна быть в формате '/add{entity_label.lower()} {fields_str}'."
    except Exception as e:
        return f"Ошибка при добавлении: {e}"

@command("/addclient")
def handle_add_client(text):
    return handle_add(
        text,
        "client",
        ["first_name", "last_name", "email", "phone_number", "address"],
        [str, str, str, str, str],
        add_client
    )

@command("/addworker")
def handle_add_worker(text):
    return handle_add(
        text,
        "worker",
        ["position_id", "first_name", "last_name", "salary", "hire_date", "chat_id"],
        [int, str, str, float, to_mysql_date, int],
        add_worker
    )

@command("/addassembly")
def handle_add_assembly(text):
    return handle_add(
        text,
        "assembly",
        ["product_name", "product_description", "price", "stock_quantity"],
        [str, str, float, int],
        add_assembly
    )

@command("/addcomponent")
def handle_add_component(text):
    return handle_add(
        text,
        "component",
        ["product_name", "price", "description", "stock_quantity"],
        [str, float, str, int],
        add_component
    )

@command("/addsupplier")
def handle_add_supplier(text):
    return handle_add(
        text,
        "supplier",
        ["company_name", "contact_name", "contact_phone", "contact_email"],
        [str, str, str, str],
        add_supplier
    )

@command("/addsale")
def handle_add_sale(text):
    return handle_add(
        text,
        "sale",
        ["employee_id", "client_id", "product_id", "quantity", "sale_date", "total_price"],
        [int, int, int, int, to_mysql_date, float],
        add_sales
    )

@command("/addposition")
def handle_add_position(text):
    return handle_add(
        text,
        "position",
        ["position"],
        [str],
        add_position
    )
