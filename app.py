from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json

    # Fake prediction logic
    fraud_probability = 0.82

    return jsonify({
        "fraud_probability": fraud_probability
    })

if __name__ == '__main__':
    app.run(debug=True)