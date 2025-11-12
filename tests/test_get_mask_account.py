import pytest, test_cases
from test_get_mask_account import get_mask_account  # Замените your_module на имя вашего модуля


@pytest.mark.parametrize(
    "invalid_input",
    [
        "",  # Пустая строка
        "   ",
    ],
)  # Только пробелы
def test_whitespace_string(self):
    """Тестирование обработки строки с пробелами"""
    with pytest.raises(ValueError):
        get_mask_account("   ")


def test_empty_string(self):
    """Тестирование обработки пустой строки"""
    with pytest.raises(ValueError):
        get_mask_account("")

    for account_number, expected in test_cases:
        assert get_mask_account(account_number) == expected
