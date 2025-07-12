import time
from TelegramApi.telegram_api import get_updates
from CommandsDB.db import create_tables

def run_bot():
    print("Бот запущен.")
    offset = None
    while True:
        offset = get_updates(offset)
        time.sleep(1)

if __name__ == "__main__":
    create_tables()
    run_bot()