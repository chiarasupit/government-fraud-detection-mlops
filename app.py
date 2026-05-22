from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load trained model
model = joblib.load(
    "/Users/frangkysupit/Downloads/models/model.pkl"
)

# Feature list expected by model
EXPECTED_FEATURES = [
    "Time",
    "V1", "V2", "V3", "V4", "V5",
    "V6", "V7", "V8", "V9", "V10",
    "V11", "V12", "V13", "V14", "V15",
    "V16", "V17", "V18", "V19", "V20",
    "V21", "V22", "V23", "V24", "V25",
    "V26", "V27", "V28",
    "Amount"
]

# Home route
@app.route('/')
def home():

    return "Fraud Detection API is running"

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():

    data = request.json

    # Fill missing features with 0
    input_dict = {}

    for feature in EXPECTED_FEATURES:

        input_dict[feature] = data.get(feature, 0)

    # Convert to DataFrame
    input_data = pd.DataFrame([input_dict])

    # Predict probability
    prediction = model.predict_proba(input_data)[0][1]

    return jsonify({
        "fraud_probability": float(prediction)
    })

# Run app
if __name__ == '__main__':

    app.run(debug=True)