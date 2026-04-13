import pandas as pd
import numpy as np
import joblib
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# ------------------------------------------------
# 1 Load Data
# ------------------------------------------------
train_data = pd.read_csv("../data/train_data.csv")
test_data  = pd.read_csv("../data/test_data.csv")

targets = ["cpu_percent", "ram_percent"]

# ------------------------------------------------
# 2 Separate Features and Targets, then Scale
# ------------------------------------------------
X_train_raw = train_data.drop(columns=targets)
X_test_raw  = test_data.drop(columns=targets)
y_train_raw = train_data[targets]
y_test_raw  = test_data[targets]

# Scale features
feature_scaler = MinMaxScaler()
X_train_scaled = feature_scaler.fit_transform(X_train_raw)
X_test_scaled  = feature_scaler.transform(X_test_raw)

# Scale targets separately
target_scaler = MinMaxScaler()
y_train_scaled = target_scaler.fit_transform(y_train_raw)
y_test_scaled  = target_scaler.transform(y_test_raw)

# Save scalers for live use
joblib.dump(feature_scaler, "../data/lstm_feature_scaler.pkl")
joblib.dump(target_scaler,  "../data/lstm_target_scaler.pkl")

# ------------------------------------------------
# 3 Create Sequences (features only as input)
# ------------------------------------------------
def create_sequences(X, y, window):
    Xs, ys = [], []
    for i in range(window, len(X)):
        Xs.append(X[i-window:i])   # window of features
        ys.append(y[i])            # target at current step
    return np.array(Xs), np.array(ys)

window_size = 30  # increased from 10 to 30

X_train_seq, y_train_seq = create_sequences(X_train_scaled, y_train_scaled, window_size)
X_test_seq,  y_test_seq  = create_sequences(X_test_scaled,  y_test_scaled,  window_size)

print("Train Shape:", X_train_seq.shape)
print("Test Shape:",  X_test_seq.shape)

# ------------------------------------------------
# 4 Build Simpler LSTM (less overfitting)
# ------------------------------------------------
model = Sequential([
    LSTM(32, input_shape=(window_size, X_train_seq.shape[2])),
    Dropout(0.2),
    Dense(2)
])

model.compile(optimizer="adam", loss="mse")

# ------------------------------------------------
# 5 Train with Early Stopping
# ------------------------------------------------
from tensorflow.keras.callbacks import EarlyStopping

early_stop = EarlyStopping(
    monitor="val_loss",
    patience=5,          # stop if no improvement for 5 epochs
    restore_best_weights=True
)

history = model.fit(
    X_train_seq, y_train_seq,
    epochs=50,           # more epochs but early stopping saves us
    batch_size=32,
    validation_split=0.1,
    callbacks=[early_stop]
)

model.save("../data/lstm_model.keras")

# ------------------------------------------------
# 6 Evaluate (inverse transform to real scale)
# ------------------------------------------------
y_pred_scaled = model.predict(X_test_seq)
y_pred = target_scaler.inverse_transform(y_pred_scaled)
y_test = target_scaler.inverse_transform(y_test_seq)

mse  = mean_squared_error(y_test, y_pred)
mae  = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2   = r2_score(y_test, y_pred)

print("\n LSTM Results (after fixes)")
print(f"MAE:      {mae:.4f}")
print(f"MSE:      {mse:.4f}")
print(f"RMSE:     {rmse:.4f}")
print(f"R2 Score: {r2:.4f}")
metric_names = ["cpu_percent", "ram_percent"]
print("\n📊 Per-Metric Breakdown:")
print("-" * 40)
for i, name in enumerate(metric_names):
    r2  = r2_score(y_test[:, i], y_pred[:, i])
    mae = mean_absolute_error(y_test[:, i], y_pred[:, i])
    rmse = np.sqrt(mean_squared_error(y_test[:, i], y_pred[:, i]))
    print(f"{name:25s} | R2: {r2:.4f} | MAE: {mae:.4f} | RMSE: {rmse:.4f}")
