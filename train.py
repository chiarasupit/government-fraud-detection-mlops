import pandas as pd
import mlflow
import mlflow.sklearn
import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score

# Load dataset
df = pd.read_csv("/Users/frangkysupit/Downloads/data/month_01.csv")

X = df.drop("Class", axis=1)
y = df["Class"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier()

model.fit(X_train, y_train)

# Predictions
preds = model.predict(X_test)

accuracy = accuracy_score(y_test, preds)
precision = precision_score(y_test, preds)
recall = recall_score(y_test, preds)

# Save model
joblib.dump(
    model,
    "/Users/frangkysupit/Downloads/models/model.pkl"
)

# Set MLflow tracking folder
mlflow.set_tracking_uri(
    "file:///Users/frangkysupit/Downloads/mlruns"
)

# Set experiment
mlflow.set_experiment(
    "Fraud Detection Monitoring"
)

with mlflow.start_run():

    mlflow.log_metric("accuracy", accuracy)
    mlflow.log_metric("precision", precision)
    mlflow.log_metric("recall", recall)

    mlflow.sklearn.log_model(
        model,
        "fraud_model"
    )

print("Initial training completed.")