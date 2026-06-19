import streamlit as st
import pandas as pd
import joblib
from huggingface_hub import hf_hub_download

model_path = hf_hub_download(
    repo_id="guptas89/tourism-model",
    filename="best_model.pkl"
)

model = joblib.load(model_path)

st.title("Wellness Tourism Purchase Prediction")

age = st.number_input("Age")

income = st.number_input("Monthly Income")

city = st.selectbox(
    "City Tier",
    [1,2,3]
)

if st.button("Predict"):

    data = pd.DataFrame({
        "Age":[age],
        "MonthlyIncome":[income],
        "CityTier":[city]
    })

    prediction = model.predict(data)

    st.write(prediction[0])