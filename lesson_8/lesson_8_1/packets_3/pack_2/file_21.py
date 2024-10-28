import os

current_file = os.path.basename(__file__)

print(f'File {current_file}: {__name__}')
print('=========================')

def another_some_func(n: int) -> int:
    return n * n
