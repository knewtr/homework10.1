from typing import Iterator, List, Any

transaction_list = (
    [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]
)

def filter_by_currency(transactions_list: List[dict], default_currency: str) -> Iterator[dict]:
    ''' Функция возвращает список транзакций в соответствии с заданной валютой'''
    for transaction in transactions_list:
        if transaction['operationAmount']['currency']['code'] == default_currency:
            yield transaction
        elif len(transactions_list) <= 0:
            raise ValueError('Пустой список транзакций')


def transaction_descriptions(transactions_list: list[dict[str, str]]) -> str:
    ''' Функция по очереди возвращает описание каждой транзакции'''
    if transactions_list:
        for data in transactions_list:
            transaction_info: str = data.get('description')
            yield transaction_info
    else:
        return 'Пустой список транзакций'


def card_number_generator(start, stop):
    '''Генерирует номер карты в заданном диапазоне'''
    while start <= stop:
        str_number = str(start)
        while len(str_number) < 16:
            str_number = '0' + str_number
        formatted_card_number = str_number[0:4] + ' ' + str_number[4:8] + ' ' + str_number[8:12] + ' ' + str_number[12:]
        yield formatted_card_number
        start += 1