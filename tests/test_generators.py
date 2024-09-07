import pytest

from src.generators import filter_by_currency

@pytest.mark.parametrize("transaction_list, default_currency, expected", [
    (
            [], "EUR", "Список пустой!"),
    (
            [], "RUB", "Список пустой!")]
                         )
def test_filter_by_currency_exceptions(transaction_list, default_currency, expected):
    result = filter_by_currency(transaction_list, default_currency)
    assert result == expected
