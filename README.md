# ML-ransomware-early-detection
---
## Goals
- Detect early indicators of ransomware activity (file encryption, process behavior, system anomalies)
- Trigger alerts or mitigation before significant damage occurs
- Must run efficiently and reliably on endpoints or within a network

This design leverages a Random Forest Classifier, a solid baseline for ransomware detection. We are using synthetic training data generated from a script in the project. Once the cutover to real data occurs, preprocessing will need to be added.
---

## Architecture Overview
```plaintext
+---------------------------+
| Data Collection           |
|  - File I/O stats         |
|  - Process behavior       |
|  - Registry access (Win)  |
|  - Network connections    |
+------------+--------------+
             |
             v
+------------+--------------+
| Feature Extraction         |
|  - Entropy change          |
|  - File rename patterns    |
|  - Unusual process spikes  |
|  - Access to shadow copies |
+------------+--------------+
             |
             v
+------------+--------------+ 
| ML Model (Classifier)      |
|  - Trained to label        |
|    "benign" or "ransomware"|
+------------+--------------+
             |
             v
+------------+--------------+
| Response Engine            |
|  - Alert/log               |
|  - Kill process            |
|  - Isolate host (opt)      |
+---------------------------+
```

---

## Key Components

### Data Collection Module
### Feature Engineering
### Model Training
### Real Time Inference
### Response Engine

---

## Datasource Sets
Use or simulate ransomware activity or use public datasets
- EMBER (Windows PE Malware)
- VirusShare
- CIC Ransomware Dataset

---

## Tech Stack
- Python
- Scikit-learn or XGBoost
- Watchdog, psutil, joblib
- Optional: **fastapi** for endpoint control
