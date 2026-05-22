import pandas as pd
import joblib
import mlflow
import mlflow.sklearn
import os

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Create models folder
os.makedirs(
    "/Users/frangkysupit/Downloads/models",
    exist_ok=True
)

# MLflow tracking
mlflow.set_tracking_uri(
    "file:///Users/frangkysupit/Downloads/mlruns"
)

mlflow.set_experiment(
    "Fraud Detection Monitoring"
)

# Drift threshold
THRESHOLD = 1

# Store yearly results
results = []

print("\nStarting yearly drift monitoring...\n")

# Compare each month with previous month
for month in range(2, 13):

    old_path = (
        f"/Users/frangkysupit/Downloads/data/month_{month-1:02}.csv"
    )

    new_path = (
        f"/Users/frangkysupit/Downloads/data/month_{month:02}.csv"
    )

    # Load datasets
    old_data = pd.read_csv(old_path)
    new_data = pd.read_csv(new_path)

    # Calculate drift
    old_mean = old_data["Amount"].mean()
    new_mean = new_data["Amount"].mean()

    drift = abs(new_mean - old_mean)

    retrained = "No"

    print(f"Month {month:02}")
    print(f"Drift value: {drift:.2f}")

    # Retraining trigger
    if drift > THRESHOLD:

        print("Drift detected → Retraining model")

        X = new_data.drop("Class", axis=1)
        y = new_data["Class"]

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42
        )

        # Train updated model
        model = RandomForestClassifier()

        model.fit(X_train, y_train)

        preds = model.predict(X_test)

        accuracy = accuracy_score(
            y_test,
            preds
        )

        # Save updated model
        joblib.dump(
            model,
            "/Users/frangkysupit/Downloads/models/model.pkl"
        )

        # Log with MLflow
        with mlflow.start_run():

            mlflow.log_metric(
                "accuracy",
                accuracy
            )

            mlflow.log_metric(
                "drift",
                drift
            )

            mlflow.sklearn.log_model(
                model,
                "fraud_model"
            )

        retrained = "Yes"

        print("Retraining completed.\n")

    else:

        print("No significant drift detected.\n")

    # Store monthly summary
    results.append({
        "Month": month,
        "Drift": round(drift, 2),
        "Retrained": retrained
    })

# Final yearly summary
print("\n=== YEARLY RETRAINING SUMMARY ===\n")

for r in results:

    print(
        f"Month {r['Month']:02} | "
        f"Drift: {r['Drift']} | "
        f"Retrained: {r['Retrained']}"
    )