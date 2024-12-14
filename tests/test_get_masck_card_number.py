import pytest
from src.masks import get_masck_card_number

def test_get_masck_card_number():
    assert get_masck_card_number(1596837868705199) == "1596 83 ** **** 5199"

@pytest.mark.parametrize("card, result",
                         [(159683786870519, "Вы ввели недостаточно цифр"),
                          ("159683786870519p", "Вы ввели не число"),
                          ("", "Вы ввели не число")])
def test_get_masck_card_number_2(card, result):
    assert get_masck_card_number(card) == result