import joblib
import pandas as pd
scaler = joblib.load("scaler.pkl")
def preprocess(features):
    df = pd.DataFrame([features])
    df_scaled = scaler.transform(df)
    
    return df_scaled
