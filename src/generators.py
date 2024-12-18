from typing import Any, Generator


def filter_by_currency(transactions: list[dict], currency: str = "USD") -> Any:
    """Генератор, который фильтрует транзакции по заданной валюте."""
    if len(transactions) > 0:
        filter_transactions: Any = filter(
            lambda transaction_list: transaction_list.get("operationAmount").get("currency").get("code") == currency,
            transactions,
        )
        return filter_transactions
    else:
        return "Список пустой"


def transaction_descriptions(transactions: list[dict]) -> Any:
    """Функция принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""
    if len(transactions) > 0:
        for transaction in transactions:
            yield transaction.get("description")
    else:
        return "Список пустой"


def card_number_generator(start: int, end: int) -> Generator:
    """Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX."""
    for number in range(start, end + 1):
        card_number = f"{number:016d}"
        formatted_number = f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
        yield formatted_number
