import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import MinMaxScaler
import joblib

data = pd.read_csv("../data/train_data.csv")

X = data[["cpu_percent", "ram_percent", "net_bytes_per_sec"]]

# ─────────────────────────────────────────
# Filter to ONLY normal/stable readings
# Remove obvious high usage periods
# ─────────────────────────────────────────

iso_forest = IsolationForest(
    n_estimators=200,
    contamination=0.02,  # very low — normal data has almost no anomalies
    random_state=42
)
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

iso_forest.fit(X_scaled)

joblib.dump(scaler, "../data/iso_scaler.pkl")
joblib.dump(iso_forest, "../data/isolation_forest.pkl")
