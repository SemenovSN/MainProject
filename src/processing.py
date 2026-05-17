def filter_by_state(dictionary_list, state='EXECUTED'):
    """
    Принимает список словарей и опционально значение для ключа state (по умолчанию 'EXECUTED').
    Возвращает новый список словарей, содержащий только те словари, у которых ключ state соответствует указанному
    значению.
    :param dictionary_list: список словарей
    :param state: значение ключа
    :return: отфильтрованный по ключу state список
    """
    filter_by_state_result = []
    for dictionary in dictionary_list:
        for key, value in dictionary.items():
            if key == 'state' and value == state:
                filter_by_state_result.append(dictionary)
    return filter_by_state_result

def sort_by_date(dictionary_list, sort_order = True):
    return sorted(dictionary_list, key=lambda x: x['date'], reverse=sort_order)
