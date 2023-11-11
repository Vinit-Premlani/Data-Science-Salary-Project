from flask import Flask, jsonify, request
import json
from data import data_in
import numpy as np
import pickle

app = Flask(__name__)


def load_models():
    file_name = "models/model_file.pkl"
    with open(file_name, 'rb') as pickled:
        data = pickle.load(pickled)
        print(data)
        model = data['model']
    return model

@app.route('/get_data', methods=['GET'])
def get_data():
    data = {"input": data_in}
    print(data)
    return data

@app.route('/predict', methods=['GET'])
def predict():
    # stub input features
    URL = 'http://127.0.0.1:5000/get_data'
    headers = {"Content-Type": "application/json"}
    data = {"input": data_in}
    x = data['input']
    print(x)
    x_in = np.array(x).reshape(1,-1)
    # load model
    model = load_models()
    prediction = model.predict(x_in)[0]
    response = json.dumps({'response': prediction})
    return response
