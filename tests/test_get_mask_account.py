import pytest

from src.masks import get_mask_account


def test_get_mask_account() -> None:
    assert get_mask_account(64686473678894779589) == "**9589"


@pytest.mark.parametrize(
    "card, result",
    [
        (3538303347444789556, "Вы ввели недостаточно цифр"),
        ("3538303347444789556u", "Введите номер лицевого счета"),
        ("", "Введите номер лицевого счета"),
    ],
)
def test_get_mask_account_2(card: str | int, result: str) -> None:
    assert get_mask_account(card) == result
