from Handler.handler_add import *
from Handler.handler_link import *
from Handler.handler_delete import *
from Handler.handler_search import *
from Handler.handler_update import *
from Handler.handler_list import *
from Handler.handler_export import *
from Handler.handler_guest import *
from Handler.commands import *
from rbac import check_access

# Функции для обработки сообщений от бота
def handle_message(message):
    try:
        chat_id = message["chat"]["id"]
        text_raw = message["text"]

        # Проверка: если текст не начинается с '/', это не команда
        if not text_raw.startswith("/"):
            return "Пожалуйста, используйте команды, начинающиеся с '/'. Например: /help"
        
        # Команда chat_id
        if text_raw.strip().lower() == "/chat_id":
            return f"Ваш chat_id: {chat_id}"

        # Определяем команду (например, /add_client -> add_client)
        command = text_raw.split()[0].lstrip("/")

        # Проверяем доступ
        if not check_access(chat_id, command):
            return "У вас нет прав для выполнения этой команды."

        text = text_raw.lower()

        # Словарь команд
        for cmd, handler in command_handlers.items():
            if text.startswith(cmd):
                return handler(text_raw)
        return "Я не понимаю эту команду."

    except:
        return "Я не понимаю."