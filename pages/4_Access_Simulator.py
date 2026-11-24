import streamlit as st

from core.access_controller import execute_operation
from utils.data_manager import load_data
from config.settings import USERS_FILE


st.title("Access Control Simulator")

st.caption(
    "Test whether a user can access protected resources."
)

users = load_data(USERS_FILE)

if not users:

    st.warning("No users available.")

else:

    username = st.selectbox(
        "Select User",
        list(users.keys())
    )

    resource = st.selectbox(
        "Select Resource",
        [
            "public_files",
            "academic_notes",
            "student_records",
            "system_files"
        ]
    )

    operations = {
        "public_files": ["view"],
        "academic_notes": ["view", "upload"],
        "student_records": ["view", "edit"],
        "system_files": ["delete"]
    }

    operation = st.selectbox(
        "Select Operation",
        operations[resource]
    )

    st.divider()

    st.subheader("Access Request")

    st.write("User:", username)
    st.write("Role:", users[username]["role"])
    st.write("Resource:", resource)
    st.write("Operation:", operation)

    if st.button("Check Access", use_container_width=True):

        if username != st.session_state.username:

            st.error(
                "You can only perform operations using your own authenticated account."
            )

        else:

            if resource == "academic_notes" and operation == "upload":

                result = execute_operation(
                    username,
                    resource,
                    operation,
                    note="Sample uploaded note"
                )

            elif resource == "student_records" and operation == "edit":

                result = execute_operation(
                    username,
                    resource,
                    operation,
                    index=0,
                    updated_record="Updated student record"
                )

            elif resource == "system_files" and operation == "delete":

                result = execute_operation(
                    username,
                    resource,
                    operation,
                    index=0
                )

            else:

                result = execute_operation(
                    username,
                    resource,
                    operation
                )

            st.write("### Result")

            if isinstance(result, str) and result.startswith("ACCESS DENIED"):

                st.error(result)

            else:

                st.success("Operation completed.")
                st.write(result)