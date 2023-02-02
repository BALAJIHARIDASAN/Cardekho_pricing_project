# This folder consist of helping function 


from housing.Exception import HousingException
import yaml
import sys

def read_yaml_file(file_path:str)->dict:
    """
    Description : This function helps to read the yaml file in config folder 
    Input : File path for config folder
    output : dictionary of config.yaml file
    """
    try:
        with open(file_path, 'rb') as yaml_file:
            return yaml.safe_load(yaml_file)

    except Exception as e:
        raise HousingException(e,sys) from e