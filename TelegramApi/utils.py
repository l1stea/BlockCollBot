import os
import logging
import requests
import config
import time
import json
from TelegramApi.pagination import PAGINATED_TEXTS, PAGINATED_TIMESTAMPS, get_paginated_pages, build_reply_markup

def send_message(chat_id, text, page=0, page_size=10):
    pages = get_paginated_pages(text, page_size)
    total_pages = len(pages)
    page = max(0, min(page, total_pages - 1))
    reply_markup = build_reply_markup(page, total_pages, page_size) if total_pages > 1 else None
    url = f"https://api.telegram.org/bot{config.TELEGRAM_TOKEN}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": pages[page] if total_pages > 0 else ""
    }
    if reply_markup:
        params["reply_markup"] = json.dumps(reply_markup)
    try:
        response = requests.get(url, params=params, timeout=config.HTTP_REQUEST_TIMEOUT)
        response.raise_for_status()
        message_id = response.json().get("result", {}).get("message_id")
        if message_id:
            if chat_id not in PAGINATED_TEXTS:
                PAGINATED_TEXTS[chat_id] = {}
            PAGINATED_TEXTS[chat_id][message_id] = {"text": text, "page_size": page_size}
            PAGINATED_TIMESTAMPS[(chat_id, message_id)] = time.time()
        return message_id
    except requests.exceptions.RequestException as e:
        logging.error(f"Ошибка при отправке сообщения: {e}")
        return None

def send_document(chat_id, file_path, caption=None):
    url = f"https://api.telegram.org/bot{config.TELEGRAM_TOKEN}/sendDocument"
    with open(file_path, "rb") as f:
        files = {"document": f}
        data = {"chat_id": chat_id}
        if caption:
            data["caption"] = caption
        try:
            response = requests.post(url, data=data, files=files, timeout=config.HTTP_REQUEST_TIMEOUT)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            logging.error(f"Ошибка при отправке файла: {e}")
    try:
        os.remove(file_path)
    except Exception as e:
        logging.error(f"Ошибка при удалении файла: {e}")
