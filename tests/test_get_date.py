import pytest
from src.widget import get_date

def test_get_date():
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"

@pytest.mark.parametrize("date, result",
                         [("2024-03-1102:26:18.671407", "Введите корректные данные"),
                          ("", "Введите корректные данные")])
def test_get_date_2(date, result):
    assert get_date(date) == result