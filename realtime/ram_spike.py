# ram_spike.py
import time
arr = []

while True:
    arr.append("A" * 10_000_000)  # ~10MB each loop
    time.sleep(0.1)