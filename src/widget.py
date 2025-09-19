from masks import get_mask_account, get_mask_card_number


def mask_card_account(input_data: str) -> str:
    tmp_data = input_data.split(' ')
    if 'счет' in input_data.lower():
        return f'{" ".join(tmp_data[:-1])} {get_mask_account(tmp_data[-1])}'
    else:
        return f'{" ".join(tmp_data[:-1])} {get_mask_card_number(tmp_data[-1])}'