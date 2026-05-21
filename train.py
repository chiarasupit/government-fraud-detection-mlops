import mlflow

# Set MLflow tracking directory
mlflow.set_tracking_uri("file:///Users/frangkysupit/mlruns")

experiment_name = "Fraud Detection Monitoring"

# Check if experiment exists
experiment = mlflow.get_experiment_by_name(experiment_name)

# Create experiment if missing
if experiment is None:
    experiment_id = mlflow.create_experiment(experiment_name)
else:
    experiment_id = experiment.experiment_id

# Start run with explicit experiment ID
with mlflow.start_run(experiment_id=experiment_id):

    mlflow.log_metric("accuracy", 0.99)
    mlflow.log_metric("precision", 0.91)
    mlflow.log_metric("recall", 0.84)

print("MLflow run completed successfully.")