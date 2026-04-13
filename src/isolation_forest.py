# train_isolation_forest.py
import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
import joblib

data = pd.read_csv("../data/train_data.csv")    
# Only use the 3 core metrics for anomaly detection
X = data[["cpu_percent", "ram_percent", "net_bytes_per_sec"]]

iso_forest = IsolationForest(
    n_estimators=100,
    contamination=0.05,  # assume 5% of data is anomalous
    random_state=42
)

iso_forest.fit(X)
joblib.dump(iso_forest, "../data/isolation_forest.pkl")
print("Isolation Forest trained and saved!")