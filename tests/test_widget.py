import pytest
from src.widget import mask_account_card, get_date


def test_mask_account_card():
    # тест - номер карты корректной длины
    assert (mask_account_card('Visa Platinum 1234567890123456') ==
            'Visa Platinum 1234 56** **** 3456')
    # тест - номер счета корректной длины
    assert mask_account_card('Счет 12345678901234567890') == 'Счет **7890'
    # тест - номер карты некорректной длины
    assert (mask_account_card('Visa Platinum 12345678901234567890') ==
            'Visa Platinum 1234 56** **** **** 7890')
    # тест - номер счета некорректной длины
    assert mask_account_card('Счет 1234567890123456') == 'Счет **3456'
    # тест - номер без указания типа (карта или счет)
    assert mask_account_card('1234567890123456') == ' 1234 56** **** 3456'
    # тест - тип (счет) без номера счета
    assert mask_account_card('Счет') == ' **С**ч**е**т**'
    # тест - тип (карта) без номера карты
    assert mask_account_card('1234567890123456') == ' 1234 56** **** 3456'
    # тест - некорректный формат ввода
    assert mask_account_card('random string') == 'random stri ng'
    # тест - пустой аргумент
    with pytest.raises(TypeError):
        mask_account_card()

def test_get_date():
    # тест - корректная дата и время в формате ISO 8601
    assert get_date('2000-01-01T00:00:00.000000') == '01.01.2000'
    # тест - некорректная дата (в формате ДД.ММ.ГГГГ) и время в формате ISO 8601
    assert get_date('01.01.2000T00:00:00.000000') == '01.01.2000'
    # тест - корректная дата в формате ISO 8601 с сепаратором
    assert get_date('2000-01-01T') == '01.01.2000'
    # тест - корректное время в формате ISO 8601 с сепаратором
    assert get_date('T00:00:00.000000') == ''
    # тест - пустой аргумент
    with pytest.raises(TypeError):
        assert  get_date()
    # тесты исключений
    with pytest.raises(ValueError):
        # тест - дата и время в формате ISO 8601 c с некорректным сепаратором
        assert get_date('2000-01-01A00:00:00.000000') == 'Счет **7890'
        # тест - дата в формате ISO 8601 без сепаратора
        assert get_date('2000-01-01') == 'Счет **7890'
