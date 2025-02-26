import logging
from from_root import from_root
import os
from logging.handlers import RotatingFileHandler
from datetime import datetime

LOG_DIR = "logs"
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%S')}.log"
MAX_LOG_FILE = 5*1024*1024 #5MB
BACKUP_LOGS = 3

log_dir_path = os.path.join(from_root(),LOG_DIR)
os.makedirs(log_dir_path,exist_ok=True)
log_file_path = os.path.join(log_dir_path,LOG_FILE)

def configure_logger():
    
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    
    formatter = logging.Formatter("[%(asctime)s] %(name)s - %(levelname)s %(message)s")
    
    filehandler= RotatingFileHandler(log_file_path,maxBytes=MAX_LOG_FILE,backupCount=BACKUP_LOGS)
    filehandler.setFormatter(formatter)
    filehandler.setLevel(logging.DEBUG)
    
    console_handler =  logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel("DEBUG")
    
    logger.addHandler(filehandler)
    logger.addHandler(console_handler)
    
configure_logger()