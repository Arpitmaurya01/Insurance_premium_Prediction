import pymongo
from src.insurance.constant import DATABASE_NAME,COLLECTION_NAME
from src.insurance.logger import logging
from src.insurance.exception import CustomException
from src.insurance.constant import MONGODB_URL_KEY
import os,sys


class MongoDBClient:
    client = None
    def __init__(self,database_name=DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                #mongo_db_url = os.getenv(MONGODB_URL_KEY)
                logging.info("Connecting to mongodb client...")
                MongoDBClient.client = pymongo.MongoClient(host="localhost",port=27017)
            
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
            logging.info(f"Connected to database:'{database_name}")
        
        except Exception as e:
            raise CustomException(e,sys)
        