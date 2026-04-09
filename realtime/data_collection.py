import time
import psutil
import numpy as np
from collections import deque

prev_net = psutil.net_io_counters().bytes_sent

#collecting real time data
def get_live_data():
    global prev_net
    
    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent
    
    curr_net = psutil.net_io_counters().bytes_sent
    network = (curr_net - prev_net) / (1024 * 1024)  # MB
    network = np.log1
    prev_net = curr_net
    
    return {
        "cpu_percent": psutil.cpu_percent(),
        "ram_percent": psutil.virtual_memory().percent,
        "net_bytes_per_sec": network
    }
