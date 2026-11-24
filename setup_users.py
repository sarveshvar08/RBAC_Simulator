from core.authentication import register_user

sample_users = [
    ("admin01", "Admin@123", "Administrator"),
    ("faculty01", "Faculty@123", "Faculty"),
    ("student01", "Student@123", "Student"),
    ("guest01", "Guest@123", "Guest")
]

for username, password, role in sample_users:

    success, message = register_user(
        username,
        password,
        role
    )

    print(username, "-", message)