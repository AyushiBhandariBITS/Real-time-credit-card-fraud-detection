import pandas as pd
import random
from faker import Faker

fake = Faker()
Faker.seed(42)
random.seed(42)

def generate_entry(is_fraud):
    # Make the high-risk/fraudulent transactions suspiciously designed
    if is_fraud:
        country = random.choice(['RU', 'NG', 'PK', 'CN'])
        device = random.choice(['Linux', 'Windows'])
        browser = random.choice(['Unknown', 'Opera'])
        channel = 'Online'
        amount = round(random.uniform(2000, 5000), 2)
        txn_hour = random.choice([0, 1, 2, 23])
        is_night = 1
    else:
        country = random.choice(['IN', 'US', 'AE', 'UK'])
        device = random.choice(['iOS', 'Android', 'MacOS'])
        browser = random.choice(['Chrome', 'Safari', 'Firefox'])
        channel = random.choice(['POS', 'ATM'])
        amount = round(random.uniform(50, 800), 2)
        txn_hour = random.randint(8, 20)
        is_night = 0 if 6 <= txn_hour <= 22 else 1

    return {
        "user_id": fake.uuid4(),
        "country": country,
        "device": device,
        "browser": browser,
        "merchant_id": fake.uuid4(),
        "amount": amount,
        "txn_hour": txn_hour,
        "is_night": is_night,
        "channel": channel,
        "is_fraud": int(is_fraud)
    }

# Create 10 high-risk (fraud) and 10 safe (legit) transactions
frauds = [generate_entry(True) for _ in range(10)]
legits = [generate_entry(False) for _ in range(10)]

df_demo = pd.DataFrame(frauds + legits).sample(frac=1, random_state=42).reset_index(drop=True)
csv_path = "data/test_transactions.csv"

df_demo.to_csv(csv_path, index=False)
csv_path
