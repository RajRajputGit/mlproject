import sys
# IMPORTANT: Import your local logger first to trigger the config
from src.logger import logging 
from src.exception.custom_exception import CustomException

if __name__=="__main__":
    try:
        logging.info("Logging has started successfully!") # Test message
        a = 1 / 0
    except Exception as e:
        # This will trigger the logging inside CustomException
        raise CustomException(e, sys) from None