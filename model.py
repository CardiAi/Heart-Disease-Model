# models.py
import joblib
import numpy as np
import pandas as pd

model = joblib.load('heart_disease_pipline.pkl')



#  map the input data to the model input

model_input_mapping = {
    'age': 'age',
    'sex': 'sex',
    'chest_pain': 'cp',
    'blood_pressure': 'trestbps',
    'cholesterol': 'chol',
    'blood_sugar': 'fbs',
    'ecg': 'restecg',
    'max_thal': 'thalch',
    'exercise_angina': 'exang',
    'old_peak': 'oldpeak',
    'slope': 'slope',
    'coronary_artery': 'ca',
    'thal': 'thal'
}


def map_input(data):
    mapped_data = {key: np.nan for key in model_input_mapping.values()}

    for key, value in data.items():
        if key in model_input_mapping:
            mapped_data[model_input_mapping[key]] = value if value is not None else np.nan
        else:
            raise ValueError(f'Key {key}  Invalid key provided. Please provide a valid key.')
  
    return mapped_data



def model_predict(data):

    input_data = map_input(data)

    input_df = pd.DataFrame(input_data, index=[0])
    print(input_data)

    prediction = model.predict(input_df)

    return prediction.tolist()[0]


