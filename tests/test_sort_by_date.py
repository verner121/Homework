from typing import Any


from src.processing import sort_by_date


def test_sort_by_date(fixture_3: list[dict[str, Any]]) -> None:
    assert sort_by_date(fixture_3, reverse=True) == [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]


def test_sort_by_date_2(fixture_3: list[dict[str, Any]]) -> None:
    assert sort_by_date(fixture_3, reverse=False) == [
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]


def test_sort_by_date_3(fixture_4: list[dict[str, Any]]) -> None:

    assert sort_by_date(fixture_4, reverse=True) == fixture_4


def test_sort_by_date_4(fixture_5: list[dict[str, Any]]) -> None:

    assert sort_by_date(fixture_5, reverse=True) == "Вы ввели некоректные данные"
