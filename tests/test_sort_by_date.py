import pytest
from datetime import datetime
from your_module import sort_by_date


@pytest.fixture
def empty_data(self):
    """Возвращает пустой список"""
    return []

@pytest.fixture
    def data_with_invalid_dates(self):
        """Возвращает данные с некорректными датами"""
        return [
            {"id": 1, "date": "2019-08-26T10:50:58.294041", "amount": 100},
            {"id": 2, "date": "invalid_date", "amount": 200},
            {"id": 3, "date": "2018-07-11T02:26:18.671407", "amount": 300},
        ]


def test_empty_list(self, empty_data):
    """Тестирование сортировки пустого списка"""
    result = sort_by_date(empty_data)
    assert result == []

def test_invalid_date_format(self, data_with_invalid_dates):
    """Тестирование обработки некорректных форматов дат"""
    with pytest.raises((ValueError, TypeError)):
    sort_by_date(data_with_invalid_dates)