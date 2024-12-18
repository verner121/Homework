from typing import Any

import pytest

from src.generators import (card_number_generator, filter_by_currency,
                            transaction_descriptions)


def test_filter_by_currency(transactions: list[dict]) -> Any:
    """Тестирование функции filter_by_currency"""
    usd_transaction = list(filter_by_currency(transactions, "USD"))
    assert len(usd_transaction) == 3
    assert {t["id"] for t in usd_transaction} == {939719570, 142264268, 895315941}

    rub_transaction = list(filter_by_currency(transactions, "RUB"))
    assert len(rub_transaction) == 2
    assert {t["id"] for t in rub_transaction} == {873106923, 594226727}

    empty_transaction = list(filter_by_currency([], "USD"))
    if len(empty_transaction) == 0:
        assert "Список пустой"

    no_currency_transactions = list(filter_by_currency(transactions, "EUD"))
    assert len(no_currency_transactions) == 0


def test_transaction_descriptions(transactions: list[dict]) -> Any:
    """Тестирование функции transaction_descriptions"""
    descriptions = list(transaction_descriptions(transactions))
    assert len(descriptions) == 5

    expected_descriptions = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]
    assert descriptions == expected_descriptions


@pytest.mark.parametrize(
    "start, end, expected",
    [
        (
            1,
            5,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
            ],
        ),
        (5, 5, ["0000 0000 0000 0005"]),
        (99999999, 100000000, ["0000 0000 9999 9999", "0000 0001 0000 0000"]),
        (100, 102, ["0000 0000 0000 0100", "0000 0000 0000 0101", "0000 0000 0000 0102"]),
    ],
)
def test_card_number_generator(start: int, end: int, expected: str) -> Any:
    """Тестирование функции test_card_number_generator"""
    generator_numbers = list(card_number_generator(start, end))
    assert generator_numbers == expected
    assert list(card_number_generator(99999999, 100000000)) == ["0000 0000 9999 9999", "0000 0001 0000 0000"]
    assert list(card_number_generator(1, 0)) == []
