import streamlit as st

from utils.data_manager import load_data
from config.settings import ROLES_FILE


st.title("Role & Permission Management")

roles = load_data(ROLES_FILE)

for role, permissions in roles.items():

    with st.expander(role):

        st.write("Assigned Permissions")

        for permission in permissions:

            st.write(f"✓ {permission}")

st.divider()

st.subheader("Permission Matrix")

all_permissions = sorted({
    permission
    for permissions in roles.values()
    for permission in permissions
})

matrix = []

for permission in all_permissions:

    row = {"Permission": permission}

    for role, permissions in roles.items():

        row[role] = (
            "Allowed"
            if permission in permissions
            else "Denied"
        )

    matrix.append(row)

st.dataframe(
    matrix,
    use_container_width=True
)