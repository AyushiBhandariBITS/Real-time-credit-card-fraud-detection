import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import IsolationForest
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
import joblib

def train_models(df):
    X = df.drop(columns=['is_fraud'])
    y = df['is_fraud']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.2, random_state=42)

    # Supervised model
    xgb = XGBClassifier(scale_pos_weight=99, use_label_encoder=False, eval_metric='logloss')
    xgb.fit(X_train, y_train)
    joblib.dump(xgb, 'models/xgboost_model.pkl')

 # LightGBM
    lgbm = LGBMClassifier(scale_pos_weight=99)
    lgbm.fit(X_train, y_train)
    joblib.dump(lgbm, 'models/lgbm_model.pkl')

    # Unsupervised model
    iso = IsolationForest(n_estimators=100, contamination=0.001)
    iso.fit(X_train)
    joblib.dump(iso, 'models/isolation_forest.pkl')

    print("Models trained and saved.")
    return xgb, iso,lgbm
