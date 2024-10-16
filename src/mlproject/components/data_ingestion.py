# Mysql--->read in local-->train test split-->dataset

import os
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import pandas as pd
from src.mlproject.utils import read_sql_data
from sklearn.model_selection import train_test_split

from dataclasses import dataclass
#what is data class

@dataclass
class DataIngestionConfig:
    train_data_path:str=os.path.join('artifacts','train.csv')
    test_data_path:str=os.path.join('artifacts','test.csv')
    raw_data_path:str=os.path.join('artifacts','raw.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            ##reading the data from mysql
            print('data ingestion is working')
            df=read_sql_data()
            logging.info("Reading Completed from mysql database")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=100)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("data ingestion is completed")

            print('data ingestion completed')

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        

        except Exception as e:
            print('data ingestion failed')
            raise CustomException(e,sys)

