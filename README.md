# Real-time-credit-card-fraud-detection pipeline

A complete machine learning pipeline for detecting credit card fraud, inspired by real-world fraud detection systems used in financial institutions and companies like Sherloq AI.

---

## 🚀 Project Features

- Supervised & Unsupervised fraud detection using:
  - ✅ XGBoost
  - ✅ LightGBM
  - ✅ Logistic Regression
  - ✅ Isolation Forest
- Real-world inspired dataset with:
  - User metadata (device, country, channel)
  - Transaction patterns (amount, time of day)
  - Behavioral indicators (off-hour flags, inflated amounts)
- Custom Risk Score Engine combining model probability with business rules
- Robust model evaluation with classification metrics and ROC AUC
- Risk reports auto-generated and saved
- Modular pipeline with scripts for preprocessing, training, evaluation, and scoring

---

## 📁 Directory Structure

```
creditcard-fraud-detection/
├── data/                        # Raw and simulated fraud datasets
│   └── realworld_fraud_simulated.csv
├── models/                     # Trained ML model files
├── reports/                    # Evaluation reports (per model, per run)
├── scripts/                    # Modular Python scripts
│   ├── preprocess.py
│   ├── validate_data.py
│   ├── train_model.py
│   ├── evaluate_model.py
│   ├── risk_score_engine.py
│   └── generate_report.py
├── dashboard.py       # streamlit         
├── inference.py
├── stream_stimlator.py
├── main.py                    # Driver file to execute full pipeline
└── README.md                   # Project documentation
```

---

## 🧪 Models Used

| Model              | Type           | Use Case                  |
|-------------------|----------------|---------------------------|
| XGBoost            | Supervised     | Main binary classifier    |
| LightGBM           | Supervised     | Faster alternative        |
| Isolation Forest   | Unsupervised   | Anomaly detection         |

---

## 📊 Risk Scoring Engine

The project includes a custom `calculate_risk_score()` function that uses:
- Model probability
- High transaction amount flag
- Night-time transaction flag
- Encoded channel (e.g. `Online`) flag

Resulting in a final `risk_score ∈ [0, 1]`, used for prioritizing fraud investigations.

---

## ⚙️ How to Run

### Step 1: Install Dependencies
```bash
pip install pandas numpy xgboost lightgbm scikit-learn matplotlib seaborn faker
```

### Step 2: Run Full Pipeline
```bash
python main.py
```

- This runs: preprocessing → validation → training → evaluation → risk scoring → reporting
- Reports saved in `/reports/` folder

### Step 3: (Optional) Run Single Inference
```python
from scripts.risk_score_engine import calculate_risk_score
risk = calculate_risk_score(model_prob=0.82, amount=2100, is_night=1, channel_encoded=1, online_code=1)
print(risk)
```

---

## 📈 Example Output

- Confusion Matrix
- Classification Report
- ROC AUC
- Top risky transactions with custom score

---

## ✅ What You’ll Learn / Showcase

- Fraud detection logic used in real ML systems
- Handling imbalanced classification problems
- Designing explainable + actionable scoring systems
- Model evaluation and drift tracking
- Scalable and modular pipeline engineering

---

## 📌 Future Additions (Planned or Optional)

- SHAP Explainability
- Real-time scoring via stream simulation
- Streamlit dashboard with alerts
- Drift monitoring & retraining trigger logic
- Integration with SQL/NoSQL databases

---

## 📬 Questions or Feedback?
Open an issue or contact me via GitHub.

---

> "In fraud detection, it's not about catching them all — it's about catching them before it's too late."
