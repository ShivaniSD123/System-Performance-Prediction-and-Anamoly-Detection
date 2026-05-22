
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 1100px;
            margin: auto;
            padding: 20px;
            line-height: 1.7;
            background-color: #f9fafb;
            color: #1f2937;
        }

        h1, h2, h3 {
            color: #111827;
        }

        h1 {
            text-align: center;
            border-bottom: 3px solid #2563eb;
            padding-bottom: 10px;
        }

        .badge {
            display: inline-block;
            padding: 6px 12px;
            margin: 4px;
            background-color: #2563eb;
            color: white;
            border-radius: 20px;
            font-size: 14px;
        }

        .section {
            background: white;
            padding: 20px;
            margin-top: 20px;
            border-radius: 12px;
            box-shadow: 0px 2px 8px rgba(0,0,0,0.08);
        }

        code {
            background: #eef2ff;
            padding: 2px 6px;
            border-radius: 6px;
        }

        pre {
            background: #111827;
            color: #f9fafb;
            padding: 15px;
            border-radius: 10px;
            overflow-x: auto;
        }

        ul {
            padding-left: 20px;
        }

        .highlight {
            color: #2563eb;
            font-weight: bold;
        }

        .architecture {
            text-align: center;
            font-weight: bold;
            background: #eff6ff;
            padding: 15px;
            border-radius: 10px;
            font-size: 18px;
        }

        .footer {
            text-align: center;
            margin-top: 40px;
            color: #6b7280;
        }
    </style>
</head>
<body>

    <h1>System Performance Prediction & Anomaly Detection</h1>

    <div style="text-align:center;">
        <span class="badge">Python</span>
        <span class="badge">Machine Learning</span>
        <span class="badge">Random Forest</span>
        <span class="badge">Isolation Forest</span>
        <span class="badge">Streamlit</span>
        <span class="badge">Real-Time Monitoring</span>
    </div>

    <div class="section">
        <h2>Project Overview</h2>
        <p>
            A real-time machine learning system for <span class="highlight">predicting system performance</span> 
            and detecting anomalous behavior using CPU, RAM, and network telemetry.
        </p>

        <p>
            Inspired by enterprise monitoring platforms like <strong>Datadog</strong> and 
            <strong>AWS CloudWatch</strong>, this project provides proactive anomaly detection,
            process-level root cause attribution, and real-time visualization for local machine monitoring.
        </p>
    </div>

    <div class="section">
        <h2>Key Features</h2>
        <ul>
            <li>Real-time monitoring of CPU, RAM, and network usage</li>
            <li>Machine learning-based CPU & RAM prediction</li>
            <li>Real-time anomaly detection using Isolation Forest</li>
            <li>Hybrid detection (ML + rule-based anomaly logic)</li>
            <li>Process-level anomaly attribution using PID analysis</li>
            <li>Desktop notifications for abnormal system behavior</li>
            <li>Interactive dashboard built with Streamlit</li>
            <li>JSON anomaly logging for post-incident analysis</li>
        </ul>
    </div>

    <div class="section">
        <h2>Architecture</h2>

        <div class="architecture">
            psutil Data Collection → Feature Engineering → Scaling → Random Forest Prediction →
            Isolation Forest Detection → Alert Engine → Streamlit Dashboard
        </div>
    </div>

    <div class="section">
        <h2>Machine Learning Pipeline</h2>

        <h3>Prediction Model</h3>
        <ul>
            <li><strong>Random Forest Regressor</strong> (Selected Production Model)</li>
            <li>Linear Regression (Baseline)</li>
            <li>LSTM (Experimental Comparison)</li>
        </ul>

        <p><strong>Best Model Performance:</strong></p>
        <ul>
            <li>R² Score: <strong>0.98</strong></li>
            <li>RMSE: <strong>0.0179</strong></li>
        </ul>

        <h3>Anomaly Detection</h3>
        <ul>
            <li><strong>Isolation Forest</strong> for unsupervised anomaly detection</li>
            <li>3-hit anomaly confirmation guard</li>
            <li>Cooldown logic to prevent alert spam</li>
        </ul>
    </div>

    <div class="section">
        <h2>Feature Engineering</h2>

        <p>Temporal features were engineered to improve predictive accuracy:</p>

        <ul>
            <li><code>cpu_lag1</code>, <code>ram_lag1</code></li>
            <li><code>cpu_roll_mean</code>, <code>ram_roll_mean</code></li>
            <li><code>cpu_change</code>, <code>ram_change</code></li>
        </ul>

        <p>
            Feature engineering improved Random Forest performance from 
            <strong>R² = 0.80 → 0.98</strong>.
        </p>
    </div>

    <div class="section">
        <h2>Tech Stack</h2>

        <ul>
            <li><strong>Python</strong></li>
            <li><strong>psutil</strong> – system telemetry</li>
            <li><strong>pandas / numpy</strong> – data processing</li>
            <li><strong>scikit-learn</strong> – ML models</li>
            <li><strong>TensorFlow / Keras</strong> – LSTM experiments</li>
            <li><strong>joblib</strong> – model serialization</li>
            <li><strong>Streamlit</strong> – real-time dashboard</li>
            <li><strong>plyer</strong> – desktop alerts</li>
        </ul>
    </div>

    <div class="section">
        <h2>Project Structure</h2>

<pre>
system-performance-monitor/
│
├── data/
│   ├── train_data.csv
│   ├── test_data.csv
│   ├── scaler.pkl
│   ├── model.pkl
│   ├── threshold.pkl
│
├── realtime/
│   ├── main.py
│   ├── alert.py
│   ├── monitor.py
│   ├── data_collection.py
│   ├── feature_engineering.py
│   ├── data_processing.py
│   ├── get_top_process.py
│
├── dashboard/
│   ├── app.py
│
└── README.html
</pre>

    </div>

    <div class="section">
        <h2>Setup & Installation</h2>

<pre>
git clone https://github.com/yourusername/system-performance-monitor.git
cd system-performance-monitor

pip install -r requirements.txt
</pre>

        <p>Run real-time monitoring:</p>

<pre>
python realtime/main.py
</pre>

        <p>Launch dashboard:</p>

<pre>
streamlit run dashboard/app.py
</pre>

    </div>

    <div class="section">
        <h2>Research Inspiration</h2>

        <ul>
            <li>Isolation Forest for cloud monitoring systems</li>
            <li>Time-series anomaly detection using temporal context</li>
            <li>Advanced anomaly detection using temporal correlation graphs</li>
        </ul>
    </div>

    <div class="section">
        <h2>Future Improvements</h2>

        <ul>
            <li>Email / Slack alert integration</li>
            <li>Cloud deployment with Docker</li>
            <li>Multi-machine distributed monitoring</li>
            <li>XGBoost / ensemble prediction models</li>
            <li>Deep Isolation Forest experimentation</li>
        </ul>
    </div>

    <div class="section">
        <h2>Why This Project Matters</h2>

        <p>
            Modern infrastructure monitoring is reactive and often opaque.
            This project demonstrates how machine learning can create a lightweight,
            explainable, proactive monitoring solution for real-world systems.
        </p>
    </div>

    <div class="footer">
        Built by Shivani Dwivedi • Machine Learning • Systems Engineering
    </div>
