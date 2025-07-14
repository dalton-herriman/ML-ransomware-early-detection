# run_detector.py
# core entry point 

import time
from detectors.file_monitor import FileMonitor
from detectors.process_monitor import get_process_features
from features.extractor import extract_features
from model.predict import predict_ransomware
from response.responder import respond

# Initialize file system monitor (e.g., Watchdog observer)
monitor = FileMonitor(path="C:/", recursive=True)
monitor.start()

print("[+] Ransomware Detector started...")

try:
    while True:
        # 1. Get collected file event features
        file_features = monitor.get_recent_events()

        # 2. Get process stats
        process_features = get_process_features()

        # 3. Combine features into a single vector
        features = extract_features(file_features, process_features)

        # 4. Run inference
        prediction = predict_ransomware(features)

        # 5. If detected, respond
        if prediction == "ransomware":
            print("[!] ALERT: Ransomware activity detected!")
            respond(features)  # Kill proc, quarantine, alert

        time.sleep(2)

except KeyboardInterrupt:
    print("\n[!] Stopping monitor...")
    monitor.stop()