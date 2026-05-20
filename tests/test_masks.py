import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number():
    # тест - номер карты в int корректной длины
    assert get_mask_card_number(1234567890123456) == "1234 56** **** 3456"
    # тест - номер карты str корректной длины
    assert get_mask_card_number("1234567890123456") == "1234 56** **** 3456"
    # тест - номер карты в int некорректной длины
    assert get_mask_card_number(123456789012345) == "1234 56** ***2 345"
    # тест - пустая строка в аргументе
    assert get_mask_card_number("") == ""
    # тест - некорректный формат ввода
    assert get_mask_card_number("1234 5678 9012 3456") == "1234  5** **** ***3 456"
    # тест - пустой аргумент
    with pytest.raises(TypeError):
        get_mask_card_number()


def test_get_mask_account():
    # тест - номер счета в int корректной длины
    assert get_mask_account(12345678901234567890) == "**7890"
    # тест - номер карты str корректной длины
    assert get_mask_account("12345678901234567890") == "**7890"
    # тест - номер карты в int некорректной длины
    assert get_mask_account(123456789012345) == "**2345"
    # тест - пустая строка в аргументе
    assert get_mask_account("") == "**"
    # тест - некорректный формат ввода
    assert get_mask_account("12345 67890 12345 67890") == "**7890"
    # тест - пустой аргумент
    with pytest.raises(TypeError):
        get_mask_account()
