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