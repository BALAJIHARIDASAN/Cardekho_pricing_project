import os
from datetime import datetime


ROOT_DIR = os.getcwd() # current working directory


CONFIG_DIR = 'config'


CONFIG_FILE_NAME = 'config.yaml'

CONFIG_FILE_PATH = os.path.join(ROOT_DIR,CONFIG_DIR,CONFIG_FILE_NAME)  # This variable gives the path of config yaml file



def get_current_time_stamp():
    return f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"


CURRENT_TIME_STAMP = get_current_time_stamp()

