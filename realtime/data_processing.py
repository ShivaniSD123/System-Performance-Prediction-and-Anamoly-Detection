import joblib
import pandas as pd
scaler = joblib.load("../data/scaler.pkl")
col = joblib.load("../data/column.pkl")
def preprocess(features):
    df = pd.DataFrame([features])
    df_scaled = scaler.transform(df)
    df = df[col]
    
    return df
