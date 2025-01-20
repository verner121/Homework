from typing import Union

CONST_CARD_NUMB = 16
CONST_ACCOUNT_NUMB = 20


def get_masck_card_number(new_input: Union[int, str]) -> str:
    """Функция, принимаюшая номер карты, на выходе - маска карты"""
    str_number = str(new_input)
    if str_number.isdigit():
        if len(str_number) == CONST_CARD_NUMB:
            return f"{str_number[:4]} {str_number[4:6]} ** **** {str_number[12:]}"
        else:
            return "Вы ввели недостаточно цифр"
    else:
        return "Вы ввели не число"


def get_mask_account(new_input: Union[int, str]) -> str:
    """Функция принимающая счет карты и на выходе - маску счета"""
    str_account = str(new_input)
    if str_account.isdigit():
        if len(str_account) == CONST_ACCOUNT_NUMB:
            return f"**{str_account[-4:]}"
        else:
            return "Вы ввели недостаточно цифр"
    else:
        return "Введите номер лицевого счета"
