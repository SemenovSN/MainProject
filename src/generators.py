from typing import Iterator


def filter_by_currency(transactions_list: list, currency_code: str) -> Iterator[dict]:
    """
    Функция принимает на вход 2 аргумента: список транзакций и код валюты.
    Возвращает транзакции с данным типом валют.
    :param transactions_list: список транзакций типа list
    :param currency_code: код валюты типа str
    :return: транзакции с данным типом валюты (итератор типа dict).
    """
    for transaction in transactions_list:
        condition_check = transaction["operationAmount"]["currency"]["code"]
        if condition_check == currency_code:
            yield transaction


def transaction_descriptions(transactions_list: list) -> Iterator[str]:
    """
    Функция принимает на вход список транзакций.
    Возвращает описание по каждой транзакции
    :param transactions_list: список транзакций типа list
    :return: описание транзакции типа str
    """
    for transaction in transactions_list:
        yield transaction["description"]


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """
    Функция принимает на вход 2 аргумента: стартовую и конечную позиции для генерации.
    Возвращает номер карты в формате XXXX XXXX XXXX XXXX.
    :param start: начальная позиция генерации типа int
    :param stop: конечная позиция генерации типа int
    :return: номер карты типа str
    """
    for generated_number in range(start, stop + 1):
        generated_number_str = str(generated_number)
        template = "0" * (16 - len(generated_number_str)) + generated_number_str
        result = f"{template[:4]} {template[4:8]} {template[8:12]} {template[12:]}"
        if len(result) == 19:
            yield result
        else:
            raise ValueError
