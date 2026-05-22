# Government Fraud Detection MLOps Pipeline

## Overview

This project implements an end-to-end MLOps pipeline for Government Fraud Detection using Machine Learning, Flask REST API, MLflow Experiment Tracking, Data Drift Monitoring, and CI/CD Automation with GitHub Actions.

The system trains a fraud detection model using historical transaction data and continuously monitors incoming monthly datasets for data drift. When significant drift is detected, the model is automatically retrained.

---

# Project Architecture

1. Data Collection
2. Model Training using Random Forest
3. MLflow Experiment Tracking
4. Flask REST API Deployment
5. Data Drift Monitoring
6. Automated Retraining
7. CI/CD Automation using GitHub Actions

---

# Technologies Used

- Python
- Flask
- Scikit-learn
- Pandas
- MLflow
- Joblib
- GitHub Actions

---

# Project Structure

```bash
government-fraud-detection-mlops/
│
├── app.py
├── train.py
├── retrain.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── .github/
│   └── workflows/
│       └── retrain.yml
│
├── data/
├── models/
└── mlruns/
