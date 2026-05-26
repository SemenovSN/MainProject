import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_currency(generators_input_fixture):
    gen_usd = filter_by_currency(generators_input_fixture, "USD")
    gen_rub = filter_by_currency(generators_input_fixture, "RUB")
    gen_eur = filter_by_currency(generators_input_fixture, "EUR")
    # тест - тестирование фильтра по коду USD
    assert next(gen_usd) == {"id":939719570,"state":"EXECUTED","date":"2018-06-30T02:08:58.425572","operationAmount":{"amount":"9824.07","currency":{"name":"USD","code":"USD"}},"description":"Перевод организации","from":"Счет 75106830613657916952","to":"Счет 11776614605963066702"}
    assert next(gen_usd) == {"id":142264268,"state":"EXECUTED","date":"2019-04-04T23:20:05.206878","operationAmount":{"amount":"79114.93","currency":{"name":"USD","code":"USD"}},"description":"Перевод со счета на счет","from":"Счет 19708645243227258542","to":"Счет 75651667383060284188"}
    assert next(gen_usd) == {"id":895315941,"state":"EXECUTED","date":"2018-08-19T04:27:37.904916","operationAmount":{"amount":"56883.54","currency":{"name":"USD","code":"USD"}},"description":"Перевод с карты на карту","from":"Visa Classic 6831982476737658","to":"Visa Platinum 8990922113665229"}
    # тест - тестирование фильтра по коду RUB
    assert next(gen_rub) == {"id":873106923,"state":"EXECUTED","date":"2019-03-23T01:09:46.296404","operationAmount":{"amount":"43318.34","currency":{"name":"руб.","code":"RUB"}},"description":"Перевод со счета на счет","from":"Счет 44812258784861134719","to":"Счет 74489636417521191160"}
    assert next(gen_rub) == {"id":594226727,"state":"CANCELED","date":"2018-09-12T21:27:25.241689","operationAmount":{"amount":"67314.70","currency":{"name":"руб.","code":"RUB"}},"description":"Перевод организации","from":"Visa Platinum 1246377376343588","to":"Счет 14211924144426031657"}
    # тест - тестирование по несуществующему коду
    with pytest.raises(StopIteration):
        assert next(gen_eur) == {"id":594226727,"state":"CANCELED","date":"2018-09-12T21:27:25.241689","operationAmount":{"amount":"67314.70","currency":{"name":"руб.","code":"RUB"}},"description":"Перевод организации","from":"Visa Platinum 1246377376343588","to":"Счет 14211924144426031657"}


def test_transaction_descriptions(generators_input_fixture):
    gen = transaction_descriptions(generators_input_fixture)
    # тест - тестирование получения описания до исчерпания генератора
    assert next(gen) == 'Перевод организации'
    assert next(gen) == 'Перевод со счета на счет'
    assert next(gen) == 'Перевод со счета на счет'
    assert next(gen) == 'Перевод с карты на карту'
    assert next(gen) == 'Перевод организации'
    # тест - тестирование получения описания при исчерпании генератора
    with pytest.raises(StopIteration):
        assert next(gen) == 'Перевод организации'


def test_card_number_generator():
    gen_normal = card_number_generator(1230, 1231)
    gen_single = card_number_generator(1234, 1234)
    gen_excess = card_number_generator(10000000000000000, 10000000000000000)
    #
    assert next(gen_normal) == '0000 0000 0000 1230'
    assert next(gen_normal) == '0000 0000 0000 1231'
    #
    assert next(gen_single) == '0000 0000 0000 1234'

