import streamlit as st
import time
import pandas as pd

import data_collection
import feature_engineering
import data_processing
import monitor

# Page config
st.set_page_config(page_title="System Monitor", layout="wide")

st.title("Real-Time System Monitoring Dashboard")

# Placeholders
cpu_placeholder = st.empty()
ram_placeholder = st.empty()
net_placeholder = st.empty()
status_placeholder = st.empty()
chart_placeholder = st.empty()

# Store history
history = []

while True:
    data = data_collection.get_live_data()
    features = feature_engineering.build_features(data)

    if features is None:
        st.warning("Collecting initial data...")
        time.sleep(1)
        continue

    input_data = data_processing.preprocess(features)

    actual_data = [[
        data["cpu_percent"],
        data["ram_percent"],
        data["net_bytes_per_sec"]
    ]]

    is_anomaly, score, _ = monitor.monitor(input_data, actual_data)

    cpu = data["cpu_percent"]
    ram = data["ram_percent"]
    net = data["net_bytes_per_sec"]

    # Update metrics
    cpu_placeholder.metric("CPU %", f"{cpu:.1f}")
    ram_placeholder.metric("RAM %", f"{ram:.1f}")
    net_placeholder.metric("NET", f"{net:.2f}")

    # Status
    if is_anomaly:
        status_placeholder.error(f"🚨 Anomaly Detected | Score: {score:.3f}")
    else:
        status_placeholder.success(" System Normal")

    # Store history
    history.append({
        "cpu": cpu,
        "ram": ram,
        "net": net
    })

    df = pd.DataFrame(history[-50:])

    # Plot
    chart_placeholder.line_chart(df)

    time.sleep(1)