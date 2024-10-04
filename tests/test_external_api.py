from unittest.mock import patch

from src.external_api import convert_to_rub

# import pytest

# from src.utils import read_json_file


# @pytest.fixture
# def get_transaction_number():
#     return 441945886


# @pytest.fixture
# def transactions():
#     file_path = read_json_file('../data/operations.json')
#     return file_path


# def test_get_transaction_rub(transactions, get_transaction_number):
#     assert get_transaction_rub(transactions, get_transaction_number) == {
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


@patch("requests.get")
def test_convert_to_rub(mock_get):
    mock_get.return_value.json.return_value = {"result": 60}
    assert convert_to_rub({"amount": "20", "currency": "USD"}) == 60
    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=20",
        headers={"apiKey": "Sx2380Pr3GZUMjwawNsGujnF6CoAlBBw"},
    )
