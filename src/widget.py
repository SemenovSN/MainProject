from masks import get_mask_account, get_mask_card_number


def mask_account_card(input_data: str) -> str:
    """
    Принимает один аргумент — строку, содержащую тип и номер карты или счета вида:
    1. Visa Platinum XXXXXXXXXXXXXXXX
    2. Счет XXXXXXXXXXXXXXXXXXXX
    Возвращает строку с замаскированным номером вида:
    1. Visa Platinum XXXX XX** **** XXXX
    2. Счет **XXXX
    :param input_data: строка с типом и номером карты/счета вида
    :return: строка с замаскированным номером
    """
    tmp_data = input_data.split(" ")
    if "счет" in input_data.lower():
        return f'{" ".join(tmp_data[:-1])} {get_mask_account(tmp_data[-1])}'
    else:
        return f'{" ".join(tmp_data[:-1])} {get_mask_card_number(tmp_data[-1])}'


def get_date(input_date: str) -> str:
    """
    Принимает на вход строку с датой в формате ISO 8601 (прим. "2024-03-11T02:26:18.671407")
    Возвращает строку в формате "ДД.ММ.ГГГГ"
    :param input_date: строка в формате ISO 8601
    :return: строка в формате ДД.ММ.ГГГГ
    """
    date_list = input_date[: input_date.index("T")].split("-")[-1::-1]
    return ".".join(date_list)
