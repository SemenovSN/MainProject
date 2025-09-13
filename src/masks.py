from typing import Union


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """
    Принимает номер карты в качестве аргумента. Возвращает маску номера карты.
    :param card_number: Номер карты вида XXXXXXXXXXXXXXXX
    :return: Маска карты вида XXXX XX** **** XXXX
    """
    l_border = 0
    tmp_list = []
    card_number = str(card_number)
    card_number = card_number.replace(card_number[6:-4], "*" * len(card_number[6:-4]))
    while l_border < len(card_number):
        tmp_list.append(card_number[l_border : l_border + 4])
        l_border += 4
    return " ".join(tmp_list).strip()


def get_mask_account(account: Union[int, str]) -> str:
    """
    Принимает номер счета в качестве аргумента. Возвращает маску номера счета.
    :param account: Номер счета вида XXXXXXXXXXXXXXXXXXXX
    :return: Маска счета вида **XXXX
    """
    account = str(account)
    return account.replace(account[:-4], "**")
