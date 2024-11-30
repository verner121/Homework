from typing import Union

CONST_CARD_NUMB = 16
CONST_ACCOUNT_NUMB = 20


def get_masck_card_number(card_number: Union[int, str]) -> None | str:
    """Функция, принимаюшая номер карты, на выходе - маска карты"""
    str_number = str(card_number)
    if str_number.isdigit():
        if len(str_number) == CONST_CARD_NUMB:
            return f"{str_number[:4]} {str_number[4:6]} ** **** {str_number[12:]}"
        else:
            print("Вы ввели недостаточно цифр")
    else:
         print("Вы ввели не число")


def get_mask_account(card_account: Union[int, str]) -> None | str:
    """Функция принимающая счет карты и на выходе - маску счета"""
    str_account = str(card_account)
    if str_account.isdigit():
        if len(str_account) == CONST_ACCOUNT_NUMB:
            return f"**{str_account[-4:]}"
        else:
            print("Вы ввели недостаточно цифр")
    else:
        print("Введите номер лицевого счета")
