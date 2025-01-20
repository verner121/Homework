import pytest

from src.masks import get_masck_card_number, get_mask_account


def test_get_masck_card_number() -> None:
    assert get_masck_card_number(1596837868705199) == "1596 83 ** **** 5199"


@pytest.mark.parametrize(
    "card, result",
    [
        (159683786870519, "Вы ввели недостаточно цифр"),
        ("159683786870519p", "Вы ввели не число"),
        ("", "Вы ввели не число"),
    ],
)
def test_get_masck_card_number_2(card: str | int, result: str) -> None:
    assert get_masck_card_number(card) == result


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


if __name__ == "__main__":
    pytest.main()  # Запуск тестов
