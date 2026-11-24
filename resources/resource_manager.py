from utils.data_manager import load_data, save_data
from config.settings import RESOURCES_FILE

def view_resource(resource_id):

    resources = load_data(RESOURCES_FILE)

    if resource_id not in resources:
        return "Resource not found."

    return resources[resource_id]["content"]

def upload_note(note):

    resources = load_data(RESOURCES_FILE)

    if "academic_notes" not in resources:
        return "Academic notes resource not found."

    resources["academic_notes"]["content"].append(note)
    save_data(RESOURCES_FILE, resources)

    return "Note uploaded successfully."

def edit_student_record(index, updated_record):

    resources = load_data(RESOURCES_FILE)

    if "student_records" not in resources:
        return "Student records not found."

    records = resources["student_records"]["content"]

    if index < 0 or index >= len(records):
        return "Invalid record index."

    records[index] = updated_record
    save_data(RESOURCES_FILE, resources)

    return "Student record updated successfully."

def delete_system_file(index):

    resources = load_data(RESOURCES_FILE)

    if "system_files" not in resources:
        return "System files not found."

    files = resources["system_files"]["content"]

    if index < 0 or index >= len(files):
        return "Invalid file index."
    
    deleted_file = files.pop(index)
    save_data(RESOURCES_FILE, resources)

    return f"Deleted: {deleted_file}"