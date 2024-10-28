from os_values import get_current_path_info

current_dir, current_file = get_current_path_info()

print(f'{current_file} in packet {current_dir}: {__name__}')
print('=========================')

from . import file_211
from .file_212 import *
