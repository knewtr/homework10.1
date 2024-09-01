def get_mask_card_number(card_number: str) -> str:
    '''Функция принимает номер карты и возвращает ее маску'''
    if card_number.isdigit() and len(card_number) == 16:
        return f"{card_number[:4]} {card_number[4:6]}{'*' * 2} {"*" * 4} {card_number[12:]}"


def get_mask_account(account_number: str) -> str:
    '''Функция принимает номер аккаунта и возвращает его маску'''
    if account_number.isdigit() and len(account_number) == 20:
        return f"{"*" * 2}{account_number[16:]}"
