import os, sys
from src.logger import logging
from src.exception import CustomException

from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

if __name__ == "__main__":
    # data ingestion initialization
    ingestion_obj = DataIngestion()
    train_path, test_path = ingestion_obj.initiate_data_ingestion()

    # data transformation initiated here 
    transformation_obj = DataTransformation()
    train_arr, test_arr, preprocessor_path = transformation_obj.initiate_data_transformation(train_path, test_path)

    # model training initialization here 
    trainer_obj = ModelTrainer()
    trainer_obj.initiate_model_trainer(train_arr, test_arr, preprocessor_path)