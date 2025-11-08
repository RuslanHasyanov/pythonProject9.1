import pytest
from datetime import datetime
from tests import get_date


@pytest.mark.parametrize("invalid_input", [
    None,  # None
    "",  # Пустая строка
    "   ",  # Пробелы


def test_empty_string(self):
    """Тестирование обработки пустой строки"""
    with pytest.raises(ValueError):
        get_date("")

def test_whitespace_string(self):
    """Тестирование обработки строки с пробелами"""
    with pytest.raises(ValueError):
        get_date("   ")