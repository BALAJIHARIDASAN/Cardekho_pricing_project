from housing.config.configuration import *
from housing.logger import logging
from housing.exception import HousingException
from housing.component.data_ingestion import *
from housing.entity.artifact_entity import *
from housing.entity.config_entity import *
import sys,os


class Pipeline:

    def __init__(self,config:Configuration= Configuration()):
        try:
            self.config  = config

        except Exception as e:
            raise HousingException from e

    def start_data_ingestion(self):
        try:
            data_ingestion = DataIngestion(data_ingestion_config=self.config.get_data_ingestion_config())
            data_ingestion.initiate_data_ingestion()

        except Exception as e:
            raise HousingException(e,sys) from  e


    def run_pipeline(self):
        try:
            data_ingestion_artifact =  self.start_data_ingestion()
        except Exception as e:
            raise HousingException(e,sys) from e