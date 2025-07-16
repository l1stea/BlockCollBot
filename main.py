import config
import time
from TelegramApi.telegram_api import get_updates
from TelegramApi.utils import notify_admin
from CommandsDB.db import create_tables
from Logging.bot_logging import *


def run_bot():
    """
    Основной цикл работы Telegram-бота.
    Логирует запуск, уведомляет администратора, обрабатывает обновления Telegram.
    При ошибках логирует их и продолжает работу.
    """
    logging.info("Бот запущен.")
    notify_admin("Бот запущен и готов к работе.")
    offset = None
    while True:
        try:
            offset = get_updates(offset)
        except Exception as e:
            logging.error(f"Ошибка в get_updates: {e}")
        time.sleep(config.POLL_INTERVAL)

if __name__ == "__main__":
    create_tables()
    while True:
        try:
            run_bot()
        except KeyboardInterrupt:
            logging.info("Бот остановлен пользователем.")
            break
        except Exception as e:
            logging.error(f"Критическая ошибка: {e}. Перезапуск через 5 секунд.")
            notify_admin(f"Бот упал с ошибкой: {e}. Перезапуск через 5 секунд.")
            time.sleep(5)