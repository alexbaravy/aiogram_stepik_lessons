import os

def get_current_path_info():
    current_dir = os.path.dirname(__file__).split('\\')[-1]
    current_file = os.path.basename(__file__)
    return current_dir, current_file

if __name__=='__main__':
    current_dir, current_file = get_current_path_info()
    print(f"Current folder: {current_dir}")
    print(f"Current file: {current_file}")
