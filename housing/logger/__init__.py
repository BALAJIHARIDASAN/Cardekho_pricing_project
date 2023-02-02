
import logging
from datetime import datetime
import os
from housing.constant import *

LOG_DIR = 'housing.logs'


CURRENT_TIME_STAMP = get_current_time_stamp()

LOG_FILE_NAME = f'log_{CURRENT_TIME_STAMP}.log'


os.makedirs(LOG_DIR,exist_ok=True)

LOG_FILE_PATH = os.path.join(LOG_DIR,LOG_FILE_NAME)


logging.basicConfig(filename=LOG_FILE_PATH,filemode='w',format='[%asctime]%(name)s-%(levelname)s-%(message)s',level=logging.INFO)