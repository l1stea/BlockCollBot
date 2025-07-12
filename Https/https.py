import os
import requests
import config
from Handler.handler import handle_message
from Handler.handler_export import handle_export_clients_to_excel

timeout = 60

# Глобальный словарь для хранения текста по chat_id и message_id
PAGINATED_TEXTS = {}

def send_message(chat_id, text, page=0, page_size=50):
    # Разбиваем текст на строки
    lines = text.split('\n')
    # Формируем страницы по page_size строк
    pages = ['\n'.join(lines[i:i+page_size]) for i in range(0, len(lines), page_size)]
    total_pages = len(pages)
    if page < 0:
        page = 0
    if page >= total_pages:
        page = total_pages - 1 if total_pages > 0 else 0
    reply_markup = None
    if total_pages > 1:
        buttons = []
        if page > 0:
            buttons.append({"text": "<", "callback_data": f"page_{page-1}"})
        if page < total_pages - 1:
            buttons.append({"text": ">", "callback_data": f"page_{page+1}"})
        reply_markup = {"inline_keyboard": [buttons]}
    url = f"https://api.telegram.org/bot{config.TELEGRAM_TOKEN}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": pages[page] if total_pages > 0 else ""
    }
    if reply_markup:
        import json
        params["reply_markup"] = json.dumps(reply_markup)
    try:
        response = requests.get(url, params=params, timeout=timeout)
        response.raise_for_status()
        message_id = response.json().get("result", {}).get("message_id")
        if message_id:
            PAGINATED_TEXTS[(chat_id, message_id)] = text
        return message_id
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при отправке сообщения: {e}")
        return None

def edit_message(chat_id, message_id, page=0, page_size=50):
    text = PAGINATED_TEXTS.get((chat_id, message_id), "")
    lines = text.split('\n')
    pages = ['\n'.join(lines[i:i+page_size]) for i in range(0, len(lines), page_size)]
    total_pages = len(pages)
    if page < 0:
        page = 0
    if page >= total_pages:
        page = total_pages - 1 if total_pages > 0 else 0
    reply_markup = None
    if total_pages > 1:
        buttons = []
        if page > 0:
            buttons.append({"text": "<", "callback_data": f"page_{page-1}"})
        if page < total_pages - 1:
            buttons.append({"text": ">", "callback_data": f"page_{page+1}"})
        reply_markup = {"inline_keyboard": [buttons]}
    url = f"https://api.telegram.org/bot{config.TELEGRAM_TOKEN}/editMessageText"
    params = {
        "chat_id": chat_id,
        "message_id": message_id,
        "text": pages[page] if total_pages > 0 else ""
    }
    if reply_markup:
        import json
        params["reply_markup"] = json.dumps(reply_markup)
    try:
        requests.get(url, params=params, timeout=timeout)
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при редактировании сообщения: {e}")

def get_updates(offset=None):
    url = f"https://api.telegram.org/bot{config.TELEGRAM_TOKEN}/getUpdates"
    params = {"offset": offset, "timeout": 60}
    try:
        response = requests.get(url, params=params, timeout=timeout)
        response.raise_for_status()
        updates = response.json()["result"]
        for update in updates:
            if "callback_query" in update:
                chat_id = update["callback_query"]["message"]["chat"]["id"]
                message_id = update["callback_query"]["message"]["message_id"]
                data = update["callback_query"]["data"]
                if data.startswith("page_"):
                    page = int(data.split("_")[1])
                    edit_message(chat_id, message_id, page=page)
                offset = update["update_id"] + 1
            elif "message" in update:
                chat_id = update["message"]["chat"]["id"]
                text = update["message"].get("text", "")
                if "/export" in text or "export" in text:
                    handle_export(chat_id, text)
                else:
                    response_text = handle_message(update["message"])
                    send_message(chat_id, response_text)
                offset = update["update_id"] + 1
        return offset
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при получении обновлений: {e}")
        return offset

def send_document(chat_id, file_path, caption=None):
    url = f"https://api.telegram.org/bot{config.TELEGRAM_TOKEN}/sendDocument"
    with open(file_path, "rb") as f:
        files = {"document": f}
        data = {"chat_id": chat_id}
        if caption:
            data["caption"] = caption
        try:
            response = requests.post(url, data=data, files=files, timeout=timeout)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при отправке файла: {e}")
    # Удаляем файл после отправки
    try:
        os.remove(file_path)
    except Exception as e:
        print(f"Ошибка при удалении файла: {e}")

def handle_export(chat_id, text):
    success, result = handle_export_clients_to_excel()
    if success:
        send_document(chat_id, result, caption="Список клиентов в Excel")
    else:
        send_message(chat_id, f"Ошибка экспорта: {result}")