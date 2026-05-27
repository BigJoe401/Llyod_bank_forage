import streamlit as st
from utils import predict_churn, feature_names

st.title("Lloyd's Customer Churn Predictor")

inputs = {}

for feature in feature_names:
    inputs[feature] = st.number_input(feature, value=0.0)

if st.button('Predict Churn'):
    result = predict_churn(inputs)

    st.success(f"Prediction: {result['label']}")
    st.write(f"Churn Probability: {result['probability']:.4f}")
    st.write(f"Threshold: {result['threshold']}")