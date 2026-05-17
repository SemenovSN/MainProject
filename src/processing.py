def filter_by_state(dictionary_list: list, state: str = "EXECUTED") -> list:
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
            if key == "state" and value == state:
                filter_by_state_result.append(dictionary)
    return filter_by_state_result


def sort_by_date(dictionary_list: list, sort_order: bool = True) -> list:
    """
    Принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание).
    Возвращает новый список, отсортированный по дате (date).
    :param dictionary_list: список словарей
    :param sort_order: порядок сортировки: True - по убыванию (по умолчанию), False - по возрастанию
    :return: сортированный по дате список словарей
    """
    return sorted(dictionary_list, key=lambda x: x["date"], reverse=sort_order)
