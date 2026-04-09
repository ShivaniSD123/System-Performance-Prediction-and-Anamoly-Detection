import numpy as np
import data_collection
import feature_engineering
import data_processing
import monitor
import joblib
import alert
import time

scalar = joblib.load("../data/scaler.pkl")
while True:
    data = data_collection.get_live_data()
    features = feature_engineering.build_features(data)
    if features is None:
        print("Collecting initial data...")
        time.sleep(1)
        continue
    input_data = data_processing.preprocess(features)
    actual_data=np.array([[
        data["cpu_percent"],
        data["ram_percent"],
        data["net_bytes_per_sec"]
    ]])
    actual_scaled = scalar.transform(actual_data)
    is_anomaly, score, pred = monitor.monitor(input_data, actual_scaled)
    print(f"Actual: {actual_scaled} | Pred: {pred} | Score: {score:.2f}")
    
    if is_anomaly:
        alert.alert(score)
    
    time.sleep(1)
