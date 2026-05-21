from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load trained model
model = joblib.load("/Users/frangkysupit/Downloads/models/model.pkl")

@app.route('/')
def home():
    return "Fraud Detection API is running"
def predict():

    data = request.json

    features = [[
        data["V1"],
        data["V2"],
        data["Amount"]
    ]]

    prediction = model.predict_proba(features)[0][1]

    return jsonify({
        "fraud_probability": float(prediction)
    })

if __name__ == '__main__':
    app.run(debug=True)