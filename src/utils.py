import os, sys

import pandas as pd
import numpy as np
import pickle

from src.logger import logging
from src.exception import CustomException


def save_obj(obj, file_path):
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, "wb") as file:
            pickle.dump(obj, file)
    
    except Exception as e:
        raise CustomException (e,sys)


def load_obj(file_path):
    try:
        with open(file_path, "rb") as file:
            return pickle.load(file)
    except Exception as e:
        raise CustomException (e,sys)

        