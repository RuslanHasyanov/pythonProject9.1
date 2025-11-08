import pytest
import re


@pytest.mark.parametrize("invalid_input", [
        None,  # None
        "",  # Пустая строка
        "   ",  # Только пробелы
        "1234",  # Слишком короткая строка
        "123456789012345678901234",  # Слишком длинная строка
        "1234abc5678def9012",  # Буквы в номере
        "1234!@#$5678%^&*9012",  # Спецсимволы
        "1234 5678 9012 345",  # Неправильная длина для карты
        "1234567890123456789",  # Неправильная длина для счета

def test_invalid_input(self, invalid_input):
    """Тестирование обработки некорректных входных данных"""
    with pytest.raises((ValueError, TypeError)):
        mask_account_card(invalid_input)


def test_input_type_validation(self):
    """Тестирование проверки типа входных данных"""
    with pytest.raises(ValueError):
        mask_account_card(1234567890123456)  # Число вместо строки
    with pytest.raises(ValueError):
        mask_account_card(["1234567890123456"])  # Список вместо строки