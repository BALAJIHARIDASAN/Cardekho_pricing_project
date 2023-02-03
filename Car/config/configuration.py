
from Car.entity.config_entity import DataIngestionConfig,TrainingPipelineConfig
from Car.util.util import read_yaml_file
from Car.logger import logging
import sys,os
from Car.constant import *
from Car.exception import CarException


# If we call these function we will get the entity from the config_entity

class Configuration:

    def __init__(self,
        config_file_path:str =CONFIG_FILE_PATH,
        current_time_stamp:str = CURRENT_TIME_STAMP 
        ) -> None:
        try:
            self.config_info  = read_yaml_file(file_path=config_file_path) # this line will get the read data  from to the yaml file
            self.training_pipeline_config = self.get_training_pipeline_config()  # this will get the path of the training pipeline
            self.time_stamp = current_time_stamp   # current time stamp
        except Exception as e:
            raise CarException(e,sys) from e



# data ingestion configuration
    def get_data_ingestion_config(self) ->DataIngestionConfig:
        
        try:
            artifact_dir = self.training_pipeline_config.artifact_dir  # this wil get the path of the aritifact dir
            data_ingestion_artifact_dir=os.path.join(
                artifact_dir,
                DATA_INGESTION_ARTIFACT_DIR,
                self.time_stamp
            ) # this line will get the complete path of the yaml file
            data_ingestion_info = self.config_info[DATA_INGESTION_CONFIG_KEY]   # this will get the path of the yaml file
            
            dataset_download_url = data_ingestion_info[DATA_INGESTION_DOWNLOAD_URL_KEY]  # this will get the url from the yaml file

            tgz_download_dir = os.path.join(
                data_ingestion_artifact_dir,
                data_ingestion_info[DATA_INGESTION_TGZ_DOWNLOAD_DIR_KEY]
            ) # 'c:\\Users\\91822\\Desktop\\git_hub\\Machine-Learning-project-end-to-end\\housing\\artifact\\data_ingestion\\tgz_data'

            raw_data_dir = os.path.join(data_ingestion_artifact_dir,
            data_ingestion_info[DATA_INGESTION_RAW_DATA_DIR_KEY]
            )  # 'c:\\Users\\91822\\Desktop\\git_hub\\Machine-Learning-project-end-to-end\\housing\\artifact\\data_ingestion\\raw_data'

            ingested_data_dir = os.path.join(
                data_ingestion_artifact_dir,
                data_ingestion_info[DATA_INGESTION_INGESTED_DIR_NAME_KEY]
            ) # 'c:\\Users\\91822\\Desktop\\git_hub\\Machine-Learning-project-end-to-end\\housing\\artifact\\data_ingestion\\ingested_data'


            ingested_train_dir = os.path.join(
                ingested_data_dir,
                data_ingestion_info[DATA_INGESTION_TRAIN_DIR_KEY]
            )  # 'c:\\Users\\91822\\Desktop\\git_hub\\Machine-Learning-project-end-to-end\\housing\\artifact\\data_ingestion\\ingested_data\\train'


            ingested_test_dir =os.path.join(
                ingested_data_dir,
                data_ingestion_info[DATA_INGESTION_TEST_DIR_KEY]
            )   # 'c:\\Users\\91822\\Desktop\\git_hub\\Machine-Learning-project-end-to-end\\housing\\artifact\\data_ingestion\\ingested_data\\test'


            data_ingestion_config=DataIngestionConfig(
                dataset_download_url=dataset_download_url, 
                tgz_download_dir=tgz_download_dir, 
                raw_data_dir=raw_data_dir, 
                ingested_train_dir=ingested_train_dir, 
                ingested_test_dir=ingested_test_dir
            )
            logging.info(f"Data Ingestion config: {data_ingestion_config}")
            return data_ingestion_config
        except Exception as e:
            raise CarException(e,sys) from e


    def get_training_pipeline_config(self) :
        try:
            training_pipeline_config = self.config_info[TRAINING_PIPELINE_CONFIG_KEY]  # this line will get the path of the yaml file contains details about the pipline
            artifact_dir = os.path.join(ROOT_DIR,
            training_pipeline_config[TRAINING_PIPELINE_NAME_KEY],
            training_pipeline_config[TRAINING_PIPELINE_ARTIFACT_DIR_KEY]
            )  # this line will get the path of the aritifact in the config.yaml file

            training_pipeline_config = TrainingPipelineConfig(artifact_dir=artifact_dir) # this the function that return in the config_entity file that hepls to generate an object
            logging.info(f"Training pipleine config: {training_pipeline_config}")
            return training_pipeline_config 
        except Exception as e:
            raise CarException(e,sys) from e