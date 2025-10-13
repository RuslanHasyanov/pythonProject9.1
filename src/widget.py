def mask_account_card(data: str) -> str:
    ''' Маскирует номер карты или счета в переданной строке '''

    # Разделяем строку на слова
    parts = data.split()

    if len(parts) < 2:
        return data

    # Последняя часть - предполагаемый номер
    number_part = parts[-1]

    # Проверяем, является ли последняя часть числом
    if not number_part.isdigit():
        return data

    # Тип карты/счета - все части кроме последней
    account_type = " ".join(parts[:-1])

    # Определяем тип по ключевым словам или длине номера
    if "счет" in account_type.lower() or len(number_part) > 16:
        # Маскировка счета: показываем только последние 4 цифры
        return f"{account_type} **{number_part[-4:]}"
    else:
        # Маскировка карты: показываем первые 6 и последние 4 цифры
        if len(number_part) == 16:
            masked_number = f"{number_part[:4]} {number_part[4:6]}** **** {number_part[-4:]}"
        return f"{account_type} {masked_number}"


def get_date(date_string: str) -> str:
    """
    Изменяет формат строки даты
    """
    try:
        # Разделяем дату и время
        date_part = date_string.split('T')[0]

        # Разделяем год, месяц, день
        year, month, day = date_part.split('-')

        # Форматируем в нужный вид
        return f"{day}.{month}.{year}"

    except (IndexError, ValueError):
        return date_string
