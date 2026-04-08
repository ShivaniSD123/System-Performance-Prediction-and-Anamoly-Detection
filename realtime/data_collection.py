import time
import psutil
from collections import deque

prev_net = psutil.net_io_counters().bytes_sent

#buffer for the lag feature + rolling feature
WINDOW_SIZE = 5

cpu_buffer = deque(maxlen=WINDOW_SIZE)
memory_buffer = deque(maxlen=WINDOW_SIZE)
network_buffer = deque(maxlen=WINDOW_SIZE)

#collecting real time data
def get_live_data():
    global prev_net
    
    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent
    
    curr_net = psutil.net_io_counters().bytes_sent
    network = (curr_net - prev_net) / (1024 * 1024)  # MB
    prev_net = curr_net
    
    return {
        "cpu": cpu,
        "memory": memory,
        "network": network
    }

#buffer update
def update_buffers(data):
    cpu_buffer.append(data['cpu'])
    memory_buffer.append(data['memory'])
    network_buffer.append(data['network'])
