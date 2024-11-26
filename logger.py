# utils/logger.py

import logging

# Configure logging
logging.basicConfig(
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="error.log",  # Logs will be saved to error.log
    filemode="a"           # Append to the file
)

def log_error(message: str):
    """Log an error message to the error log."""
    logging.error(message)
