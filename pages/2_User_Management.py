import streamlit as st

from core.authentication import register_user
from utils.data_manager import load_data
from config.settings import USERS_FILE, ROLES_FILE


st.title("User Management")

st.caption("Create and manage system users")

users = load_data(USERS_FILE)
roles = load_data(ROLES_FILE)

st.subheader("Register New User")

with st.form("register_user"):

    username = st.text_input("Username")

    password = st.text_input(
        "Password",
        type="password"
    )

    role = st.selectbox(
        "Assign Role",
        list(roles.keys())
    )

    submitted = st.form_submit_button(
        "Create User"
    )

    if submitted:

        if not username.strip() or not password:

            st.error("All fields are required.")

        else:

            success, message = register_user(
                username.strip(),
                password,
                role
            )

            if success:
                st.success(message)
                st.rerun()

            else:
                st.error(message)


st.divider()

st.subheader("Existing Users")

users = load_data(USERS_FILE)

user_data = [
    {
        "Username": username,
        "Role": details["role"]
    }
    for username, details in users.items()
]

st.dataframe(
    user_data,
    use_container_width=True
)