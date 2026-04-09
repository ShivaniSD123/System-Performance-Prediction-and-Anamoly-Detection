import time
from collections import deque
from datetime import datetime
import numpy as np
#buffer for the lag feature + rolling feature
WINDOW_SIZE = 5

cpu_buffer = deque(maxlen=WINDOW_SIZE)
ram_buffer = deque(maxlen=WINDOW_SIZE)
net_buffer = deque(maxlen=WINDOW_SIZE)

#feature engennering
def build_features(data):
    cpu = data["cpu_percent"]
    ram = data["ram_percent"]
    net = data["net_bytes_per_sec"]
    
    # Update buffers
    cpu_buffer.append(cpu)
    ram_buffer.append(ram)
    net_buffer.append(net)
    
    # Wait for buffer to fill
    if len(cpu_buffer) < WINDOW_SIZE:
        return None
    
    features = {}
    
    # Current values
    features["cpu_percent"] = cpu
    features["ram_percent"] = ram
    features['net_bytes_per_sec'] = np.log1p(net)
    
    # Rolling means
    features["cpu_roll_mean"] = np.mean(cpu_buffer)
    features["ram_roll_mean"] = np.mean(ram_buffer)
    features["net_roll_mean"] = np.mean(net_buffer)
    
    # Change features
    features["cpu_change"] = cpu - cpu_buffer[-2]
    features["ram_change"] = ram - ram_buffer[-2]
    features["net_change"] = net - net_buffer[-2]
    features["net_change"] = np.sign(features["net_change"]) * np.log1p(np.abs(features["net_change"]))
    
    # Time features
    now = datetime.now()
    features["hour"] = now.hour
    features["minute"] = now.minute

    # Lag features
    features["cpu_lag1"] = cpu_buffer[-2]
    features["ram_lag1"] = ram_buffer[-2]
    features["net_lag1"] = net_buffer[-2]
    
    return features