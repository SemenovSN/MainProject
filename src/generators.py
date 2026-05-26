from typing import Iterator


def filter_by_currency(transactions_list: list, currency_code: str) -> Iterator[dict]:
    for transaction in transactions_list:
        condition_check = transaction['operationAmount']['currency']['code']
        if condition_check == currency_code:
            yield transaction

def transaction_descriptions(transactions_list: list) -> Iterator[str]:
    for transaction in transactions_list:
        yield transaction["description"]

def card_number_generator(start: int, stop: int) -> Iterator[str]:
    for generated_number in range(start, stop + 1):
        generated_number = str(generated_number)
        template = '0' * (16 - len(generated_number)) + str(generated_number)
        result = f'{template[:4]} {template[4:8]} {template[8:12]} {template[12:]}'
        yield result
