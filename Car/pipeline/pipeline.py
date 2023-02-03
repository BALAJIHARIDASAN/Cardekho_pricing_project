from Car.config.configuration import *
from Car.logger import logging
from Car.exception import CarException
from Car.component.data_ingestion import *
from Car.entity.artifact_entity import *
from Car.entity.config_entity import *
import sys,os


class Pipeline:

    def __init__(self,config:Configuration= Configuration()):
        try:
            self.config  = config

        except Exception as e:
            raise CarException from e

    def start_data_ingestion(self):
        try:
            data_ingestion = DataIngestion(data_ingestion_config=self.config.get_data_ingestion_config())
            data_ingestion.initiate_data_ingestion()

        except Exception as e:
            raise CarException(e,sys) from  e


    def run_pipeline(self):
        try:
            data_ingestion_artifact =  self.start_data_ingestion()
        except Exception as e:
            raise CarException(e,sys) from e