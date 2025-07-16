import requests
import config
import time
import logging
import json
from TelegramApi.pagination import PAGINATED_TEXTS, PAGINATED_TIMESTAMPS, get_paginated_pages, build_reply_markup
from Handler.handler import handle_message
from TelegramApi.utils import send_message

def edit_message(chat_id, message_id, page=0, page_size=None):
    user_msgs = PAGINATED_TEXTS.get(chat_id, {})
    msg_data = user_msgs.get(message_id)
    if not msg_data or not msg_data.get("text"):
        url = f"https://api.telegram.org/bot{config.TELEGRAM_TOKEN}/editMessageText"
        params = {
            "chat_id": chat_id,
            "message_id": message_id,
            "text": "Данные устарели. Пожалуйста, запросите список заново."
        }
        try:
            requests.get(url, params=params, timeout=config.HTTP_REQUEST_TIMEOUT)
        except requests.exceptions.RequestException as e:
            logging.error(f"Ошибка при редактировании сообщения: {e}")
        return
    text = msg_data["text"]
    page_size = page_size if page_size else msg_data["page_size"]
    pages = get_paginated_pages(text, page_size)
    total_pages = len(pages)
    page = max(0, min(page, total_pages - 1))
    reply_markup = build_reply_markup(page, total_pages, page_size) if total_pages > 1 else None
    url = f"https://api.telegram.org/bot{config.TELEGRAM_TOKEN}/editMessageText"
    params = {
        "chat_id": chat_id,
        "message_id": message_id,
        "text": pages[page] if total_pages > 0 else ""
    }
    if reply_markup:
        params["reply_markup"] = json.dumps(reply_markup)
    try:
        requests.get(url, params=params, timeout=config.HTTP_REQUEST_TIMEOUT)
        PAGINATED_TEXTS[chat_id][message_id]["page_size"] = page_size
        PAGINATED_TIMESTAMPS[(chat_id, message_id)] = time.time()
    except requests.exceptions.RequestException as e:
        logging.error(f"Ошибка при редактировании сообщения: {e}")


def get_updates(offset=None):
    url = f"https://api.telegram.org/bot{config.TELEGRAM_TOKEN}/getUpdates"
    params = {"offset": offset, "timeout": config.TELEGRAM_API_TIMEOUT}
    try:
        response = requests.get(url, params=params, timeout=config.HTTP_REQUEST_TIMEOUT)
        response.raise_for_status()
        updates = response.json()["result"]
        for update in updates:
            if "callback_query" in update:
                chat_id = update["callback_query"]["message"]["chat"]["id"]
                message_id = update["callback_query"]["message"]["message_id"]
                data = update["callback_query"]["data"]
                if data.startswith("page_"):
                    parts = data.split("_")
                    page = int(parts[1])
                    page_size = int(parts[2])
                    edit_message(chat_id, message_id, page=page, page_size=page_size)
                elif data.startswith("setsize_"):
                    parts = data.split("_")
                    page_size = int(parts[1])
                    page = int(parts[2])
                    edit_message(chat_id, message_id, page=page, page_size=page_size)
                offset = update["update_id"] + 1
            elif "message" in update:
                chat_id = update["message"]["chat"]["id"]
                result = handle_message(update["message"])
                if isinstance(result, tuple) and result[0] == "document":
                        # ('document', file_path, caption)
                        from TelegramApi.utils import send_document
                        send_document(chat_id, result[1], caption=result[2])
                else:
                   send_message(chat_id, result if isinstance(result, str) else result[1])
                offset = update["update_id"] + 1
        return offset
    except requests.exceptions.Timeout:
        # logging.warning("Telegram API не ответил за отведенное время.")
        return offset  # Продолжаем с тем же offset
    except requests.exceptions.RequestException as e:
        logging.error(f"Ошибка при получении обновлений: {e}")
        return offset