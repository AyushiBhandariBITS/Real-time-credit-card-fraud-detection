import pandas as pd
from datetime import datetime

def generate_report(metrics_dict):
    df = pd.DataFrame([metrics_dict])
    date_str = datetime.today().strftime('%Y-%m-%d')
    df.to_csv(f'reports/model_eval_{date_str}.csv', index=False)
    print(f"Report saved to reports/model_eval_{date_str}.csv")
    return