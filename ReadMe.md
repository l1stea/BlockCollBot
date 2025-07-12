# BlockCollBot

## Описание

**BlockCollBot** — это Telegram-бот для работы с базой данных сотрудников/клиентов, с поддержкой экспорта в Excel, постраничной навигации по длинным сообщениям и разграничением прав доступа.

## Возможности

- Постраничная навигация по длинным сообщениям с помощью кнопок `<`, `>`, выбор количества строк на странице.
- Экспорт данных в Excel по команде.
- Хранение и очистка состояния пагинации для каждого пользователя.
- Уведомления администратору о запуске и ошибках.
- Логирование всех событий и ошибок в файл `bot.log`.
- Гибкая настройка через файл `config.py`.

## Установка

1. Клонируйте репозиторий:
   ```sh
   git clone https://github.com/l1stea/BlockCollBot.git
   cd BlockCollBot
   ```

2. Установите зависимости:
   ```sh
   pip install -r requirements.txt
   ```

3. Настройте файл `config.py`:
   - Укажите параметры подключения к БД.
   - Вставьте токен Telegram-бота.
   - Установите нужные параметры логирования.

4. Проверьте структуру базы данных и создайте необходимые таблицы (см. `CommandsDB/db.py`).

## Запуск

```sh
python main.py
```

## Тесты

Тесты находятся в папке `tests`. Запуск тестов:
```sh
pytest tests/
```

## Логирование

Все логи сохраняются в файл `bot.log` в корне проекта (UTF-8).

## Структура проекта

```
Курсовая работа/
├── main.py
├── config.py
├── requirements.txt
├── bot.log
├── Logging/
│   └── bot_logging.py
├── CommandsDB/
│   ├── db.py
│   ├── get.py
│   └── ...
├── Handler/
│   ├── handler.py
│   └── handler_export.py
├── TelegramApi/
│   ├── telegram_api.py
│   ├── pagination.py
│   └── export.py
└── tests/
    └── test_get.py
```
---

**Для запуска бота требуется Python 3.8+ и доступ к MySQL.**


## Безопасность и переменные окружения

Для хранения секретных данных (токенов, паролей, логинов) используется файл `.env`, который не добавляется в репозиторий.

### Как настроить

1. **Создайте файл `.env` в корне проекта:**
    ```
    TELEGRAM_TOKEN=ваш_секретный_токен
    DB_USER=ваш_пользователь
    DB_PASSWORD=ваш_пароль
    DB_HOST=localhost
    DB_NAME=ваша_база
    ```

2. **Убедитесь, что в `.gitignore` есть строка:**
    ```
    .env
    ```

3. **Весь проект автоматически подхватит переменные из `.env` через библиотеку [python-dotenv](https://pypi.org/project/python-dotenv/).**

4. **Пример использования в `config.py`:**
    ```python
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
    ```

**Это защищает ваши пароли и токены от случайной публикации в открытом доступе!**

## Контакты

Автор: Тимошенко Е.М.  
GitHub: [l1stea](https://github.com/l1stea)
___