import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    ("received_data", "expected"),
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ('', None),
        ("Maestro 64686473678894", None),
        ("Счет 6468647367889477958910", None),
    ],
)
def test_mask_account_card(received_data, expected):
    assert mask_account_card(received_data) == expected


@pytest.mark.parametrize(
    ("date", "correct_date"), [("2024-03-11T02:26:18.671407", "11.03.2024"), ("", '')]
)
def test_get_date(date, correct_date):
    assert get_date(date) == correct_date
