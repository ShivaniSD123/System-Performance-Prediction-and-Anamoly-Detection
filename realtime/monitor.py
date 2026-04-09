import joblib
import numpy as np

model= joblib.load("../data/model.pkl")
threshold = joblib.load("../data/threshold.pkl")

def monitor(input_data, actual_data):
    pred= model.predict(input_data)
    residual = np.abs(actual_data - pred)
    score = np.linalg.norm(residual)
    return score > threshold, score, pred
