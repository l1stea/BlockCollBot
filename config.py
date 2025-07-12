# config.py
from dotenv import load_dotenv
import os

load_dotenv()

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME")
}
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

POLL_INTERVAL = 1
LOG_LEVEL = "INFO"

TELEGRAM_API_TIMEOUT = 60  # seconds for long polling
HTTP_REQUEST_TIMEOUT = 10  # seconds for HTTP requests