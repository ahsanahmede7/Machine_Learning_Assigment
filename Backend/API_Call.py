from fastapi import FastAPI
import pickle
import pandas as pd
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)
app = FastAPI()


@app.get("/")
def read_root():
    return {'message': "Hello Welcome to Our Machine Learning Model"}

@app.post("/predict")
def predict(age:int,workclass:str,fnlwgt:int,education:str,educational_num:int,marital_status:str,occupation:str,relationship:str,race:str,gender:str,capital_gain:int,capital_loss:int,hours_per_week:int,native_country:str):
    data = pd.DataFrame({
        'age': [age],
        'workclass': [workclass],
        'fnlwgt': [fnlwgt],
        'education': [education],
        'educational-num': [educational_num],
        'marital-status': [marital_status],
        'occupation': [occupation],
        'relationship': [relationship],
        'race': [race],
        'gender': [gender],
        'capital-gain': [capital_gain],
        'capital-loss': [capital_loss],
        'hours-per-week': [hours_per_week],
        'native-country': [native_country]
    })
    prediction = model.predict(data)
    return {'prediction': prediction[0]}
