import numpy as np
import data_collection
import feature_engineering
import data_processing
import monitor
import joblib
import alert
import time

scalar = joblib.load("../data/scaler.pkl")

anomaly_counter = 0
CONFIRM_COUNT = 3  # must spike 3 times in a row to alert
last_alert_time = 0
COOLDOWN = 60 #seconds between alerts
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
    is_anomaly, score, pred = monitor.monitor(input_data, actual_data)

    #Which metric is spiking 
    cpu = data["cpu_percent"]
    ram = data["ram_percent"]
    net = data["net_bytes_per_sec"]

    print(f"CPU: {cpu:.1f}% | RAM: {ram:.1f}% | NET: {net:.2f} | Score: {score:.3f}")

    if is_anomaly:
        anomaly_counter += 1
    else:
        anomaly_counter = 0

    if anomaly_counter >= CONFIRM_COUNT:
        if time.time() - last_alert_time > COOLDOWN:
            alert.alert(score, data)
            last_alert_time = time.time()
            anomaly_counter = 0

    time.sleep(1)
