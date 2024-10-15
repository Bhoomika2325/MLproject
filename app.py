from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
from src.mlproject.components.data_ingestion import DataIngestion
from src.mlproject.components.data_ingestion import DataIngestionConfig
import sys
import os
#sys.path.append(os.path.abspath('src.mlproject.components'))
#from data_ingestion import DataIngestion

if __name__=="__main__":
    logging.info("the execution has started")


    try:
        ##print('start')
        #data_ingestion_config=DataIngestionConfig()
        data_ingestion=DataIngestion()
        data_ingestion.initiate_data_ingestion()
        #print('data ingestion start')
        
    except Exception as e:
        logging.info("Custom exception")
        raise CustomException(e,sys)

