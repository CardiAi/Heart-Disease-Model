from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
import joblib



app = Flask(__name__)



model = joblib.load('heart_disease_pipline.pkl')


    


columns = ['age',
 'sex',
 'cp',
 'trestbps',
 'chol',
 'fbs',
 'restecg',
 'thalch',
 'exang',
 'oldpeak',
 'slope',
 'ca',
 'thal']



@app.route('/')
def home():
    return 'Heart Disease Prediction API'

@app.route('/predict', methods=['POST'])
def predict():

    data = request.json
    print(data)

    
    for column in columns:
        if column not in data:
            data[column] = np.nan

    input_df = pd.DataFrame(data, index=[0])

    # Make predictions
    prediction = model.predict(input_df)

    # Return prediction as JSON response
    return jsonify({'prediction': prediction.tolist()[0]})

if __name__ == '__main__':
    app.run(debug=True)
