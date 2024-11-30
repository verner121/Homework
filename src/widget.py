from typing import Union

from src import masks


def mask_account_card(user_input: Union[str]) -> None | str:
    """Функция, принимающая номер или счет карты с названием банка"""
    split_input = user_input.split()
    if len(split_input) == 2:
        if split_input[0].lower() == "счет":
            new_input = "".join(split_input[-1])
            return masks.get_mask_account(new_input)
        else:
            new_input = "".join(split_input[-1])
            return masks.get_masck_card_number(new_input)
    else:
        return print("Вы ввели неккоректные данные")


def get_date(user_date: Union[str]) -> None | str:
    """Функция, принимающая дату"""
    new_date = user_date.split("T")
    date = new_date[0].split("-")
    return print(f"{date[-1]}.{date[-2]}.{date[-3]}")
