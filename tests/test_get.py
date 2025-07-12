import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from CommandsDB.get import get_position_by_chat_id, get_admin_chat_id_from_db

def test_get_position_by_chat_id():
    # Замените на существующий chat_id в вашей тестовой базе
    test_chat_id = 123456789
    position = get_position_by_chat_id(test_chat_id)
    assert position in ("admin", "user", None)  # допустимые значения

def test_get_admin_chat_id_from_db():
    admin_chat_id = get_admin_chat_id_from_db()
    assert isinstance(admin_chat_id, int) or admin_chat_id is None