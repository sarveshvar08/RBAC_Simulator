#	Main application entry point
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

    st.title("RBAC Simulator")
    st.subheader("Secure Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        if authenticate_user(username, password):

            st.session_state.authenticated = True
            st.session_state.username = username
            st.success("Login successful!")
            st.rerun()
        else:
            st.error("Invalid username or password.")

def dashboard():

    username = st.session_state.username
    role = get_user_role(username)

    st.title("RBAC Dashboard")
    st.success(f"Welcome, {username}")
    st.info(f"Your Role: {role}")

    if st.button("Logout"):

        st.session_state.authenticated = False
        st.session_state.username = None
        st.rerun()

if st.session_state.authenticated:
    dashboard()
else:
    login_page()