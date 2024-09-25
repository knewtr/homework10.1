import pytest

from src.utils import read_json_file

# @pytest.fixture
# def get_path():
#     path_to_file = '../data/operations.json'
#     return path_to_file


# def test_read_json_file(get_path):
#     assert read_json_file(get_path)[0] == {
#     "id": 441945886,
#     "state": "EXECUTED",
#     "date": "2019-08-26T10:50:58.294041",
#     "operationAmount": {
#       "amount": "31957.58",
#       "currency": {
#         "name": "руб.",
#         "code": "RUB"
#       }
#     },
#     "description": "Перевод организации",
#     "from": "Maestro 1596837868705199",
#     "to": "Счет 64686473678894779589"
#   }


@pytest.fixture
def wrong_path():
    return []


def test_wrong_path(wrong_path):
    assert read_json_file("wrong_path") == []
