import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "number, expected",
    [
        ("7365410843013587", "7365 41** **** 3587"),
        ("73654108430135", ''),
        ("aa65410843013587", ''),
        ("736541084301358712", ''),
        ('', ''),
    ],
)
def test_get_mask_card_number(number, expected):
    assert get_mask_card_number(number) == expected


@pytest.mark.parametrize(
    "account, expected_account",
    [
        ("73654108430135874305", "**4305"),
        ("736541084301358743", ''),
        ("aaaa4108430135874305", ''),
        ("7365410843013587430512", ''),
        ('', ''),
    ],
)
def test_get_mask_account(account, expected_account):
    assert get_mask_account(account) == expected_account
