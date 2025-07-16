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
            return ("text", "Пожалуйста, используйте команды, начинающиеся с '/'. Например: /help")

        # Команда chat_id
        if text_raw.strip().lower() == "/chat_id":
            return ("text", f"Ваш chat_id: {chat_id}")

        # Определяем команду (например, /add_client -> add_client)
        command = text_raw.split()[0].lstrip("/")

        # Проверяем доступ
        if not check_access(chat_id, command):
            return ("text", "У вас нет прав для выполнения этой команды.")
        
        # Приводим текст к нижнему регистру для унификации
        text = text_raw.lower()

        if text.endswith(" -h") or text.endswith(" --help"):
            cmd = text.split()[0]
            desc = command_descriptions.get(cmd)
            if desc:
                return ("text", f"Описание команды {cmd}:\n{desc}")

        # Словарь команд
        for cmd, handler in command_handlers.items():
            if text.startswith(cmd):
                return handler(text_raw)
        return ("text", "Я не понимаю эту команду.")

    except:
        return ("text", "Я не понимаю.")