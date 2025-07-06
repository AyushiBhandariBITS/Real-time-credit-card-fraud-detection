import pandas as pd
import joblib
import time
import os
import numpy as np
from scripts.risk_score_engine import calculate_risk_score
from scripts.preprocess import preprocess
from scripts.validate_data import validate_data
MODEL_PATH = "models/xgboost_model.pkl"
STREAM_PATH = "data/test_transactions.csv"
ALERT_LOG_PATH = "streamlit_app/alerts.csv"

# Load model
model = joblib.load(MODEL_PATH)

# Categorical encoders (should match your preprocessing)
def encode_features(txn):
    txn = preprocess(pd.DataFrame([txn]))
    validate_data(txn)
    return txn


if not os.path.exists(STREAM_PATH):
    print("Waiting for stream to begin...")

while True:
    if os.path.exists(STREAM_PATH):
        txn_o = pd.read_csv(STREAM_PATH).iloc[0].to_dict()
        txn = encode_features(txn_o)
        

        features = pd.DataFrame([{
            'device_encoded': int(txn['device_encoded']),
            'browser_encoded': int(txn['browser_encoded']),
            'country_encoded': int(txn['country_encoded']),
            'channel_encoded': int(txn['channel_encoded']),
            'log_amount': float(txn['log_amount']),
            'amount': float(txn['amount']),
            'txn_hour': int(txn['txn_hour']),
            'is_night': int(txn['is_night'])
        }])


        prob = model.predict_proba(features)[0][1]
        risk = calculate_risk_score(prob, features.iloc[0]['amount'], features.iloc[0]['is_night'], txn_o['channel'])

        print(f"→ Scored txn: prob: {prob:.4f} | risk: {risk:.4f}")

        if risk > 0.85:
            print("🚨 Alert: Fraud suspected!")
            alert_row = txn.copy()
            alert_row['model_prob'] = prob
            alert_row['risk_score'] = risk

            if not os.path.exists(ALERT_LOG_PATH):
                pd.DataFrame([dict(alert_row)]).to_csv(ALERT_LOG_PATH, index=False)
            else:
                pd.DataFrame([dict(alert_row)]).to_csv(ALERT_LOG_PATH, mode='a', header=False, index=False)

    time.sleep(2)
