import os, sys
import pandas as pd
import numpy as np

from src.exception import CustomException
from src.logger import logging
from src.utils import save_obj

from imblearn.over_sampling import SMOTE
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from dataclasses import dataclass 

@dataclass
class DataTransformationConfig:
    preprocessor_path = os.path.join("artifacts", "preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transform(self):
        try:
            preprocessor = Pipeline(steps=[
                ("scaler", StandardScaler())
                ]
            )

            return preprocessor
        except Exception as e:
            logging.error(f"Error in get_data_transformer: {e}")
            raise CustomException(e,sys)
        
    def initiate_data_transformation(self, train_set_path, test_set_path):
        try:
            logging.info("Loading the data for Preprocessing")
            train_df = pd.read_csv(train_set_path)
            test_df = pd.read_csv(test_set_path)

            target_col = "Default"

            # Seprate the target col from the data
            x_train_df = train_df.drop(target_col, axis=1)
            y_train_df = train_df[target_col]

            x_test_df = test_df.drop(target_col, axis=1)
            y_test_df = test_df[target_col]

            # Applying SMOTE to the training data
            smote = SMOTE(random_state=42)
            x_train_resampled, y_train_resampled = smote.fit_resample(x_train_df, y_train_df)
            logging.info("SMOTE applied to the training data")

            preprocessor = self.get_data_transform()
            
            logging.info("Appling preprocessing")
            x_train_scaled_df = preprocessor.fit_transform(x_train_resampled)
            x_test_scaled_df = preprocessor.transform(x_test_df)

            # Combine scaled features and target into arrays
            train_arr = np.c_[x_train_scaled_df, y_train_resampled]
            test_arr = np.c_[x_test_scaled_df, y_test_df]

            logging.info("Saving the preprocessor object")
            save_obj(obj = preprocessor, file_path = self.data_transformation_config.preprocessor_path)
            
            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_path
            )
        except Exception as e:
            raise CustomException(e, sys)