import time
from CommandsDB.db import *
from Https.https import get_updates

def run_bot():
    print("Бот запущен.")
    offset = None
    while True:
        offset = get_updates(offset)
        time.sleep(1)

if __name__ == "__main__":
    create_tables()
    run_bot()