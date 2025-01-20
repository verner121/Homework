import pytest
import unittest
from src.widget import get_date, mask_account_card


def test_get_date() -> None:
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"


@pytest.mark.parametrize(
    "date, result", [("2024-03-1102:26:18.671407", "Введите корректные данные"), ("", "Введите корректные данные")]
)
def test_get_date_2(date: str, result: str) -> None:
    assert get_date(date) == result


@pytest.mark.parametrize(
    "acc, result",
    [
        ("Maestro 1596837868705199", "1596 83 ** **** 5199"),
        ("Счет 64686473678894779589", "**9589"),
        ("MasterCard 7158300734726758", "7158 30 ** **** 6758"),
        ("Счет 35383033474447895560", "**5560"),
    ],
)
def test_mask_account_card(acc: str, result: str) -> None:
    assert mask_account_card(acc) == result


@pytest.mark.parametrize(
    "acc_2, result_2",
    [
        ("1596837868705199", "Вы ввели неккоректные данные"),
        ("64686473678894779589", "Вы ввели неккоректные данные"),
        ("mastercard 7158300734726758", "7158 30 ** **** 6758"),
        ("счет 35383033474447895560", "**5560"),
        ("", "Введите счет или номер карты"),
        ("счет 3538303347444789556", "Вы ввели недостаточно цифр"),
        ("mastercard 715830073472675", "Вы ввели недостаточно цифр"),
    ],
)
def test_mask_account_card_2(acc_2: str, result_2: str) -> None:
    assert mask_account_card(acc_2) == result_2


if __name__ == "__main__":
    unittest.main()  # Запуск тестов
