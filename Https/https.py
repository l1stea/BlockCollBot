# import os
# import requests
# import config
# import time
# import threading
# from Handler.handler import handle_message
# from Handler.handler_export import handle_export_clients_to_excel

# timeout = 60

# # Структура: {chat_id: {message_id: {"text": ..., "page_size": ...}}}
# PAGINATED_TEXTS = {}
# PAGINATED_TIMESTAMPS = {}
# MAX_LIFETIME = 3600  # 1 час

# def cleanup_paginated_texts():
#     while True:
#         now = time.time()
#         for chat_id in list(PAGINATED_TEXTS.keys()):
#             for message_id in list(PAGINATED_TEXTS[chat_id].keys()):
#                 last_access = PAGINATED_TIMESTAMPS.get((chat_id, message_id), now)
#                 if now - last_access > MAX_LIFETIME:
#                     del PAGINATED_TEXTS[chat_id][message_id]
#                     PAGINATED_TIMESTAMPS.pop((chat_id, message_id), None)
#             if not PAGINATED_TEXTS[chat_id]:
#                 del PAGINATED_TEXTS[chat_id]
#         time.sleep(600)  # Проверять каждые 10 минут

# threading.Thread(target=cleanup_paginated_texts, daemon=True).start()

# def get_paginated_pages(text, page_size):
#     lines = text.split('\n')
#     return ['\n'.join(lines[i:i+page_size]) for i in range(0, len(lines), page_size)]

# def build_reply_markup(page, total_pages, page_size):
#     buttons = []
#     if page > 0:
#         buttons.append({"text": "<", "callback_data": f"page_{page-1}_{page_size}"})
#     if page < total_pages - 1:
#         buttons.append({"text": ">", "callback_data": f"page_{page+1}_{page_size}"})
#     buttons_size = [
#         {"text": "10", "callback_data": f"setsize_10_{page}"},
#         {"text": "25", "callback_data": f"setsize_25_{page}"},
#         {"text": "50", "callback_data": f"setsize_50_{page}"}
#     ]
#     return {"inline_keyboard": [buttons, buttons_size]}

# def send_message(chat_id, text, page=0, page_size=10):
#     pages = get_paginated_pages(text, page_size)
#     total_pages = len(pages)
#     page = max(0, min(page, total_pages - 1))
#     reply_markup = build_reply_markup(page, total_pages, page_size) if total_pages > 1 else None
#     url = f"https://api.telegram.org/bot{config.TELEGRAM_TOKEN}/sendMessage"
#     params = {
#         "chat_id": chat_id,
#         "text": pages[page] if total_pages > 0 else ""
#     }
#     if reply_markup:
#         import json
#         params["reply_markup"] = json.dumps(reply_markup)
#     try:
#         response = requests.get(url, params=params, timeout=timeout)
#         response.raise_for_status()
#         message_id = response.json().get("result", {}).get("message_id")
#         if message_id:
#             if chat_id not in PAGINATED_TEXTS:
#                 PAGINATED_TEXTS[chat_id] = {}
#             PAGINATED_TEXTS[chat_id][message_id] = {"text": text, "page_size": page_size}
#             PAGINATED_TIMESTAMPS[(chat_id, message_id)] = time.time()
#         return message_id
#     except requests.exceptions.RequestException as e:
#         print(f"Ошибка при отправке сообщения: {e}")
#         return None

# def edit_message(chat_id, message_id, page=0, page_size=None):
#     user_msgs = PAGINATED_TEXTS.get(chat_id, {})
#     msg_data = user_msgs.get(message_id)
#     # Проверка: если данных нет, выводим сообщение об истечении срока
#     if not msg_data or not msg_data.get("text"):
#         url = f"https://api.telegram.org/bot{config.TELEGRAM_TOKEN}/editMessageText"
#         params = {
#             "chat_id": chat_id,
#             "message_id": message_id,
#             "text": "Данные устарели. Пожалуйста, запросите список заново."
#         }
#         try:
#             requests.get(url, params=params, timeout=timeout)
#         except requests.exceptions.RequestException as e:
#             print(f"Ошибка при редактировании сообщения: {e}")
#         return
#     text = msg_data["text"]
#     page_size = page_size if page_size else msg_data["page_size"]
#     pages = get_paginated_pages(text, page_size)
#     total_pages = len(pages)
#     page = max(0, min(page, total_pages - 1))
#     reply_markup = build_reply_markup(page, total_pages, page_size) if total_pages > 1 else None
#     url = f"https://api.telegram.org/bot{config.TELEGRAM_TOKEN}/editMessageText"
#     params = {
#         "chat_id": chat_id,
#         "message_id": message_id,
#         "text": pages[page] if total_pages > 0 else ""
#     }
#     if reply_markup:
#         import json
#         params["reply_markup"] = json.dumps(reply_markup)
#     try:
#         requests.get(url, params=params, timeout=timeout)
#         PAGINATED_TEXTS[chat_id][message_id]["page_size"] = page_size
#         PAGINATED_TIMESTAMPS[(chat_id, message_id)] = time.time()
#     except requests.exceptions.RequestException as e:
#         print(f"Ошибка при редактировании сообщения: {e}")

# def get_updates(offset=None):
#     url = f"https://api.telegram.org/bot{config.TELEGRAM_TOKEN}/getUpdates"
#     params = {"offset": offset, "timeout": 60}
#     try:
#         response = requests.get(url, params=params, timeout=timeout)
#         response.raise_for_status()
#         updates = response.json()["result"]
#         for update in updates:
#             if "callback_query" in update:
#                 chat_id = update["callback_query"]["message"]["chat"]["id"]
#                 message_id = update["callback_query"]["message"]["message_id"]
#                 data = update["callback_query"]["data"]
#                 if data.startswith("page_"):
#                     parts = data.split("_")
#                     page = int(parts[1])
#                     page_size = int(parts[2])
#                     edit_message(chat_id, message_id, page=page, page_size=page_size)
#                 elif data.startswith("setsize_"):
#                     parts = data.split("_")
#                     page_size = int(parts[1])
#                     page = int(parts[2])
#                     edit_message(chat_id, message_id, page=page, page_size=page_size)
#                 offset = update["update_id"] + 1
#             elif "message" in update:
#                 chat_id = update["message"]["chat"]["id"]
#                 text = update["message"].get("text", "")
#                 if "/export" in text or "export" in text:
#                     handle_export(chat_id, text)
#                 else:
#                     response_text = handle_message(update["message"])
#                     send_message(chat_id, response_text)
#                 offset = update["update_id"] + 1
#         return offset
#     except requests.exceptions.RequestException as e:
#         print(f"Ошибка при получении обновлений: {e}")
#         return offset

# def send_document(chat_id, file_path, caption=None):
#     url = f"https://api.telegram.org/bot{config.TELEGRAM_TOKEN}/sendDocument"
#     with open(file_path, "rb") as f:
#         files = {"document": f}
#         data = {"chat_id": chat_id}
#         if caption:
#             data["caption"] = caption
#         try:
#             response = requests.post(url, data=data, files=files, timeout=timeout)
#             response.raise_for_status()
#         except requests.exceptions.RequestException as e:
#             print(f"Ошибка при отправке файла: {e}")
#     try:
#         os.remove(file_path)
#     except Exception as e:
#         print(f"Ошибка при удалении файла: {e}")

# def handle_export(chat_id, text):
#     success, result = handle_export_clients_to_excel()
#     if success:
#         send_document(chat_id, result, caption="Список клиентов в Excel")
#     else:
#         send_message(chat_id, f"Ошибка экспорта: {result}")