import pandas as pd
from scripts.preprocess import preprocess
from scripts.validate_data import validate_data
from scripts.train_model import train_models
from scripts.evaluate_model import evaluate_model
from scripts.generate_report import generate_report
from sklearn.metrics import precision_score, recall_score, roc_auc_score,classification_report
from sklearn.model_selection import train_test_split

# Load & preprocess
print("Loading dataset...")
df = pd.read_csv('data/simulated_transactions.csv')
df = preprocess(df)
print(df.columns)
# Validate data
print("Running data validation...")
validate_data(df)

# Train models
print("Training models...")
xgb, iso, lgbm = train_models(df)


# Evaluate XGBoost
print("Evaluating XGBoost model...")
X = df.drop(columns=['is_fraud'])
y = df['is_fraud']
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.2)
y_pred_xgb = xgb.predict(X_test)
y_prob_xgb = xgb.predict_proba(X_test)[:, 1]
evaluate_model(y_test, y_pred_xgb, y_prob_xgb, model_name="XGBoost")
metrics = {
    'model': 'XGBoost',
    'precision': precision_score(y_test, y_pred_xgb),
    'recall': recall_score(y_test, y_pred_xgb),
    'auc': roc_auc_score(y_test, y_prob_xgb),
    'timestamp': pd.Timestamp.now()
}
print("Generating report for XGBoost...")
print(metrics)
generate_report(metrics)

# Evaluate LightGBM
print("Evaluating LightGBM model...")
y_pred_lgbm = lgbm.predict(X_test)
y_prob_lgbm = lgbm.predict_proba(X_test)[:, 1]
evaluate_model(y_test, y_pred_lgbm, y_prob_lgbm, model_name="LightGBM")
metrics = {
    'model': 'LightBGM',
    'precision': precision_score(y_test, y_pred_lgbm),
    'recall': recall_score(y_test, y_pred_lgbm),
    'auc': roc_auc_score(y_test, y_prob_lgbm),
    'timestamp': pd.Timestamp.now()
}
print("Generating report for LightGBM...")
generate_report(metrics)
print(metrics)

# Evaluate Isolation Forest
print("Evaluating Isolation Forest model...")
y_pred_iso = iso.predict(X_test)
y_pred_iso = [1 if x == -1 else 0 for x in y_pred_iso]  # Convert -1 to 1 for anomalies
evaluate_model(y_test, y_pred_iso, None, model_name="Isolation Forest") 
print("Evaluating Isolation Forest (Unsupervised)...")
y_pred_iso = iso.predict(X_test)
# Convert outputs: 1 (inlier) → 0, -1 (outlier) → 1 (fraud)
y_pred_iso = [0 if p == 1 else 1 for p in y_pred_iso]
report_dict= classification_report(y_test, y_pred_iso , output_dict=True)
print("Generating report for Isolation Forest...")
metrics = {
    'model': 'Isolation Forest',
    'precision': report_dict['1']['precision'],
    'recall': report_dict['1']['recall'],
    'auc': None,  # Not applicable, no probability
    'timestamp': pd.Timestamp.now()
}
generate_report(metrics)
print(metrics)


print("Pipeline complete.")
