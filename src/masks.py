def get_mask_card_number(card_number: int) -> str:
    """
    Формирует маску для номера карты.
    Формат: XXXX XX** **** XXXX
    """
    card_number_str = str(card_number)
    if len(card_number_str) == 16:
        mask_card_number = f"{card_number_str[0:4]} {card_number_str[4:6]}** **** {card_number_str[-4:]}"
        return mask_card_number

    return "Неверно введен номер карты"


def get_mask_account(account_number: int) -> str:
    """
    Формирует маску для номера счёта.
    Формат: **XX (где XX - последние 2 цифры)
    """
    account_number_str = str(account_number)

    if len(account_number_str) == 20:
        mask_account_number = f"**{account_number_str[-4:]}"
        return mask_account_number

    return "Неверно введен номер счета"
