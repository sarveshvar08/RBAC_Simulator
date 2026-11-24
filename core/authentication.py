import hashlib
import secrets

from utils.data_manager import load_data, save_data
from config.settings import USERS_FILE

def hash_password(password, salt=None):

    if salt is None:
        salt = secrets.token_hex(16)

    password_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        bytes.fromhex(salt),
        600000
    )
    return salt, password_hash.hex()

def register_user(username, password, role):

    users = load_data(USERS_FILE)
    if username in users:
        return False, "Username already exists."

    salt, password_hash = hash_password(password)
    users[username] = {
        "username": username,
        "role": role,
        "salt": salt,
        "password_hash": password_hash
    }
    save_data(USERS_FILE, users)
    return True, "User registered successfully."

def authenticate_user(username, password):

    users = load_data(USERS_FILE)

    if username not in users:
        return False

    user = users[username]
    salt = user["salt"]
    _, entered_hash = hash_password(password, salt)
    return secrets.compare_digest(
        entered_hash,
        user["password_hash"]
    )