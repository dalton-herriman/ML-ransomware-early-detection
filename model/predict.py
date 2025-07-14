# model/predict.py

import joblib
import numpy as np
import os

MODEL_PATH = "model/ransomware_model.joblib"

# Load model once at import
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model not found at {MODEL_PATH}. Please train it first.")
    
model = joblib.load(MODEL_PATH)

def predict_ransomware(feature_vector: dict) -> str:
    """
    Predicts whether the input is benign or ransomware.
    
    Parameters:
    - feature_vector (dict): Dictionary with keys:
        'entropy', 'file_rename_rate', 'cpu_usage', 'io_write_speed'
        
    Returns:
    - str: 'benign' or 'ransomware'
    """
    # Order matters!
    ordered_features = [
        feature_vector["entropy"],
        feature_vector["file_rename_rate"],
        feature_vector["cpu_usage"],
        feature_vector["io_write_speed"]
    ]

    prediction = model.predict([ordered_features])[0]
    return prediction
