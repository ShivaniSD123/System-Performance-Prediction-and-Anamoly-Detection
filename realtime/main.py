import numpy as np
import data_collection
import feature_engineering
import data_processing
import monitor
import joblib
import alert
import time
import get_top_process
import json

scalar = joblib.load("../data/scaler.pkl")

anomaly_counter = 0
CONFIRM_COUNT = 2  # must spike 3 times in a row to alert
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

    actual_data = np.array([[
        data["cpu_percent"],
        data["ram_percent"],
        data["net_bytes_per_sec"]
    ]])

    is_anomaly, score, pred = monitor.monitor(input_data, actual_data)

    # Extract metrics
    cpu = data["cpu_percent"]
    ram = data["ram_percent"]
    net = data["net_bytes_per_sec"]

    print(f"CPU: {cpu:.1f}% | RAM: {ram:.1f}% | NET: {net:.2f} | Score: {score:.3f}")

    # ADD THIS HERE (IMPORTANT)
    status = {
        "cpu": cpu,
        "ram": ram,
        "net": net,
        "is_anomaly": bool(is_anomaly),
        "score": score
    }

    with open("status.json", "w") as f:
        json.dump(status, f)

    # ------------------------------
    # anomaly logic (unchanged)
    # ------------------------------
    if is_anomaly:
        anomaly_counter += 1
    else:
        anomaly_counter = 0

    if anomaly_counter >= CONFIRM_COUNT:
        if time.time() - last_alert_time > COOLDOWN:

            top_process = get_top_process.get_top_processes()
            alert.alert(score, data, top_process)

            last_alert_time = time.time()
            anomaly_counter = 0

    time.sleep(1)