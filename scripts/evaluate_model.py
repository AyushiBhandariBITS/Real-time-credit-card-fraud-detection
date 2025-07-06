from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def evaluate_model(y_true, y_pred, y_prob, model_name):
    print(f"\nEvaluation Report for {model_name}:")
    print(classification_report(y_true, y_pred))
    if y_prob is not None:
        auc = roc_auc_score(y_true, y_prob)
        print(f"ROC AUC Score: {auc:.4f}")
    else:
        print("ROC AUC Score: Not applicable (no probability output)")
    cm = confusion_matrix(y_true, y_pred)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title(f"Confusion Matrix - {model_name}")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.show()
    return
