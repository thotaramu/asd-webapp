
import streamlit as st
import numpy as np
import pickle

# Load the trained model
model = pickle.load(open('asd_model.pkl', 'rb'))

st.title("ASD Detection Web App")

# Inputs for AQ scores
a_scores = [st.slider(f"A{i}_Score", 0, 1, 0) for i in range(1, 11)]
result = st.selectbox("Test Result", [0, 1])
country_code = st.number_input("Country Code (Encoded)", min_value=0)

if st.button("Predict"):
    input_data = np.array([a_scores + [result, country_code]])
    prediction = model.predict(input_data)
    st.success("ASD Detected!" if prediction[0] == 1 else "No ASD Detected.")
