# Government Fraud Detection MLOps Project

This project demonstrates a simple MLOps pipeline for a Government Fraud Detection system using:

- Python
- Flask API
- MLflow
- GitHub Actions
- Machine Learning concepts

The system predicts the probability of fraudulent claims based on user input data.

---

# Project Overview

The project includes:

- A Flask REST API for fraud prediction
- MLflow experiment tracking
- GitHub Actions CI pipeline
- Basic machine learning workflow
- API testing using Postman

---

# Project Structure

```bash
government-fraud-detection-mlops/
│
├── app.py
├── train.py
├── requirements.txt
├── README.md
│
└── .github/
    └── workflows/
        └── main.yml
```

---

# Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | REST API |
| MLflow | Experiment tracking |
| GitHub Actions | CI/CD pipeline |
| Postman | API testing |

---

# Installation

## 1. Clone the Repository

```bash
git clone https://github.com/chiarasupit/government-fraud-detection-mlops.git
```

---

## 2. Navigate to Project Folder

```bash
cd government-fraud-detection-mlops
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Flask API

Start the Flask application:

```bash
python app.py
```

The API will run on:

```bash
http://127.0.0.1:5000
```

---

# API Endpoint

## Fraud Prediction Endpoint

### POST Request

```bash
POST /predict
```

### Sample JSON Input

```json
{
    "amount": 1200,
    "income": 2500,
    "previous_claims": 3
}
```

### Sample JSON Response

```json
{
    "fraud_probability": 0.82
}
```

---

# MLflow Experiment Tracking

This project uses MLflow to track machine learning experiments and metrics.

## Run Training Script

```bash
python train.py
```

Example output:

```bash
MLflow run completed successfully.
```

---

## Launch MLflow UI

```bash
mlflow ui --port 5002
```

Open in browser:

```bash
http://127.0.0.1:5002
```

Tracked metrics include:

- Accuracy
- Precision
- Recall

---

# GitHub Actions CI Pipeline

The project includes a GitHub Actions workflow for Continuous Integration.

The pipeline automatically:

- Sets up Python
- Installs dependencies
- Verifies Flask installation
- Verifies MLflow installation
- Runs workflow checks

Workflow file location:

```bash
.github/workflows/main.yml
```

---

# Example GitHub Actions Workflow

```yaml
name: MLOps Pipeline

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.13'

      - name: Install dependencies
        run: |
          pip install -r requirements.txt

      - name: Verify Python installation
        run: python --version

      - name: Verify Flask installation
        run: python -c "import flask; print('Flask installed successfully')"

      - name: Verify MLflow installation
        run: python -c "import mlflow; print('MLflow installed successfully')"
```

---

# Example Workflow Results

The GitHub Actions workflow successfully completed the following stages:

- Set up job
- Checkout repository
- Set up Python
- Install dependencies
- Verify Python installation
- Verify Flask installation
- Verify MLflow installation
- Complete job

---

# API Testing with Postman

The Flask API was tested using Postman.

### Example Request

```json
{
    "amount": 1200,
    "income": 2500,
    "previous_claims": 3
}
```

### Example Response

```json
{
    "fraud_probability": 0.82
}
```

---

# Future Improvements

Possible future enhancements include:

- Real machine learning model integration
- Docker containerization
- Kubernetes deployment
- Automated model retraining
- Cloud deployment
- Monitoring dashboard
- Database integration

---

# Author

Chiara Supit

---

# License

This project is for educational purposes.
