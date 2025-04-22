import logging
import os
import sys 


LOG_FILE = 'logger.log'
log_file = 'log-files'

LOG_FILE_PATH = os.path.join('log-files',LOG_FILE)
os.makedirs(log_file,exist_ok=True)

logging.basicConfig(level=logging.INFO,format='[%(asctime)s] - %(levelname)s : %(module)s - %(message)s',
                    handlers= [logging.FileHandler(LOG_FILE_PATH),
                               logging.StreamHandler(sys.stdout)])


logger = logging.getLogger('NLPLogger')