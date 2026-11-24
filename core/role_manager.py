from utils.data_manager import load_data
from config.settings import USERS_FILE

def get_user_role(username):

    users = load_data(USERS_FILE)

    if username not in users:
        return None

    return users[username]["role"]