# Пример структуры ролей и разрешённых команд
ROLE_COMMANDS = {
    "admin": ["all"],
    "seller": ["addsale", "addclient", "listclients", "searchclient"],
    "warehouse": ["addsupply", "listsupplies"],
    "hr": ["addemployee", "listemployees"],
    "assembler": ["addassembly", "listassemblies"]
}

def get_user_role(chat_id):
    """
    Получить роль пользователя по chat_id.
    Здесь пример с заглушкой — в реальном проекте брать из БД.
    """
    # Пример: словарь пользователей для теста
    users = {
        # 222222222: "admin",
        382814603: "seller",
        # 222222222: "warehouse",
        # 333333333: "hr",
        # 444444444: "assembler"
    }
    return users.get(chat_id, None)

def check_access(chat_id, command):
    """
    Проверяет, имеет ли пользователь с данным chat_id право выполнять команду.
    """
    role = get_user_role(chat_id)
    if not role:
        return False
    allowed = ROLE_COMMANDS.get(role, [])
    return "all" in allowed or command in allowed