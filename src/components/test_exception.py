from logger import logging
from src.exception.custom_exception import CustomException
import sys

if __name__ == "__main__":
    try:
        logging.info("Attempting a risky operation...")
        result = 10 / 0  # This will trigger an error
    except Exception as e:
        logging.info("Divide by Zero Error detected")
        # Raising the custom exception which provides the file and line number
        raise CustomException(e, sys)