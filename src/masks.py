import logging
import os
from typing import Union

CONST_CARD_NUMB = 16
CONST_ACCOUNT_NUMB = 20

# Создание папки logs, если она не существует
if not os.path.exists('logs'):
    os.makedirs('logs')

# Настройка логирования для модуля masks
logger = logging.getLogger('masks')
logger.setLevel(logging.DEBUG)

# Создание обработчика для записи логов в файл
file_handler = logging.FileHandler('logs/masks.log', mode='w', encoding='utf-8')
file_handler.setLevel(logging.DEBUG)

# Форматирование логов
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)

# Добавление обработчика к логгеру
logger.addHandler(file_handler)


def get_masck_card_number(new_input: Union[int, str]) -> str:
    """Функция, принимаюшая номер карты, на выходе - маска карты"""

    logger.debug(f"Получение маски для номера карты: {new_input}")
    str_number = str(new_input)
    if str_number.isdigit():
        if len(str_number) == CONST_CARD_NUMB:
            logger.info(f"Маска карты успешно создана: {str_number}")
            return f"{str_number[:4]} {str_number[4:6]} ** **** {str_number[12:]}"
        else:
            logger.error("Ошибка: Номер карты должен содержать 16 цифр.")
            return "Вы ввели недостаточно цифр"
    else:
        logger.error("Ошибка: Номер карты должен содержать 16 цифр.")
        return "Вы ввели не число"


def get_mask_account(new_input: Union[int, str]) -> str:
    """Функция принимающая счет карты и на выходе - маску счета"""
    logger.debug(f"Получение маски для номера счета: {new_input}")
    str_account = str(new_input)
    if str_account.isdigit():
        if len(str_account) == CONST_ACCOUNT_NUMB:
            logger.info(f"Маска счета успешно создана: {str_account}")
            return f"**{str_account[-4:]}"
        else:
            logger.error("Ошибка: Номер счета должен содержать 20 цифр.")
            return "Вы ввели недостаточно цифр"
    else:
        logger.error("Ошибка: Номер счета должен содержать 20 цифр.")
        return "Введите номер лицевого счета"
