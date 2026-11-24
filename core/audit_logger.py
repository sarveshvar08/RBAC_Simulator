import json
from datetime import datetime

def record_activity(username, role, resource, operation, status):

    log_entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "username": username,
        "role": role,
        "resource": resource,
        "operation": operation,
        "status": status
    }
    try:
        with open("data/audit_logs.json", "r") as file:
            logs = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        logs = []

    logs.append(log_entry)

    with open("data/audit_logs.json", "w") as file:
        json.dump(logs, file, indent=4)