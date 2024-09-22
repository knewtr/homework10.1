import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(filename)s %(levelname)s: %(message)s",
    filename="../logs/masks.log",
    filemode="w",
)

logger = logging.getLogger()


def get_mask_card_number(card_number: str) -> str | None:
    """Функция принимает номер карты и возвращает ее маску"""
    masked_card_number: str = ""
    logger.info("Checking card number")
    if card_number.isdigit() and len(card_number) == 16:
        masked_card_number = f'{card_number[:4]} {card_number[4:6]}{'*' * 2} {"*" * 4} {card_number[12:]}'
    logger.info(f'Masked card number:{card_number[:4]} {card_number[4:6]}{'*' * 2} {"*" * 4} {card_number[12:]}')
    return masked_card_number


def get_mask_account(account_number: str) -> str | None:
    """Функция принимает номер аккаунта и возвращает его маску"""
    masked_account_number: str = ""
    logger.info("Checking account number")
    if account_number.isdigit() and len(account_number) == 20:
        masked_account_number = f'{"*" * 2}{account_number[16:]}'
    logger.info(f'Masked account number:{"*" * 2}{account_number[16:]}')
    return masked_account_number
