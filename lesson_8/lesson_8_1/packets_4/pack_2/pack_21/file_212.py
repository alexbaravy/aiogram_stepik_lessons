from os_values import get_current_path_info

current_dir, current_file = get_current_path_info()

print(f'{current_file} in packet {current_dir}: {__name__}')
print('=========================')

var_1: int = 1
var_2: str = 'Some Text'


def _reverse_text(text: str) -> str:
    return text[::-1]


def some_func(text: str, times: int) -> str:
    return _reverse_text(text * times)
