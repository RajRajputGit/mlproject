import logging
import os
from datetime import datetime

# create logs folder
logs_dir = "logs"
os.makedirs(logs_dir, exist_ok=True)

# log file name
log_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_path = os.path.join(logs_dir, log_file)

# create logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# file handler (this writes to the file)
file_handler = logging.FileHandler(log_path)

# log format
formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)
file_handler.setFormatter(formatter)

# connect file to logger
logger.addHandler(file_handler)
