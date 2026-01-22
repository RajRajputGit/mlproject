import logging
import os
from datetime import datetime

# 1. Create a naming convention for the log file (e.g., 01_22_2026_12_30_00.log)
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# 2. Create a 'logs' folder in the current directory
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(os.path.dirname(logs_path), exist_ok=True)

# 3. Basic Configuration
logging.basicConfig(
    filename=logs_path,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# This allows other files to simply 'from src.logger import logging'