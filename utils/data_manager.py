import json
import os


def load_data(file_path):
    """Load data from a JSON file."""

    if not os.path.exists(file_path):
        return {}

    with open(file_path, "r") as file:
        return json.load(file)


def save_data(file_path, data):
    """Save data into a JSON file."""

    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)