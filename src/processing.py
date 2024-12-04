from typing import Any


def filter_by_state(user_dictionary: list[dict[str, Any]], state: str = "EXECUTED") -> Any:
    """Функция для выведения данных по определенному значению"""
    new_dictionary = []
    for i in user_dictionary:
        if i["state"] == state:
            new_dictionary.append(i)
    return print(new_dictionary)


def sort_by_date(user_dictionary: list[dict[str, Any]], reverse: bool = True) -> Any:
    """Функция, сортирующая список словаlist[dict[str, Any]]рей по дате"""
    new_date = sorted(user_dictionary, key=lambda i: i["date"], reverse=reverse)
    return print(new_date)
