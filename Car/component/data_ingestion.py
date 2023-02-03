# code for data ingestion component

# 1. download housing data and save in the tgz folder
# 2. extract the data and save in the raw data folder
# 3. create data ingested folder
# 4. Split the data as train and test and save in train and test folder inside the data ingested folder



from Car.entity.config_entity import DataIngestionConfig
import sys,os
from Car.exception import CarException
from Car.logger import logging
from Car.entity.artifact_entity import DataIngestionArtifact
import tarfile
from zipfile import ZipFile
import numpy as np
from six.moves import urllib
import pandas as pd
from sklearn.model_selection import StratifiedShuffleSplit

class DataIngestion:

    def __init__(self,data_ingestion_config:DataIngestionConfig ):
        try:
            logging.info(f"{'>>'*20}Data Ingestion log started.{'<<'*20} ")
            self.data_ingestion_config = data_ingestion_config  # inilizing the data ingestion config path

        except Exception as e:
            raise CarException(e,sys)
    

    def download_Car_data(self,) -> str:  # download the data from url
        try:
            '''This function helps to download the data from the url
            '''
            #extraction remote url to download dataset
            download_url = self.data_ingestion_config.dataset_download_url

            #folder location to download file
            tgz_download_dir = self.data_ingestion_config.tgz_download_dir
            
            os.makedirs(tgz_download_dir,exist_ok=True)  # create the folder  for downloading dataset
            
            tgz_file_path = r'C:\Users\91822\Desktop\git_hub\Cardekho_pricing_project\dataset\car_dekho.zip'

            return tgz_file_path  
        except Exception as e:
            raise HousingException(e,sys) from e

    def extract_tgz_file(self,tgz_file_path:str):  # extracting the data 
        '''This function helps to extract the dataset '''
        try:
            raw_data_dir = self.data_ingestion_config.raw_data_dir  # get the directory of raw data folder

            if os.path.exists(raw_data_dir): # To check whether the folder is exist or not
                os.remove(raw_data_dir)   # remove the folder if it exist

            os.makedirs(raw_data_dir,exist_ok=True)  # to create the folder raw data dir to save the dataset

            logging.info(f"Extracting tgz file: [{tgz_file_path}] into dir: [{raw_data_dir}]")
            with ZipFile(tgz_file_path,'r') as Car_tgz_file_obj:
                Car_tgz_file_obj.extractall(path=raw_data_dir) # extract the raw data dir
            logging.info(f"Extraction completed")

        except Exception as e:
            raise CarException(e,sys) from e
    
    def split_data_as_train_test(self) -> DataIngestionArtifact:  # split the data into train and test dataset

        '''' This function helps to split the data into train and test data'''
        try:
            raw_data_dir = self.data_ingestion_config.raw_data_dir  # get the directory for data ingested

            file_name = os.listdir(raw_data_dir)[0]  # To get the file name from the list

            Car_file_path = os.path.join(raw_data_dir,file_name)   # directory for complete file path that need to split


            logging.info(f"Reading csv file: [{Car_file_path}]")
            Car_data_frame = pd.read_csv(Car_file_path)  # reading the extracted file

            Car_data_frame["selling_cat"] = pd.cut(
                Car_data_frame["selling_price"],
                bins=[0.0, 1.5, 3.0, 4.5, 6.0, np.inf],
                labels=[1,2,3,4,5]
            )  # distribution of the median income
            

            logging.info(f"Splitting data into train and test")
            strat_train_set = None # creating the dataset for train 
            strat_test_set = None # creating the dataset for test

            split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=121)  # spliting the dataset

            for train_index,test_index in split.split(Car_data_frame, Car_data_frame["selling_cat"]): # ration that split happens will always have same proportion
                strat_train_set = Car_data_frame.loc[train_index].drop(["selling_cat"],axis=1)  # extract the row wise data using values
                strat_test_set = Car_data_frame.loc[test_index].drop(["selling_cat"],axis=1)  # extract the row wise data using values
  
            train_file_path = os.path.join(self.data_ingestion_config.ingested_train_dir,
                                            file_name)  # creating the directory for the train data

            test_file_path = os.path.join(self.data_ingestion_config.ingested_test_dir,
                                        file_name)   # creating the directory for the test data
            
            if strat_train_set is not None:
                os.makedirs(self.data_ingestion_config.ingested_train_dir,exist_ok=True)
                logging.info(f"Exporting training datset to file: [{train_file_path}]")
                strat_train_set.to_csv(train_file_path,index=False)  # to store the data in the train directory

            if strat_test_set is not None:
                os.makedirs(self.data_ingestion_config.ingested_test_dir, exist_ok= True)
                logging.info(f"Exporting test dataset to file: [{test_file_path}]")
                strat_test_set.to_csv(test_file_path,index=False)  # to store the data in the test directory
            

            data_ingestion_artifact = DataIngestionArtifact(train_file_path=train_file_path,
                                test_file_path=test_file_path,
                                is_ingested=True,
                                message=f"Data ingestion completed successfully."
                                )
            logging.info(f"Data Ingestion artifact:[{data_ingestion_artifact}]")
            return data_ingestion_artifact

        except Exception as e:
            raise CarException(e,sys) from e

    def initiate_data_ingestion(self)-> DataIngestionArtifact:  # to initiate the data ingestion component and produces the data ingestion aritifact
        '''This function will return the data ingestion artifact path'''
        try:
            tgz_file_path =  self.download_Car_data()  # download the file
            self.extract_tgz_file(tgz_file_path=tgz_file_path) # extract the file
            return self.split_data_as_train_test() # split the file as train and test
        except Exception as e:
            raise CarException(e,sys) from e
    


    def __del__(self):
        logging.info(f"{'>>'*20}Data Ingestion log completed.{'<<'*20} \n\n")


    def __del__(self):
        logging.info(f"{'>>'*20}Data Ingestion log completed.{'<<'*20} \n\n")