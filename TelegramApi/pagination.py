import time
import threading

PAGINATED_TEXTS = {}
PAGINATED_TIMESTAMPS = {}
MAX_LIFETIME = 3600  # 1 час

def get_paginated_pages(text, page_size):
    lines = text.split('\n')
    return ['\n'.join(lines[i:i+page_size]) for i in range(0, len(lines), page_size)]

def build_reply_markup(page, total_pages, page_size):
    buttons = []
    if page > 0:
        buttons.append({"text": "<", "callback_data": f"page_{page-1}_{page_size}"})
    if page < total_pages - 1:
        buttons.append({"text": ">", "callback_data": f"page_{page+1}_{page_size}"})
    buttons_size = [
        {"text": "10", "callback_data": f"setsize_10_{page}"},
        {"text": "25", "callback_data": f"setsize_25_{page}"},
        {"text": "50", "callback_data": f"setsize_50_{page}"}
    ]
    return {"inline_keyboard": [buttons, buttons_size]}

def cleanup_paginated_texts():
    while True:
        now = time.time()
        for chat_id in list(PAGINATED_TEXTS.keys()):
            for message_id in list(PAGINATED_TEXTS[chat_id].keys()):
                last_access = PAGINATED_TIMESTAMPS.get((chat_id, message_id), now)
                if now - last_access > MAX_LIFETIME:
                    del PAGINATED_TEXTS[chat_id][message_id]
                    PAGINATED_TIMESTAMPS.pop((chat_id, message_id), None)
            if not PAGINATED_TEXTS[chat_id]:
                del PAGINATED_TEXTS[chat_id]
        time.sleep(600)

threading.Thread(target=cleanup_paginated_texts, daemon=True).start()