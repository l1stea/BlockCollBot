from CommandsDB.get import *

# Обработчики команд для вывода списка
def handle_get_position_by_chat_id(text):
    try:
        position = get_position_by_chat_id(text)
        if not position:
            return None
        return position
    except Exception as e:
        return None
    