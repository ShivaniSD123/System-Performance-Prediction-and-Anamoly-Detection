import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load train and test data
train_data = pd.read_csv("../data/train_data_raw.csv")
test_data = pd.read_csv("../data/test_data_raw.csv")

# Target variables
targets = ["cpu_percent", "ram_percent", "net_bytes_per_sec"]

# Features
X_train = train_data.drop(columns=targets)
X_test = test_data.drop(columns=targets)

# Targets
y_train = train_data[targets]
y_test = test_data[targets]

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("Linear Regression Results")
print("MSE:", mse)
print("RMSE:", rmse)
print("R2:", r2)
