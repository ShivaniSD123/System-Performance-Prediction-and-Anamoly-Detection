import joblib
import numpy as np
import pandas as pd

model         = joblib.load("../data/model.pkl")
iso_forest    = joblib.load("../data/isolation_forest.pkl")
std_residuals = joblib.load("../data/std_residuals.pkl")

def monitor(input_data, actual_data):
    # RF predicts cpu and ram
    pred = model.predict(input_data)
    
    actual_df = pd.DataFrame(
        actual_data, 
        columns=["cpu_percent", "ram_percent", "net_bytes_per_sec"]
    )
    # Isolation Forest checks all 3 metrics for spikes
    anomaly_label = iso_forest.predict(actual_data)   # -1 = anomaly, 1 = normal
    anomaly_score = iso_forest.decision_function(actual_data)  # lower = more anomalous
    
    is_anomaly = anomaly_label[0] == -1
    score = float(-anomaly_score[0])  # flip sign so higher = more anomalous
    
    return is_anomaly, score, pred
