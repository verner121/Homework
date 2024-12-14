import pytest

@pytest.fixture
def fixture_1():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}]

@pytest.fixture
def fixture_2():
    return [{'id': 41428829, 'date': '2019-07-03T18:35:29.512364'}]



