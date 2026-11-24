from core.access_controller import execute_operation


print("\n========== RBAC SIMULATOR ==========")

# Test 1: Student views academic notes
print("\nTest 1: Student viewing notes")

result = execute_operation(
    "student01",
    "academic_notes",
    "view"
)

print(result)


# Test 2: Student tries deleting system files
print("\nTest 2: Student deleting system files")

result = execute_operation(
    "student01",
    "system_files",
    "delete",
    index=0
)

print(result)


# Test 3: Faculty uploads notes
print("\nTest 3: Faculty uploading notes")

result = execute_operation(
    "faculty01",
    "academic_notes",
    "upload",
    note="Introduction to Operating Systems"
)

print(result)


# Test 4: Guest tries viewing student records
print("\nTest 4: Guest accessing student records")

result = execute_operation(
    "guest01",
    "student_records",
    "view"
)

print(result)


# Test 5: Administrator deletes system file
print("\nTest 5: Administrator deleting system file")

result = execute_operation(
    "admin01",
    "system_files",
    "delete",
    index=0
)

print(result)

print("\n====================================")