from utils.data_manager import load_data
from config.settings import ROLES_FILE

def check_permission(role, permission):

    roles = load_data(ROLES_FILE)
    if role not in roles:
        return False

    return permission in roles[role]