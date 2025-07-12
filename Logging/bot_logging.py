import logging
import config

logging.basicConfig(
    level=getattr(logging, config.LOG_LEVEL),
    format="%(asctime)s [%(levelname)s] %(message)s",
    filename="bot.log",
    filemode="a",
    encoding="utf-8"
)