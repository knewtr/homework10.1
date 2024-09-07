import pytest

from src.generators import card_number_generator


@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (0, 1, "0000 0000 0000 0000"),
        (9999999999999999, 9999999999999999, "9999 9999 9999 9999"),
        (1000, 1001, "0000 0000 0000 1000"),
    ],
)
def test_card_number_generator(start: int, stop: int, expected: str) -> None:
    generated_number = card_number_generator(start, stop)
    assert next(generated_number) == expected
