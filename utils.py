"""
utils.py

Minimal helper functions for directory, file save, and temporary file removal operations.
"""

import os


def save_uploaded_file(uploaded_file, upload_dir: str = "uploads") -> str:
    """Saves uploaded Streamlit file to the uploads directory."""
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)

    file_path = os.path.join(upload_dir, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    return file_path


def remove_file(file_path: str):
    """Safely removes a file from local storage if it exists."""
    try:
        if file_path and os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        print(f"Error removing temporary file {file_path}: {e}")
