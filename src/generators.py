def filter_by_currency(transactions: list, currency_code: str) -> dict:
    for transaction in transactions:
        condition_check = transaction['operationAmount']['currency']['code']
        if condition_check == currency_code:
            yield transaction
