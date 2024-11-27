import os
import subprocess
from utils.logger import log_error

def extract_exif_data(file_path):
    """Extract EXIF metadata."""
    try:
        if not os.path.isfile(file_path):
            return f"Error: File '{file_path}' does not exist."
        command = ['exiftool', file_path]
        process = subprocess.run(command, capture_output=True, text=True)
        return process.stdout if process.returncode == 0 else process.stderr
    except Exception as e:
        log_error(f"EXIF extraction failed: {e}")
        return f"Error occurred: {e}"
