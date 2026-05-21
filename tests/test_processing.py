import pytest

from src.processing import filter_by_state, sort_by_date

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
