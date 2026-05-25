import streamlit as st
import requests

st.title("Machine Learning Model Prediction")
st.write("Enter the details to get the prediction from the model")

age = st.number_input("Age", min_value=0, max_value=100, value=30)

workclass = st.selectbox(
    "Workclass",
    ["Private", "Self emp not inc", "Self emp inc", "Federal gov", "Local gov", "State gov", "Without pay", "Never worked"]
)

fnlwgt = st.number_input("Final Weight", min_value=0, value=100000)

education = st.selectbox(
    "Education",
    ["Bachelors", "Some college", "11th", "HS grad", "Prof school", "Assoc acdm", "Assoc voc", "9th", "7th 8th", "12th", "Masters", "1st 4th", "10th", "Doctorate", "5th 6th", "Preschool"]
)

educational_num = st.number_input("Educational Number", min_value=0, max_value=16, value=10)

marital_status = st.selectbox(
    "Marital Status",
    ["Married civ spouse", "Divorced", "Never married", "Separated", "Widowed", "Married spouse absent", "Married AF spouse"]
)

occupation = st.selectbox(
    "Occupation",
    ["Tech support", "Craft repair", "Other service", "Sales", "Exec managerial", "Prof specialty", "Handlers cleaners", "Machine op inspct", "Adm clerical", "Farming fishing", "Transport moving", "Priv house serv", "Protective serv", "Armed Forces"]
)

relationship = st.selectbox(
    "Relationship",
    ["Wife", "Own child", "Husband", "Not in family", "Other relative", "Unmarried"]
)

race = st.selectbox(
    "Race",
    ["White", "Black", "Asian Pac Islander", "Amer Indian Eskimo", "Other"]
)

gender = st.selectbox("Gender", ["Male", "Female"])

capital_gain = st.number_input("Capital Gain", min_value=0, value=0)
capital_loss = st.number_input("Capital Loss", min_value=0, value=0)

hours_per_week = st.number_input("Hours per week", min_value=0, max_value=168, value=40)

native_country = st.selectbox(
    "Native Country",
    ["United States", "Cambodia", "England", "Puerto Rico", "Canada", "Germany", "Outlying US Guam USVI etc", "India", "Japan", "Greece", "South", "China", "Cuba", "Iran", "Honduras", "Philippines", "Italy", "Poland", "Jamaica", "Vietnam", "Mexico", "Portugal", "Ireland", "France", "Dominican Republic", "Laos", "Ecuador", "Taiwan", "Haiti", "Columbia", "Hungary", "Guatemala", "Nicaragua", "Scotland", "Thailand"]
)

if st.button("Predict"):
    url = "https://ahsanahmede7-machine-learning-model.hf.space/predict"

    data = {
        "age": age,
        "workclass": workclass,
        "fnlwgt": fnlwgt,
        "education": education,
        "educational_num": educational_num,
        "marital_status": marital_status,
        "occupation": occupation,
        "relationship": relationship,
        "race": race,
        "gender": gender,
        "capital_gain": capital_gain,
        "capital_loss": capital_loss,
        "hours_per_week": hours_per_week,
        "native_country": native_country
    }

    response = requests.post(url, params=data)

    if response.status_code == 200:
        prediction = response.json().get("prediction")
        st.success(f"The predicted income is: {prediction}")
    else:
        st.error("Error in prediction. Please try again.")