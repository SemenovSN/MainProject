def filter_by_currency(transactions: list, currency_code: str) -> dict:
    for transaction in transactions:
        condition_check = transaction['operationAmount']['currency']['code']
        if condition_check == currency_code:
            yield transaction

def transaction_descriptions(transactions: list) -> str:
    for transaction in transactions:
        yield transaction["description"]
