import joblib
import pandas as pd
scaler = joblib.load("../data/scaler.pkl")
col = joblib.load("../data/column.pkl")
scale_columns = joblib.load("../data/scale_columns.pkl")
def preprocess(features):
    df = pd.DataFrame([features])
    df = df.drop(columns=["cpu_percent", "ram_percent", "net_bytes_per_sec"], errors="ignore")

    df_scaled = scaler.transform(df)
    
    df = df[col]
    df[scale_columns] = scaler.transform(df[scale_columns])
    return df
