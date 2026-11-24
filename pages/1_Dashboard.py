import streamlit as st

from utils.data_manager import load_data
from config.settings import USERS_FILE, ROLES_FILE, AUDIT_LOGS_FILE


st.title("System Dashboard")

st.caption("RBAC Security Monitoring System")

users = load_data(USERS_FILE)
roles = load_data(ROLES_FILE)
logs = load_data(AUDIT_LOGS_FILE)

if not isinstance(logs, list):
    logs = []

total_users = len(users)
total_roles = len(roles)

allowed = sum(
    1 for log in logs
    if log.get("status") == "ALLOWED"
)

denied = sum(
    1 for log in logs
    if log.get("status") == "DENIED"
)

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Users", total_users)
col2.metric("Total Roles", total_roles)
col3.metric("Access Granted", allowed)
col4.metric("Access Denied", denied)

st.divider()

st.subheader("Registered Users")

if users:

    user_data = []

    for username, details in users.items():

        user_data.append({
            "Username": username,
            "Role": details["role"]
        })

    st.dataframe(
        user_data,
        use_container_width=True
    )

else:

    st.info("No users registered.")

st.divider()

st.subheader("Recent Security Activity")

if logs:

    st.dataframe(
        logs[-10:][::-1],
        use_container_width=True
    )

else:

    st.info("No security activity recorded yet.")