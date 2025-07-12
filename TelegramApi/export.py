from Handler.handler_export import handle_export_clients_to_excel
from telegram_api import send_document, send_message

def handle_export(chat_id, text):
    success, result = handle_export_clients_to_excel()
    if success:
        send_document(chat_id, result, caption="Список клиентов в Excel")
    else:
        send_message(chat_id, f"Ошибка экспорта: {result}")