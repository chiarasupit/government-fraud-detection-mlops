# Fraud Detection MLOps Pipeline

## Overview
This project demonstrates an end-to-end MLOps workflow for a fraud detection machine learning system.

The system includes:
- Flask REST API deployment
- MLflow experiment tracking
- GitHub Actions CI/CD automation
- Model monitoring and evaluation

## Technologies Used
- Python
- Flask
- MLflow
- GitHub Actions
- Postman

## REST API
The machine learning model was deployed using Flask as a REST API.

Endpoint:
POST /predict

Example response:
{
  "fraud_probability": 0.82
}

## MLflow Monitoring
MLflow was integrated to:
- track experiments
- monitor metrics
- manage model runs
- support reproducibility

Metrics tracked:
- Accuracy
- Precision
- Recall

## CI/CD with GitHub Actions
GitHub Actions was used to automate:
- dependency installation
- workflow execution
- pipeline validation

## Author
Chiara Supit
