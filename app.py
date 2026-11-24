import streamlit as st

from core.authentication import authenticate_user
from core.role_manager import get_user_role

st.set_page_config(
    page_title="RBAC Simulator",
    page_icon="🔐",
    layout="wide"
)

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if "username" not in st.session_state:
    st.session_state.username = None

def login_page():

    st.title("🔐 RBAC Simulator")
    st.caption("Role-Based Access Control Management System")
    st.divider()
    col1, col2, col3 = st.columns([1, 1.2, 1])

    with col2:
        st.subheader("Welcome Back")
        username = st.text_input("Username")
        password = st.text_input(
            "Password",
            type="password"
        )
        if st.button("Login", use_container_width=True):

            if authenticate_user(username, password):
                st.session_state.authenticated = True
                st.session_state.username = username
                st.rerun()
            else:
                st.error("Invalid username or password.")

def main():

    if not st.session_state.authenticated:
        login_page()
    else:

        username = st.session_state.username
        role = get_user_role(username)
        st.sidebar.title("RBAC Simulator")
        st.sidebar.success(
            f"Logged in: {username}"
        )
        st.sidebar.info(
            f"Role: {role}"
        )

        if st.sidebar.button("Logout"):

            st.session_state.authenticated = False
            st.session_state.username = None
            st.rerun()
        st.title("Welcome to RBAC Simulator")
        st.write(
            "Use the navigation menu to explore the system."
        )

main()