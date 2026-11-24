from utils.data_manager import load_data

def get_user_role(username):
    #Return the role assigned to a user.

    users = load_data("data/users.json")
    
    if username not in users:
        return None
    
    return users[username]["role"]