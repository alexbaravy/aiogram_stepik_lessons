import pickle

def save_users():
    with open('users_data.pkl', 'wb') as f:
        pickle.dump(users, f)

def load_users():
    try:
        with open('users_data.pkl', 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return {}

users = load_users()