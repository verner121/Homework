import  pytest
from src.widget import mask_account_card

@pytest.mark.parametrize("acc, result", [
    ("Maestro 1596837868705199", "1596 83 ** **** 5199"),
    ("Счет 64686473678894779589", "**9589"),
    ("MasterCard 7158300734726758", "7158 30 ** **** 6758"),
    ("Счет 35383033474447895560", "**5560")])
def test_mask_account_card(acc, result):
    assert mask_account_card(acc) == result

@pytest.mark.parametrize("acc_2, result_2", [
    ("1596837868705199", "Вы ввели неккоректные данные"),
    ("64686473678894779589", "Вы ввели неккоректные данные"),
    ("mastercard 7158300734726758", "7158 30 ** **** 6758"),
    ("счет 35383033474447895560", "**5560"),
    ("","Введите счет или номер карты"),
    ("счет 3538303347444789556", "Вы ввели недостаточно цифр"),
    ("mastercard 715830073472675", "Вы ввели недостаточно цифр")])
def test_mask_account_card_2(acc_2, result_2):
    assert mask_account_card(acc_2) == result_2