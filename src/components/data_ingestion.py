import sys
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass 
from src.logger import logging
from src.exception import CustomException

@dataclass
class DataIngestionConfig:
    raw_data_path: str = os.path.join("artifacts", "raw.csv")
    train_data_path: str = os.path.join("artifacts", "train.csv")
    test_data_path: str = os.path.join("artifacts", "test.csv")

class DataIngestion:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Data Ingestion initialized")

        try:
            # Read data from the URL
            df = pd.read_csv("Notebooks\credit_card_clients.csv")
            
            # Save raw data
            os.makedirs(os.path.dirname(self.data_ingestion_config.raw_data_path), exist_ok=True)
            df.to_csv(self.data_ingestion_config.raw_data_path, index=False)

            # Rename column for clarity
            df.drop("ID", axis=1, inplace=True)
            df.rename(columns={"default.payment.next.month": "Default"}, inplace=True)

            # Replace values for EDUCATION and MARRIAGE columns
            df['EDUCATION'].replace({5: 4, 6: 4, 0:4}, inplace=True)
            df['MARRIAGE'].replace({0: 3}, inplace=True)

            # Split the data into train and test sets
            train_set, test_set = train_test_split(df, test_size=0.20, random_state=42)

            # Save train and test data
            os.makedirs(os.path.dirname(self.data_ingestion_config.train_data_path), exist_ok=True)
            train_set.to_csv(self.data_ingestion_config.train_data_path, index=False)

            os.makedirs(os.path.dirname(self.data_ingestion_config.test_data_path), exist_ok=True)
            test_set.to_csv(self.data_ingestion_config.test_data_path, index=False)

            logging.info("Data Ingestion finished successfully")

            return (
                self.data_ingestion_config.train_data_path,
                self.data_ingestion_config.test_data_path
            )
        
        except Exception as e:
            logging.error(f"Error in data ingestion: {e}")
            raise CustomException(e, sys)
