# models.py
import joblib
import numpy as np
import pandas as pd

model = joblib.load('heart_disease_pipline.pkl')


def handle_none_values(data):
    for key in data:
        if data[key] is None:
            data[key] = np.nan
    return data


def model_predict(data):
    data = handle_none_values(data)
    print(data)
    input_df = pd.DataFrame(data, index=[0])
    prediction = model.predict(input_df)

    return prediction.tolist()[0][0]
