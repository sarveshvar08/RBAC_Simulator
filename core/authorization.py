from utils.data_manager import load_data

def check_permission(role, permission):
    #Check whether a role has the requested permission.

    roles = load_data("data/roles.json")
    if role not in roles:
        return False
    if permission in roles[role]:
        return True

    return False