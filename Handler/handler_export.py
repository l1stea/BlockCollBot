from openpyxl import Workbook
from Handler.commands import command

@command("/exportclients", description="Экспортировать список клиентов в Excel.")
def handle_export_clients_to_excel(file_path="clients.xlsx"):
    file_path = file_path.replace("/export", "").replace("export", "")
    if not file_path.lower().endswith(".xlsx"):
        file_path += ".xlsx"
    from CommandsDB.list import list_clients
    data = list_clients()
    columns = ["ID", "Имя", "Фамилия", "Email", "Телефон", "Адрес"]
    try:
        wb = Workbook()
        ws = wb.active
        ws.append(columns)
        for row in data:
            ws.append(row)
        wb.save(file_path)
        return ("document", file_path, "Список клиентов")
    except Exception as e:
        return ("text", str(e))

@command("/exportfinancials", description="Экспортировать финансовые данные в Excel.")
def handle_export_financials_to_excel(file_path="financials.xlsx"):
    file_path = file_path.replace("/export", "").replace("export", "")
    if not file_path.lower().endswith(".xlsx"):
        file_path += ".xlsx"
    from CommandsDB.list import list_financials
    data = list_financials()

    IDX_ID = 0
    IDX_EMPLOYEE = 1
    IDX_CLIENT = 2
    IDX_PRODUCT = 3
    IDX_DATE = 4
    IDX_QUANTITY = 5
    IDX_SUM = 6

    export_data = [
        [
            row[IDX_ID],
            row[IDX_DATE],
            row[IDX_SUM],
            f"Employee: {row[IDX_EMPLOYEE]}, Client: {row[IDX_CLIENT]}, Product: {row[IDX_PRODUCT]}, Quantity: {row[IDX_QUANTITY]}"
        ]
        for row in data
    ]
    columns = ["ID", "Дата", "Сумма", "Описание"]
    try:
        wb = Workbook()
        ws = wb.active
        ws.append(columns)
        for row in export_data:
            ws.append(row)
        wb.save(file_path)
        return ("document", file_path, "Финансовый отчет")
    except Exception as e:
        return ("text", str(e))