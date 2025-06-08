import logging
import os
from datetime import datetime

def setup_logger(log_name: str = 'sauce_demo'):

    # Create logs directory if it doesn't exist
    os.makedirs("logs", exist_ok=True)
    
    # Timestamped log file for uniqueness
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_filename = f"logs/{log_name}_{timestamp}.log"

    logger = logging.getLogger(log_name)
    logger.setLevel(logging.DEBUG)
    logger.propagate = False  # Prevents duplicate logs

    # File handler
    fh = logging.FileHandler(log_filename)
    fh.setLevel(logging.DEBUG)

    # Console handler
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    formatter = logging.Formatter('%(name)s  %(asctime)s - %(levelname)s - %(message)s')

    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(fh)
        logger.addHandler(ch)

    return logger
