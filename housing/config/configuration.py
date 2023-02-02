

from housing.entity.config_entity import *
from housing.utils.util import read_yaml_file
from housing.constant import *
#from housing.logger import logging
from housing.Exception import HousingException
import sys







class Configuration:


    def __init__(self,config_file_path = CONFIG_FILE_PATH,current_time_stamp:str= CURRENT_TIME_STAMP):
        
        try:
            self.config_info  = read_yaml_file(file_path=config_file_path)
            self.training_pipeline_config = self.get_training_pipeline_config()
            self.time_stamp = current_time_stamp
        except Exception as e:
            raise HousingException(e,sys) from e


    def get_data_ingestion_config(self):
        try:
            pass
        except Exception as e:
            raise HousingException(e,sys) from e   


    def get_training_pipeline_config(self) ->TrainingPipelineConfig:
        '''This function try to get the path of the artifact dir from the config yaml file'''
        try:
            training_pipeline_config = self.config_info[TRAINING_PIPELINE_CONFIG_KEY]
            artifact_dir = os.path.join(ROOT_DIR,
            training_pipeline_config[TRAINING_PIPELINE_NAME_KEY],
            training_pipeline_config[TRAINING_PIPELINE_ARTIFACT_DIR_KEY]
            )

            training_pipeline_config = TrainingPipelineConfig(artifact_dir=artifact_dir)
            return training_pipeline_config
        except Exception as e:
            raise HousingException(e,sys) from e