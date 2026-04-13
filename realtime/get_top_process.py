import psutil
import time

def get_top_processes():
    processes = []

    # First call (initialize)
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            proc.cpu_percent(interval=None)
        except:
            continue

    time.sleep(0.5)  # small delay to measure CPU

    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            processes.append(proc.info)
        except:
            continue

    top_cpu = sorted(processes, key=lambda x: x['cpu_percent'] or 0, reverse=True)[:3]
    top_ram = sorted(processes, key=lambda x: x['memory_percent'] or 0, reverse=True)[:3]

    return top_cpu, top_ram