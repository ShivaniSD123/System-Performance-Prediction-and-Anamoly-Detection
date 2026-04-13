import joblib
import pandas as pd

scaler = joblib.load("../data/scaler.pkl")
expected_cols = joblib.load("../data/column.pkl")

FEATURES_TO_USE = ["ram_lag1", "cpu_lag1", "cpu_change", 
                   "ram_change", "cpu_roll_mean", "ram_roll_mean"]

def preprocess(features):
    df = pd.DataFrame([features])
    
    # Scale the 6 features
    df[FEATURES_TO_USE] = scaler.transform(df[FEATURES_TO_USE])
    
    # Reorder to exactly match training column order ← THIS IS THE FIX
    df = df[expected_cols]
    # In data_processing.py temporarily
    
    return df
