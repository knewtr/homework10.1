import pytest

from src.utils import read_json_file


@pytest.fixture
def list_check_fixture():
    transaction_list = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        },
        {
            "id": 587085106,
            "state": "EXECUTED",
            "date": "2018-03-23T10:45:06.972075",
            "operationAmount": {"amount": "48223.05", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
    ]
    return transaction_list


@pytest.fixture
def str_check_fixture():
    str_for_search = "вклад"
    return str_for_search


@pytest.fixture
def json_list():
    test_list = read_json_file("../data/operations.json")
    return test_list


@pytest.fixture
def category_list():
    list_1 = ["Открытие вклада", "Перевод с карты на карту", "Перевод со счета на счет"]
    return list_1


def test_search_func(list_check_fixture, str_check_fixture):
    assert {
        "id": 587085106,
        "state": "EXECUTED",
        "date": "2018-03-23T10:45:06.972075",
        "operationAmount": {"amount": "48223.05", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Открытие вклада",
        "to": "Счет 41421565395219882431",
    }


def test_transaction_category(json_list, category_list):
    assert {"Открытие вклада": 10, "Перевод со счета на счет": 15, "Перевод с карты на карту": 19}
