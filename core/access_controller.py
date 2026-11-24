import streamlit as st

from core.authorization import check_permission
from core.role_manager import get_user_role
from core.audit_logger import record_activity

from resources.resource_manager import (
    view_resource,
    upload_note,
    edit_student_record,
    delete_system_file
)

def execute_operation(username, resource, operation, **kwargs):

    if not st.session_state.get("authenticated", False):
        return "ACCESS DENIED: Please login first."

    if st.session_state.get("username") != username:
        return "ACCESS DENIED: Session user mismatch."

def execute_operation(username, resource, operation, **kwargs):

    role = get_user_role(username)

    if role is None:
        record_activity(
            username, "Unknown", resource, operation, "DENIED"
        )
        return "Access Denied: User not found."

    permission = f"{resource}.{operation}"

    if not check_permission(role, permission):
        record_activity(
            username, role, resource, operation, "DENIED"
        )
        return "ACCESS DENIED: Insufficient permissions."

    if resource == "public_files" and operation == "view":
        result = view_resource(resource)
    elif resource == "academic_notes" and operation == "view":
        result = view_resource(resource)
    elif resource == "academic_notes" and operation == "upload":
        result = upload_note(kwargs.get("note", ""))
    elif resource == "student_records" and operation == "view":
        result = view_resource(resource)
    elif resource == "student_records" and operation == "edit":
        result = edit_student_record(
            kwargs.get("index", -1),
            kwargs.get("updated_record", "")
        )
    elif resource == "system_files" and operation == "delete":
        result = delete_system_file(kwargs.get("index", -1))
    else:
        result = "Invalid operation."

    record_activity(
        username, role, resource, operation, "ALLOWED"
    )

    return result