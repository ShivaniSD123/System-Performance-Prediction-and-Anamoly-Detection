import streamlit as st
import json
import time
import pandas as pd
import json

st.set_page_config(page_title="System Monitor", layout="wide")

st.title("Real-Time Monitoring Dashboard")

cpu_placeholder = st.empty()
ram_placeholder = st.empty()
net_placeholder = st.empty()
status_placeholder = st.empty()
chart_placeholder = st.empty()

history = []

while True:
    try:
        with open("status.json", "r") as f:
            status = json.load(f)
    except:
        st.warning("Waiting for data...")
        time.sleep(1)
        continue

    cpu = status["cpu"]
    ram = status["ram"]
    net = status["net"]
    is_anomaly = status["is_anomaly"]
    score = status["score"]

    # Metrics
    cpu_placeholder.metric("CPU %", f"{cpu:.1f}")
    ram_placeholder.metric("RAM %", f"{ram:.1f}")
    net_placeholder.metric("NET", f"{net:.2f}")

    # Status
    if is_anomaly:
        status_placeholder.error(f" High | Score: {score:.3f}")
    else:
        status_placeholder.success("Normal")

    # Graph
    history.append({"cpu": cpu, "ram": ram, "net": net})
    df = pd.DataFrame(history[-50:])
    chart_placeholder.line_chart(df)

    time.sleep(1)