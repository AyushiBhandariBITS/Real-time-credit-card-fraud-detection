import pandas as pd

def validate_data(df):
    report = {}
    report['missing_values'] = df.isnull().sum().sum()
    report['duplicate_rows'] = df.duplicated().sum()
    report['high_amount_txns'] = df[df['amount'] > 2000].shape[0]
    report['off_hours_txns'] = df[(df['txn_hour'] < 6) | (df['txn_hour'] > 22)].shape[0]
    
    print("Validation Report:")
    for k, v in report.items():
        print(f"{k}: {v}")
    
    return report