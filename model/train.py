# model/train.py

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from joblib import dump
import os

# Paths
DATA_PATH = "data/ransomware_dataset.csv"
MODEL_PATH = "model/ransomware_model.joblib"

def load_data():
    print("[+] Loading dataset...")
    df = pd.read_csv(DATA_PATH)
    X = df.drop(columns=["label"])
    y = df["label"]
    return X, y

def train_model(X, y):
    print("[+] Splitting data...")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    print("[+] Training RandomForestClassifier...")
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)

    print("[+] Evaluating model...")
    y_pred = clf.predict(X_test)
    print(classification_report(y_test, y_pred))

    print(f"[+] Saving model to {MODEL_PATH}")
    os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
    dump(clf, MODEL_PATH)

if __name__ == "__main__":
    X, y = load_data()
    train_model(X, y)