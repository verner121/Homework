from typing import Any

from src.processing import filter_by_state


def test_filter_by_state(fixture_1: list[dict[str, Any]], state: str = "EXECUTED") -> None:
    assert filter_by_state(fixture_1, state="EXECUTED") == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}
    ]


def test_filter_by_state_2(fixture_2: list[dict[str, Any]], state: str = "EXECUTED") -> None:
    assert filter_by_state(fixture_2, state="EXECUTED") == "Значения state нет в списке"


def test_filter_by_state_3(fixture_1: list[dict[str, Any]], state: str = "EXECUTED") -> None:
    assert filter_by_state(fixture_1, state="CANCELED") == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"}
    ]
