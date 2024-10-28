import os
import inspect


def get_current_path_info():
    # Получаем фрейм вызывающего файла
    caller_frame = inspect.stack()[1]
    caller_file = caller_frame.filename

    current_dir = os.path.dirname(caller_file).split('\\')[-1]
    current_file = os.path.basename(caller_file)

    return current_dir, current_file


if __name__ == '__main__':
    current_dir, current_file = get_current_path_info()
    print(f"Current dir: {current_dir}")
    print(f"Current file: {current_file}")
