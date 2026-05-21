import pandas as pd
import joblib
import mlflow
import mlflow.sklearn

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Simulate latest monthly data
new_data = pd.read_csv("/Users/frangkysupit/Downloads/data/month_02.csv")
old_data = pd.read_csv("/Users/frangkysupit/Downloads/data/month_01.csv")

# Simple drift detection
old_mean = old_data["Amount"].mean()
new_mean = new_data["Amount"].mean()

drift = abs(new_mean - old_mean)

print("Drift value:", drift)

# Threshold
THRESHOLD = 50

if drift > THRESHOLD:

    print("Drift detected → Retraining model")

    X = new_data.drop("Class", axis=1)
    y = new_data["Class"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier()

    model.fit(X_train, y_train)

    preds = model.predict(X_test)

    accuracy = accuracy_score(y_test, preds)

    # Overwrite old model
    joblib.dump(model, "/Users/frangkysupit/Downloads/models/model.pkl")

    # Log new model version
    mlflow.set_experiment("Fraud Detection Monitoring")

    with mlflow.start_run():

        mlflow.log_metric("accuracy", accuracy)

        mlflow.sklearn.log_model(
            model,
            "fraud_model"
        )

    print("Retraining completed.")

else:

    print("No significant drift detected.")