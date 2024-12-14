from typing import Union

from src import masks


def mask_account_card(user_input: Union[str]) -> str:
    """Функция.принимающая номер карты или счета, на выходе - маска"""
    if user_input != "":
      split_input = user_input.split()
      if len(split_input) == 2:
          if len(split_input[1]) == 20 or 16:
            if split_input[0].lower() == "счет":
                new_input = "".join(split_input[-1])
                return masks.get_mask_account(new_input)
            else:
                new_input = "".join(split_input[-1])
                return masks.get_masck_card_number(new_input)
          else:
              return "Вы ввели недостаточно цифр"
      else:
          return "Вы ввели неккоректные данные"
    else:
      return "Введите счет или номер карты"


def get_date(user_date: Union[str]) -> str:
    """Функция, принимающая дату"""
    new_date = user_date.split("T")
    date = new_date[0].split("-")
    return f"{date[-1]}.{date[-2]}.{date[-3]}"
