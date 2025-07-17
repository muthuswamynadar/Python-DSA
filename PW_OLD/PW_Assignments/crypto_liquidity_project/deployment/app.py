import streamlit as st
import numpy as np
import joblib

model = joblib.load("model.pkl")
st.title("Cryptocurrency Liquidity Predictor")

ma_7 = st.number_input("7-Day Moving Average")
ma_30 = st.number_input("30-Day Moving Average")
volatility = st.number_input("Volatility")
liquidity_ratio = st.number_input("Liquidity Ratio")

if st.button("Predict"):
    input_data = np.array([[ma_7, ma_30, volatility, liquidity_ratio]])
    prediction = model.predict(input_data)
    st.success(f"Predicted Price: {prediction[0]:.4f}")
