import pandas as pd
from Handler.commands import command

@command("/exportclients")
def handle_export_clients_to_excel(file_path="clients.xlsx"):
    file_path = file_path.replace("/export", "").replace("export", "")
    if not file_path.lower().endswith(".xlsx"):
        file_path += ".xlsx"
    from CommandsDB.list import list_clients
    data = list_clients()
    columns = ["ID", "Имя", "Фамилия", "Email", "Телефон", "Адрес"]
    try:
        df = pd.DataFrame(data, columns=columns)
        df.to_excel(file_path, index=False)
        return True, file_path
    except Exception as e:
        return False, str(e)
    
@command("/exportfinancials")
def handle_export_financials_to_excel(file_path="financials.xlsx"):
    file_path = file_path.replace("/export", "").replace("export", "")
    if not file_path.lower().endswith(".xlsx"):
        file_path += ".xlsx"
    from CommandsDB.list import list_financials
    data = list_financials()
    columns = ["ID", "Дата", "Сумма", "Описание"]
    try:
        df = pd.DataFrame(data, columns=columns)
        df.to_excel(file_path, index=False)
        return True, file_path
    except Exception as e:
        return False, str(e)
