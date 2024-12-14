from typing import Any


def filter_by_state(user_dictionary, state = 'CANCELED'):
    """Функция для выведения данных по определенному значению"""
    new_dictionary_1 = []
    new_dictionary_2 = []
    for dictionary in user_dictionary:
      if "state" in dictionary:
        if dictionary["state"] == state:
          new_dictionary_1.append(dictionary)
          return new_dictionary_1
        elif dictionary["state"] == "CANCELED" :
            new_dictionary_2.append(dictionary)
            return new_dictionary_2
      else:
          return "Значения state нет в списке"

def sort_by_date(user_dictionary: list[dict[str, Any]], reverse: bool = True) -> list[dict[str, Any]]:
    """Функция, сортирующая список по дате"""
    new_date = sorted(user_dictionary, key=lambda dictionary: dictionary["date"], reverse=reverse)
    return new_date
