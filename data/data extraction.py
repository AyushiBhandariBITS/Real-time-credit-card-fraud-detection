import pandas as pd
import numpy as np
from faker import Faker
import random

fake = Faker()

# Set seed for reproducibility
np.random.seed(42)
random.seed(42)

# Simulate 10,000 transactions
n_samples = 10000
fraud_ratio = 0.015  # 1.5% fraud
n_fraud = int(n_samples * fraud_ratio)
n_legit = n_samples - n_fraud

# Helper function to randomly introduce fraud conditions
def generate_transaction(is_fraud):
    user_id = fake.uuid4()
    country = fake.country_code()
    device = random.choice(['iOS', 'Android', 'Windows', 'MacOS', 'Linux'])
    browser = random.choice(['Chrome', 'Safari', 'Firefox', 'Edge'])
    merchant_id = fake.uuid4()
    amount = round(random.uniform(1, 3000), 2)

    txn_hour = random.randint(0, 23)
    is_night = 1 if txn_hour < 6 or txn_hour > 22 else 0
    channel = random.choice(['Online', 'POS', 'ATM'])

    # Fraud logic
    if is_fraud:
        country = random.choice(['RU', 'NG', 'CN', 'PK'])  # known high-risk countries
        device = random.choice(['Windows', 'Linux'])       # less common for mobile txns
        browser = 'Unknown'
        amount *= random.uniform(1.5, 3)                   # inflated amount
        is_night = 1
        channel = 'Online'

    return {
        'user_id': user_id,
        'country': country,
        'device': device,
        'browser': browser,
        'merchant_id': merchant_id,
        'amount': round(amount, 2),
        'txn_hour': txn_hour,
        'is_night': is_night,
        'channel': channel,
        'is_fraud': int(is_fraud)
    }

# Generate data
transactions = [generate_transaction(False) for _ in range(n_legit)] + \
               [generate_transaction(True) for _ in range(n_fraud)]

# Shuffle and create DataFrame
df_simulated = pd.DataFrame(transactions)
df_simulated = df_simulated.sample(frac=1).reset_index(drop=True)
df_simulated.head()
# Save to CSV
df_simulated.to_csv('data/simulated_transactions.csv', index=False)