from typing import Any


def filter_by_state(user_dictionary: list[dict[str, Any]], state: str = "EXECUTED") -> list[dict[str, Any]]:
    """Функция для выведения данных по определенному значению"""
    new_dictionary = []
    for dictionary in user_dictionary:
        if dictionary["state"] == state:
            new_dictionary.append(dictionary)
    return new_dictionary


def sort_by_date(user_dictionary: list[dict[str, Any]], reverse: bool = True) -> list[dict[str, Any]]:
    """Функция, сортирующая список по дате"""
    new_date = sorted(user_dictionary, key=lambda dictionary: dictionary["date"], reverse=reverse)
    return new_date
