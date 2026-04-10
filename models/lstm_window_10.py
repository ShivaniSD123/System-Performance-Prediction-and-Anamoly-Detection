import pandas as pd
import numpy as np

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout

from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# ------------------------------------------------
# 1 Load Train and Test Data
# ------------------------------------------------
train_data = pd.read_csv("../data/train_data.csv")
test_data = pd.read_csv("../data/test_data.csv")

# ------------------------------------------------
# 2 Define Target Variables
# ------------------------------------------------
targets = ["cpu_percent", "ram_percent", "net_bytes_per_sec"]


# ------------------------------------------------
# 3 Function to Create Sequences
# ------------------------------------------------
def create_sequences(data, targets, window):

    X = []
    y = []

    values = data.values
    target_index = [data.columns.get_loc(col) for col in targets]

    for i in range(window, len(data)):
        X.append(values[i-window:i])
        y.append(values[i, target_index])

    return np.array(X), np.array(y)


# ------------------------------------------------
# 4 Create Time Windows
# ------------------------------------------------
window_size = 10

X_train, y_train = create_sequences(train_data, targets, window_size)
X_test, y_test = create_sequences(test_data, targets, window_size)


print("Train Shape:", X_train.shape)
print("Test Shape:", X_test.shape)


# ------------------------------------------------
# 5 Build LSTM Model
# ------------------------------------------------
model = Sequential()

model.add(LSTM(
    64,
    return_sequences=True,
    input_shape=(X_train.shape[1], X_train.shape[2])
))

model.add(Dropout(0.2))

model.add(LSTM(32))
model.add(Dropout(0.2))

model.add(Dense(3))   # predicting cpu, ram, network


# ------------------------------------------------
# 6 Compile Model
# ------------------------------------------------
model.compile(
    optimizer="adam",
    loss="mse"
)


# ------------------------------------------------
# 7 Train Model
# ------------------------------------------------
history = model.fit(
    X_train,
    y_train,
    epochs=20,
    batch_size=32,
    validation_split=0.1
)


# ------------------------------------------------
# 8 Predictions
# ------------------------------------------------
y_pred = model.predict(X_test)
x_pred=model.predict(X_train)

# ------------------------------------------------
# 9 Evaluation Metrics
# ------------------------------------------------
mse = mean_squared_error(y_test, y_pred)
x_mse=mean_squared_error(y_train, x_pred)
rmse = np.sqrt(mse)

mae = mean_absolute_error(y_test, y_pred)

r2 = r2_score(y_test, y_pred)


print("\nLSTM Results")
print("MAE:", mae)
print("MSE:", mse)
print("Train MSE ", x_mse)
print("RMSE:", rmse)
print("R2 Score:", r2)
