# dashboard.py (for streamlit_app/)
import streamlit as st
import pandas as pd
import os
import time

STREAM_PATH = "streamlit_app/stream_txn.csv"
if not os.path.exists(STREAM_PATH):
    st.warning("Waiting for transaction stream to begin...")
    st.stop()
ALERT_LOG_PATH = "streamlit_app/alerts.csv"

st.set_page_config(page_title="Real-Time Fraud Monitor", layout="wide")
st.title("🛡️ Real-Time Fraud Detection Dashboard")

st.sidebar.header("Live Feed Controls")
refresh_rate = st.sidebar.slider("Refresh every N seconds", min_value=1, max_value=10, value=2)

placeholder = st.empty()

while True:
    with placeholder.container():
        st.subheader("Latest Transaction")
        if os.path.exists(STREAM_PATH):
            txn = pd.read_csv(STREAM_PATH)
            st.write(txn)

        st.subheader("Alerts Log")
        if os.path.exists(ALERT_LOG_PATH):
            alerts = pd.read_csv(ALERT_LOG_PATH)
            st.dataframe(alerts.sort_values("risk_score", ascending=False).head(10))
        else:
            st.info("No alerts yet.")

    time.sleep(refresh_rate)
    st.rerun()