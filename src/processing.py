def filter_by_state(dictionary_list, state='EXECUTED'):
    filter_by_state_result = []
    for dictionary in dictionary_list:
        for key, value in dictionary.items():
            if key == 'state' and value == state:
                filter_by_state_result.append(dictionary)
    return filter_by_state_result
