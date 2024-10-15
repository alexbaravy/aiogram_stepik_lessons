print('File', __name__)
print('=========================')

from .file_12 import num


def some_func(n: int) -> float:
    return (n + n) / n ** n


result = some_func(num)
