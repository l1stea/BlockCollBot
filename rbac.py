# Пример структуры ролей и разрешённых команд
from Handler.handler_get import handle_get_position_by_chat_id


ROLE_COMMANDS = {
    "admin": ["all"],
    "seller": ["addsale", "addclient", "listclients", "searchclient"],
    "warehouse": ["addsupply", "listsupplies"],
    "hr": ["addemployee", "listemployees"],
    "assembler": ["addassembly", "listassemblies"],
    "guest": ["start", "chat_id"]
}

def get_user_role(chat_id):
    return handle_get_position_by_chat_id(chat_id)

def check_access(chat_id, command):
    """
    Проверяет, имеет ли пользователь с данным chat_id право выполнять команду.
    """
    role = get_user_role(chat_id)
    if not role:
        allowed_guest = ROLE_COMMANDS.get("guest", [])
        return command in allowed_guest
    allowed = ROLE_COMMANDS.get(role, [])
    return "all" in allowed or command in allowed