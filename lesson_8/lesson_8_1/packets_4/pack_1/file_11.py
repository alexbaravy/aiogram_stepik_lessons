from os_values import get_current_path_info

current_dir, current_file = get_current_path_info()

print(f'{current_file} in packet {current_dir}: {__name__}')
print('=========================')

__all__ = ['some_var', 'yet_another_var', 'another_func']

some_var: int = 42
another_var: int = 242
yet_another_var: str = 'some_text'

def _reverse_text(text: str) -> str:
    return text[::-1]


def some_func(text: str, times: int) -> str:
    return _reverse_text(text * times)


def another_func() -> None:
    pass