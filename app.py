from flask import Flask, request, jsonify
from model import model_predict


app = Flask(__name__)

@app.route('/')
def home():
    return 'Heart Disease Prediction API'

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json

    # Make predictions
    prediction = model_predict(data)

    # Return prediction as JSON response
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)
    