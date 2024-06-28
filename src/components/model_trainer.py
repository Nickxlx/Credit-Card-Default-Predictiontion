import sys, os
from sklearn.metrics import accuracy_score

from src.logger import logging
from src.exception import CustomException
from src.utils import  save_obj, load_obj
from dataclasses import dataclass

@dataclass
class ModelTrainerConfig:
    model_path = os.path.join("artifacts", "finl_model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self, train_arr, test_arr, preprocessor_path):
        try:
            model_file_path = "models/best_model.pkl"
            model = load_obj(model_file_path)
            preprocessor = load_obj(preprocessor_path)

            logging.info("Splitting Train and Test data")
            x_train, y_train, x_test, y_test = (
                train_arr[:, :-1],
                train_arr[:, -1], 
                test_arr[:, :-1],
                test_arr[:, -1]
            )

            x_train_scaled = preprocessor.fit_transform(x_train)
            x_test_scaled = preprocessor.transform(x_test)

            model.fit(x_train_scaled, y_train)
            print ("Model Training is Sucsessfully Done! ")

            y_pred = model.predict(x_test_scaled)

            # Log the accuracy of the model
            accuracy = accuracy_score(y_test, y_pred)
            logging.info(f"Model Accuracy: {accuracy}")
    
            if y_pred[0] == 0:
                logging.info("Person is not Faulty")
            else:
                logging.info("Person is Faulty")
            
            save_obj(model, self.model_trainer_config.model_path)
            logging.info(f"Saving the model {self.model_trainer_config.model_path}")
            print(f"Saving the model {self.model_trainer_config.model_path}")

        except Exception as e:
            raise CustomException(e, sys)
