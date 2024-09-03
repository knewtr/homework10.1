from typing import Any

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_data: str | Any) -> str | Any:
    """Функция маскирует номер карты или номер аккаунта"""
    card_name: str = "".join(
        element if element.isalpha() or element == " " else "" for element in card_data
    )
    card_number: str = "".join(
        element if element.isdigit() else "" for element in card_data
    )
    if len(card_number) == 16:
        masked_card_number = get_mask_card_number(card_number)
        masked_data: str = card_name + masked_card_number
        return masked_data
    elif len(card_number) == 20:
        masked_account_number = get_mask_account(card_number)
        masked_data: str = card_name + masked_account_number
        return masked_data
    else:
        return None


def get_date(date: str | Any) -> str | Any:
    """Функция преобразует строку с датой в формат ДД.ММ.ГГГГ"""
    correct_date: str = ""
    if date != "":
        correct_date: str = "".join(f"{date[8:10]}.{date[5:7]}.{date[0:4]}")
    return correct_date