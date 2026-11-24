# Application settings and file paths
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"

USERS_FILE = DATA_DIR / "users.json"
ROLES_FILE = DATA_DIR / "roles.json"
RESOURCES_FILE = DATA_DIR / "resources.json"
AUDIT_LOGS_FILE = DATA_DIR / "audit_logs.json"