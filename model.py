# models.py
import joblib
import numpy as np
import pandas as pd

model = joblib.load('heart_disease_pipline.pkl')




def model_predict(data):

    

    input_df = pd.DataFrame(data, index=[0])
    print(data)

    prediction = model.predict(input_df)

    return prediction.tolist()[0][0]