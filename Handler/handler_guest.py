from Handler.commands import *

@command("/start", description="Начать работу с ботом.")
def handle_start(text):
    return "Привет! Я ваш новый бот. Используйте команды для редактирования данных. (/help - помощь)"


@command("/help", description="Показать список всех команд и их описания.")
def handle_help(text):
    help_lines = ["Список доступных команд:\n"]
    for cmd, desc in command_descriptions.items():
        help_lines.append(f"{cmd} — {desc}\n")
    return "\n".join(help_lines)