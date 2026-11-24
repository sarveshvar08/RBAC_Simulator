# Role-Based Access Control (RBAC) Simulator

A Python-based Operating Systems project that demonstrates how role-based authorization can protect application resources. The simulator models four roles—**Administrator, Faculty, Student, and Guest**—and checks permissions before allowing protected operations.

> **Academic scope:** This is a controlled, user-space simulation for CSE234 Operating Systems. It does not modify the operating-system kernel or enforce permissions on files outside this application.

## Project at a glance

- **Course:** CSE234 – Operating Systems
- **Project number:** 16
- **Course outcome:** CO5 – Protection and Security
- **Bloom's levels:** L3, L4, L5
- **Language:** Python
- **Interface:** Streamlit
- **Data storage:** JSON

## Features

- Role-to-permission mapping for Administrator, Faculty, Student and Guest.
- Permission checks using resource-specific identifiers such as `academic_notes.view`.
- Simulated protected resources and operations.
- Password authentication using salted PBKDF2-HMAC-SHA256 hashes.
- Session-aware application flow.
- Audit records for allowed and denied access attempts.
- Streamlit pages for dashboard, user management, permissions, access simulation, resources and logs.

**Implementation note:** Treat this list as the intended project feature set. Before submission, verify that every feature is implemented and protected in the final code. In particular, enforce administrator-only actions and authorization inside backend functions—not only in the Streamlit interface.

## Architecture

```text
Streamlit UI
    |
Authentication and Session
    |
Role Manager
    |
Authorization Engine
    |
Access Controller
    |
Protected Resource Manager
    |
JSON Data Files + Audit Logger
```

### Main modules

| Path | Responsibility |
|---|---|
| `app.py` | Streamlit application entry point and login flow |
| `core/authentication.py` | User registration, password hashing and login verification |
| `core/authorization.py` | Checks whether a role has a requested permission |
| `core/role_manager.py` | Retrieves user-role assignments |
| `core/access_controller.py` | Checks authorization before protected operations |
| `core/audit_logger.py` | Records access decisions |
| `resources/resource_manager.py` | Performs simulated resource operations |
| `utils/data_manager.py` | Reads and writes JSON data |
| `config/settings.py` | Centralized project and data-file paths |
| `data/users.json` | User records and password hashes |
| `data/roles.json` | Role-permission policies |
| `data/resources.json` | Simulated protected resources |
| `data/audit_logs.json` | Access history |
| `pages/` | Streamlit dashboard and feature pages |
| `tests/` | Automated tests |

## Requirements

- Python 3.10 or newer recommended
- pip
- A terminal (PowerShell, Command Prompt, or shell)
- Visual Studio Code or another Python editor

## Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd RBAC-Simulator
```

If you have not pushed the project to GitHub yet, open the project folder directly in your editor.

### 2. Create and activate a virtual environment

**Windows PowerShell**

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Windows Command Prompt**

```cmd
py -m venv .venv
.venv\Scripts\activate.bat
```

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

Create or update `requirements.txt` with the packages used by the application:

```text
streamlit
pandas
pytest
```

Then install:

```bash
python -m pip install -r requirements.txt
```

### 4. Check the data files

Ensure the `data/` directory contains valid JSON files:

- `users.json`
- `roles.json`
- `resources.json`
- `audit_logs.json`

An empty audit log should contain:

```json
[]
```

Role policies should use the same permission identifiers expected by the access controller. For example:

```json
{
  "Student": [
    "public_files.view",
    "academic_notes.view"
  ],
  "Guest": [
    "public_files.view"
  ]
}
```

Do not commit real user passwords, production credentials or private data.

### 5. Create demonstration users

If the project includes `setup_users.py`, review the sample credentials in that file and run it once to create password hashes:

```bash
python setup_users.py
```

The setup script should not be run repeatedly against an already populated user file unless duplicate-user behavior is expected. Change all sample credentials before sharing or deploying the project.

## Run the application

From the project root:

```bash
python -m streamlit run app.py
```

Streamlit will print a local address in the terminal. Open that address in your browser.

## Run tests

Run the automated test suite, if the test files have been added:

```bash
python -m pytest -q
```

Standalone demonstration scripts can be run with:

```bash
python test_rbac.py
python test_phase2.py
python test_authentication.py
```

Run only the scripts that exist in your current project version.

## Example access policy

The following is an illustrative policy. The actual `data/roles.json` file is the source of truth for the running application.

| Permission | Administrator | Faculty | Student | Guest |
|---|---:|---:|---:|---:|
| `public_files.view` | Allow | Allow | Allow | Allow |
| `academic_notes.view` | Allow | Allow | Allow | Deny |
| `academic_notes.upload` | Allow | Allow | Deny | Deny |
| `student_records.view` | Allow | Allow | Deny | Deny |
| `student_records.edit` | Allow | Allow | Deny | Deny |
| `system_files.delete` | Allow | Deny | Deny | Deny |

## Test scenarios

| ID | Role | Requested operation | Expected decision |
|---|---|---|---|
| TC-01 | Student | View academic notes | Allow |
| TC-02 | Student | Delete system file | Deny |
| TC-03 | Faculty | Upload academic note | Allow |
| TC-04 | Guest | View student records | Deny |
| TC-05 | Administrator | Delete system file | Allow |
| TC-06 | Any user | Login with incorrect password | Reject |
| TC-07 | Unknown role | Request protected permission | Deny |
| TC-08 | Unauthenticated session | Request protected operation | Deny |

Record the **actual** result for each test before submitting the report. Do not label an expected result as a passed test until it has been executed.

## Evaluation metric

A useful security metric for this project is the access-denial rate:

```text
Access-denial rate (%) =
(Number of denied requests / Total access requests) × 100
```

Also report:

- Total access requests
- Allowed requests
- Denied requests
- Test cases passed
- Any invalid or failed operations

Calculate these values from the final audit log. Do not insert sample or estimated numbers as project results.

## Security design principles

1. **Default deny:** Unknown roles and missing permissions must be denied.
2. **Least privilege:** Assign each role only the permissions required for its tasks.
3. **Centralized authorization:** Protected operations must pass through a trusted backend authorization check.
4. **Session identity:** Derive the acting user from the authenticated session; do not trust a username submitted by a client.
5. **Password storage:** Store salted password hashes, never plaintext passwords.
6. **Accurate audit trail:** Record the final operation outcome; invalid or failed operations must not be recorded as successful.
7. **Administrative restrictions:** User creation and role-policy changes must be authorized on the backend.

## Limitations

- The simulator protects resources inside the application only; it is not an operating-system kernel security module.
- JSON files are appropriate for a small demonstration but do not provide robust concurrent writes or database transactions.
- Local audit files are not tamper-proof.
- A production deployment would require stronger session controls, secure configuration, database-backed storage, validation, monitoring and security review.


## Contributors

| Name | Registration number | Contribution |
|---|---|---|
| [Student 1] | [Registration number] | [Contribution] |
| [Student 2] | [Registration number] | [Contribution] |
| [Student 3] | [Registration number] | [Contribution] |

## References

- [Python `hashlib` documentation](https://docs.python.org/3/library/hashlib.html)
- [Python `secrets` documentation](https://docs.python.org/3/library/secrets.html)
- [Streamlit documentation](https://docs.streamlit.io/)
- [NIST Role-Based Access Control resources](https://csrc.nist.gov/projects/role-based-access-control)

---

