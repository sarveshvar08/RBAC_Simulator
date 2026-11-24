import streamlit as st

from core.access_controller import execute_operation


st.title("Protected Resources")

st.caption(
    "Access system resources according to assigned permissions."
)

resources = {
    "Public Files": "public_files",
    "Academic Notes": "academic_notes",
    "Student Records": "student_records"
}

selected_resource = st.selectbox(
    "Choose Resource",
    list(resources.keys())
)

resource_id = resources[selected_resource]

if st.button("View Resource"):

    result = execute_operation(
        st.session_state.username,
        resource_id,
        "view"
    )

    if isinstance(result, str) and result.startswith("ACCESS DENIED"):

        st.error(result)

    elif isinstance(result, str):

        st.error(result)

    else:

        st.success("Access Granted")

        for item in result:

            st.write("•", item)