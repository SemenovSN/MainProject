import pytest

from src.processing import filter_by_state, sort_by_date
from tests.conftest import processing_fixture


@pytest.mark.parametrize('state, expected_result',
                         [('EXECUTED', [{'date': '2019-07-03T18:35:29.512364', 'id': 414288290, 'state': 'EXECUTED'},
                                        {'date': '2018-06-30T02:08:58.425572', 'id': 939719570, 'state': 'EXECUTED'},
                                        {'date': '2018-06-30T02:08:58.425572', 'id': 939719570, 'state': 'EXECUTED'}]),
                          ('CANCELED', [{'id': 939719570, 'state': 'CANCELED', 'date': '2018-06-30T02:08:58.425572'},
                                        {'id': 414288290, 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.512364'}]),
                          ('DELETED', [])])
def test_filter_by_state(processing_fixture, state, expected_result):
    # тест - параметризованный тест фильтрации по state
    assert filter_by_state(processing_fixture, state) == expected_result

@pytest.mark.parametrize('sort_order, expected_result',
                         [(True, [{'id': 414288290, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                  {'id': 414288290, 'state': 'UNKNOWN', 'date': '2019-07-03T18:35:29.512364'},
                                  {'id': 414288290, 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.512364'},
                                  {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                                  {'id': 939719570, 'state': 'CANCELED', 'date': '2018-06-30T02:08:58.425572'},
                                  {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]),
                          (False, [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                                   {'id': 939719570, 'state': 'CANCELED', 'date': '2018-06-30T02:08:58.425572'},
                                   {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                                   {'id': 414288290, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                   {'id': 414288290, 'state': 'UNKNOWN', 'date': '2019-07-03T18:35:29.512364'},
                                   {'id': 414288290, 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.512364'}]),
                          (None, [{'id': 414288290, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                  {'id': 414288290, 'state': 'UNKNOWN', 'date': '2019-07-03T18:35:29.512364'},
                                  {'id': 414288290, 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.512364'},
                                  {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                                  {'id': 939719570, 'state': 'CANCELED', 'date': '2018-06-30T02:08:58.425572'},
                                  {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}])])

def test_sort_by_date(processing_fixture, sort_order, expected_result):
    # проверка явной передачи аргумента sort_order
    if not sort_order is None:
        # тест - параметризованный тест сортировки sort_by_date с явной передачей аргумента sort_order
        assert sort_by_date(processing_fixture, sort_order) == expected_result
    else:
        # тест - параметризованный тест сортировки sort_by_date без явной передачи аргумента sort_order (по ум.)
        assert sort_by_date(processing_fixture) == expected_result