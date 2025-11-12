import pytest
from processing import filter_by_state

@pytest.mark.parametrize("state", [
        "EXECUTED",
        "PENDING",
        "CANCELED",
        "",
        "UNKNOWN_STATE"

@pytest.mark.parametrize("state, expected_count, expected_ids"), [
        ("EXECUTED", 3, [1, 3, 5]),
        ("PENDING", 2, [2, 6]),
        ("CANCELED", 1, [4]),
        ("COMPLETED", 0, []),  # Несуществующий статус
        ("executed", 0, []),] # Регистрозависимый поиск


def test_empty_list_input(self, empty_data):
    """Тестирование с пустым списком на входе"""
    result = filter_by_state(empty_data, "EXECUTED")

    assert result == []
    assert len(result) == 0


def test_empty_data_with_different_states(self, empty_data, state):
    """Тестирование пустого списка с различными статусами"""
    result = filter_by_state(empty_data, state)
    assert result == []