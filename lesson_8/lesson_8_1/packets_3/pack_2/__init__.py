import os

from pack_2.file_21 import another_some_func

current_dir = os.path.dirname(__file__).split('\\')[-1]
last_folder = current_dir
current_file = os.path.basename(__file__)

print(f'{current_file} in packet {last_folder}: {__name__}')
print('=========================')
