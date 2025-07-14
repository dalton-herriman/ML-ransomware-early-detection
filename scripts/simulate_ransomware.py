# scripts/simulate_ransomware.py

import pandas as pd
import numpy as np
import os

OUTPUT_PATH = "data/ransomware_dataset.csv"
NUM_SAMPLES = 1000
RANSOMWARE_RATIO = 0.4  # 40% ransomware, 60% benign

def generate_samples(n, label):
    if label == "benign":
        entropy = np.random.normal(loc=5.5, scale=0.5, size=n)
        rename_rate = np.random.poisson(3, n)
        cpu = np.random.normal(30, 10, n)
        io_write = np.random.normal(200, 50, n)
    else:
        entropy = np.random.normal(loc=7.8, scale=0.3, size=n)
        rename_rate = np.random.poisson(60, n)
        cpu = np.random.normal(90, 5, n)
        io_write = np.random.normal(1200, 200, n)

    return pd.DataFrame({
        "entropy": np.clip(entropy, 0, 8),
        "file_rename_rate": np.clip(rename_rate, 0, None),
        "cpu_usage": np.clip(cpu, 0, 100),
        "io_write_speed": np.clip(io_write, 0, None),
        "label": [label] * n
    })

def generate_dataset():
    print("[+] Generating synthetic ransomware dataset...")
    n_ransom = int(NUM_SAMPLES * RANSOMWARE_RATIO)
    n_benign = NUM_SAMPLES - n_ransom

    df_benign = generate_samples(n_benign, "benign")
    df_ransom = generate_samples(n_ransom, "ransomware")

    df = pd.concat([df_benign, df_ransom], ignore_index=True)
    df = df.sample(frac=1).reset_index(drop=True)  # Shuffle

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    df.to_csv(OUTPUT_PATH, index=False)
    print(f"[+] Saved dataset to {OUTPUT_PATH} ({len(df)} rows)")

if __name__ == "__main__":
    generate_dataset()
