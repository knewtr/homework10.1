from unittest.mock import patch

import pandas as pd
import pytest

from src.file_reader import get_transaction_csv, get_transaction_xlsx


@pytest.fixture
def test_df() -> pd.DataFrame:
    test_dict = {
        "id": [650703.0, 3598919.0],
        "state": ["EXECUTED", "EXECUTED"],
        "date": ["2023-09-05T11:30:32Z", "2020-12-06T23:00:58Z"],
        "amount": [16210.0, 29740.0],
        "currency_name": ["Sol", "Peso"],
        "currency_code": ["PEN", "COP"],
        "from": ["Счет 58803664561298323391", "Discover 3172601889670065"],
        "to": ["Счет 39745660563456619397", "Discover 0720428384694643"],
        "description": ["Перевод организации", "Перевод с карты на карту"],
    }
    return pd.DataFrame(test_dict)


@patch("src.file_reader.pd.read_csv")
def test_get_transaction_csv(mock_csv, test_df):
    mock_csv.return_value = test_df
    result = get_transaction_csv("C:/Users/Knewt/myProjects/homework10.1/data/transactions.csv")
    expected = test_df.to_dict(orient="records")
    assert result == expected


@patch("src.file_reader.pd.read_excel")
def test_get_transaction_xlsx(mock_xlsx, test_df):
    mock_xlsx.return_value = test_df
    result = get_transaction_xlsx("C:/Users/Knewt/myProjects/homework10.1/data/transactions_excel.xlsx")
    expected = test_df.to_dict(orient="records")
    assert result == expected


def test_get_incorrect_path():
    assert get_transaction_csv("") == []
