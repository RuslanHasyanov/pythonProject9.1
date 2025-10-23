def filter_by_state(transactions, state="EXECUTED"):
    """
    Фильтрует список словарей по значению ключа 'state', возвращает
    новый список словарей, отфильтрованных по state
    """
    return [transaction for transaction in transactions if transaction.get("state") == state]


def sort_by_date(transactions, reverse=True):
    """
    Сортирует список словарей по дате с безопасной обработкой отсутствующих значений,
    возвращает новый отсортированный список словарей
    """
    return sorted(
        transactions, key=lambda x: x.get("date") or "", reverse=reverse  # Используем пустую строку если даты нет
    )
