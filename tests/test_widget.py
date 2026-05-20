from src.widget import mask_account_card


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
    # тест - некорректный формат ввода
    # тест - пустой аргумент
    # тест - некорректный тип аргумента

def test_get_date():
    pass