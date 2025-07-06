import pandas as pd
import numpy as np

def preprocess(df):
    df = df.copy()

    # Encode categorical features
    df['device_encoded'] = df['device'].astype('category').cat.codes
    df['browser_encoded'] = df['browser'].astype('category').cat.codes
    df['country_encoded'] = df['country'].astype('category').cat.codes
    df['channel_encoded'] = df['channel'].astype('category').cat.codes
    # Log-transform amount to reduce skew
    df['log_amount'] = np.log1p(df['amount'])

    # You may drop unused columns or keep them for interpretation
    df_model = df[[
        'device_encoded', 'browser_encoded', 'country_encoded',
        'channel_encoded', 'log_amount', 'amount', 'txn_hour','is_night',
        'is_fraud'  # target
    ]]

    return df_model

