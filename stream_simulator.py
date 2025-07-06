# stream_simulator.py
import time
import pandas as pd
import random
import os

DATA_PATH = "C:/Users/Ayushi/Desktop/credit card fraud/data/test_transactions.csv"
ALERT_LOG_PATH = "streamlit_app/alerts.csv"
STREAM_PATH = "streamlit_app/stream_txn.csv"

def stream_transactions(delay=2):
    df = pd.read_csv(DATA_PATH)

    while True:
        txn = df.sample(1).to_dict(orient='records')[0]
        # Save current transaction to CSV for streamlit to read
        pd.DataFrame([txn]).to_csv(STREAM_PATH, index=False)
        print(f"Streamed txn: {txn['user_id']} | Amount: {txn['amount']} | is_fraud: {txn['is_fraud']}")
        time.sleep(delay)

if __name__ == "__main__":
    if not os.path.exists("streamlit_app"):
        os.makedirs("streamlit_app")
    stream_transactions()