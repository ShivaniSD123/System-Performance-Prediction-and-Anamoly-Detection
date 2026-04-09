import time

last_alert_time = 0

def alert(score):
    global last_alert_time
    
    if time.time() - last_alert_time > 10:
        print(f"ALERT! Anomaly detected | Score={score:.2f}")
        last_alert_time = time.time()