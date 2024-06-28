import sys

import pandas as pd
import numpy as np
from src.logger import logging
from src.exception import CustomException
from src.utils import load_obj

from flask import Flask, render_template, request, json

application = Flask(__name__)
app = application

# Load your pre-trained model and preprocessor
model_path = "artifacts/finl_model.pkl"
preprocessor_path = "artifacts/preprocessor.pkl"

model = load_obj(model_path)
preprocessor = load_obj(preprocessor_path)

@app.route('/')
def home():
    return render_template('index.html', prediction=None)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collect input data from form
        input_data = request.form['features']
        
        # Split the input string by commas and convert to float
        input_data = [float(i) for i in input_data.split(',')]
        
        # Ensure the correct number of features
        if len(input_data) != 23:
            return render_template('index.html', prediction="Error: Please enter exactly 23 feature values.")
        
        # Convert input data to numpy array and reshape
        input_data = np.array(input_data).reshape(1, -1)

        input_data_preprocessed = preprocessor.transform(input_data)

        prediction = model.predict(input_data_preprocessed)

        # Interpret the prediction
        if prediction[0] == 0:
            result = "Person is not Faulty"
        else:
            result = "Person is Faulty"

        return render_template('index.html', prediction=result)
    except Exception as e:
        return render_template('index.html', prediction=f"Error: {str(e)}")


if __name__ == "__main__":
    app.run(host = "0.0.0.0", port=8080, debug= True )
