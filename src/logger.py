import logging
import os
from datetime import datetime

# Create a unique log file name with timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the logs directory path
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)  # Ensure the directory exists

# Full log file path
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Create a custom logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# File handler to write logs to a file
file_handler = logging.FileHandler(LOG_FILE_PATH)
file_handler.setLevel(logging.INFO)

# Console handler to print logs to the console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Define the log format
formatter = logging.Formatter("[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)



