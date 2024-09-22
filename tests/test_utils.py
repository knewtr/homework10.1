import pytest

from src.utils import read_json_file

# @pytest.fixture
# def test_path():
#     return '../data/operations.json'


# def test_read_json_file(test_path):
#     assert read_json_file(test_path)[1] == {
#     "id": 41428829,
#     "state": "EXECUTED",
#     "date": "2019-07-03T18:35:29.512364",
#     "operationAmount": {
#       "amount": "8221.37",
#       "currency": {
#         "name": "USD",
#         "code": "USD"
#       }
#     },
#     "description": "Перевод организации",
#     "from": "MasterCard 7158300734726758",
#     "to": "Счет 35383033474447895560"
#   }


@pytest.fixture
def wrong_path():
    return []


def test_wrong_path(wrong_path):
    assert read_json_file("wrong_path") == []
