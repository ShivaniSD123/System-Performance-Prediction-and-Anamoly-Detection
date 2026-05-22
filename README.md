<h1 align="center">🚀 System Performance Prediction & Anomaly Detection</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange?style=for-the-badge&logo=scikitlearn">
  <img src="https://img.shields.io/badge/Random%20Forest-Prediction-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/Isolation%20Forest-Anomaly%20Detection-red?style=for-the-badge">
  <img src="https://img.shields.io/badge/Streamlit-Dashboard-ff4b4b?style=for-the-badge&logo=streamlit">
</p>

<p align="center">
  Real-time machine learning system for predicting system performance and detecting anomalies using CPU, RAM, and network telemetry.
</p>

---

## 📌 Project Overview

This project is a **real-time system monitoring and anomaly detection platform** that predicts CPU and RAM utilization while detecting abnormal system behavior using machine learning.

Inspired by enterprise monitoring platforms like **Datadog** and **AWS CloudWatch**, the system provides:

- 📈 Real-time performance prediction
- 🚨 Anomaly detection with alerts
- 🔍 Process-level root cause attribution
- 📊 Interactive monitoring dashboard

---

## ✨ Key Features

✅ Real-time CPU, RAM, and network monitoring  
✅ Random Forest-based CPU & RAM prediction  
✅ Isolation Forest anomaly detection  
✅ Hybrid anomaly detection (ML + threshold logic)  
✅ Process-level PID attribution  
✅ Desktop notifications for anomalies  
✅ Streamlit dashboard for live monitoring  
✅ JSON anomaly event logging  

---

## 🏗️ System Architecture

```text
psutil Data Collection
        ↓
Feature Engineering
        ↓
Data Preprocessing + Scaling
        ↓
 ┌──────────────────────┬────────────────────────┐
 │                      │                        │
 │ Random Forest Model  │ Isolation Forest Model │
 │ (Prediction)         │ (Anomaly Detection)    │
 │                      │                        │
 └──────────────────────┴────────────────────────┘
        ↓
Alert Engine + Process Attribution
        ↓
Streamlit Dashboard
```

---

## 🧠 Machine Learning Pipeline

### Prediction Models Evaluated

| Model | R² Score | RMSE | Status |
|------|---------|------|--------|
| Linear Regression | 0.8876 | 0.1090 | Baseline |
| Random Forest | **0.9802** | **0.0179** | ✅ Selected |
| LSTM | 0.7410 | 0.0549 | Experimental |

### Why Random Forest?

Random Forest was selected because:

- High prediction accuracy
- Fast inference for real-time monitoring
- Handles non-linear behavior effectively
- Native support for multi-output regression

---

## 🌲 Anomaly Detection

Anomalies are detected using **Isolation Forest**, an unsupervised anomaly detection algorithm.

### Detection Strategy

- Isolation Forest detects unusual system behavior
- Rule-based thresholds detect obvious spikes
- 3-hit anomaly confirmation guard reduces false positives
- Cooldown logic prevents alert spam

### Types of anomalies detected

- CPU spikes
- RAM spikes
- Network spikes
- Combined abnormal behavior

---

## ⚙️ Feature Engineering

Temporal behavior was captured using engineered features:

```python
cpu_lag1
ram_lag1
cpu_roll_mean
ram_roll_mean
cpu_change
ram_change
```

### Impact

Feature engineering improved model performance significantly:

```text
Random Forest R²:
0.80 → 0.98
```

This demonstrates the importance of capturing temporal dependencies in system telemetry.

---

## 📊 Visualization

The project includes:

- Actual vs Predicted performance plots
- Residual analysis
- Real-time system metric visualization
- Streamlit dashboard monitoring

---

## 🛠️ Tech Stack

**Programming Language**
- Python

**Libraries & Tools**
- psutil
- pandas
- numpy
- scikit-learn
- TensorFlow / Keras
- Streamlit
- joblib
- plyer
- matplotlib

---

## 📂 Project Structure

```text
system-performance-monitor/
│
├── data/
│   ├── train_data.csv
│   ├── test_data.csv
│   ├── scaler.pkl
│   ├── model.pkl
│   ├── threshold.pkl
│   └── std_residuals.pkl
│
├── realtime/
│   ├── main.py
│   ├── alert.py
│   ├── monitor.py
│   ├── data_collection.py
│   ├── feature_engineering.py
│   ├── data_processing.py
│   └── get_top_process.py
│
├── dashboard/
│   └── app.py
│
├── training/
│   ├── random_forest.py
│   ├── lstm.py
│   └── linear_regression.py
│
└── README.md
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/system-performance-monitor.git
cd system-performance-monitor
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

Start real-time monitoring:

```bash
python realtime/main.py
```

Launch Streamlit dashboard:

```bash
streamlit run dashboard/app.py
```

---

## 🔍 Research Inspiration

This project is inspired by research in:

- Isolation Forest for cloud anomaly detection
- Time-series anomaly detection using temporal context
- Temporal correlation modeling for anomaly detection

Key concepts adopted:

- Real-time anomaly detection
- Temporal feature engineering
- Explainable anomaly attribution

---

## 🔮 Future Improvements

Potential enhancements:

- Email / Slack alert integration
- Docker deployment
- Cloud-based distributed monitoring
- XGBoost-based prediction experiments
- Deep Isolation Forest
- Adaptive anomaly thresholds

---

## 💼 Why This Project Matters

Modern monitoring tools are often reactive and black-box.

This project demonstrates:

- proactive monitoring
- explainable anomaly detection
- lightweight local observability
- practical ML systems engineering

---

## 👩‍💻 Author

**Shivani Dwivedi**

Machine Learning | Systems Engineering | Real-Time Monitoring

---
