
import streamlit as st
import numpy as np
import pickle

# Load the trained model
model = pickle.load(open('asd_model.pkl', 'rb'))

st.title("Autism Spectrum Disorder (ASD) Detection")

st.markdown("""
Please answer the following questions based on your observations.  
**Select 1 for "Yes" and 0 for "No".**
""")

# AQ-10 questions
questions = [
    "1. I often notice small sounds when others do not.",
    "2. I usually concentrate more on the whole picture than the small details.",
    "3. I find it easy to do more than one thing at a time.",
    "4. If there is an interruption, I can switch back to what I was doing quickly.",
    "5. I find it easy to 'read between the lines' when someone is talking.",
    "6. I know how to tell if someone listening is getting bored.",
    "7. When I’m reading a story, I find it easy to imagine what the characters might look like.",
    "8. I find it easy to work out what someone is thinking or feeling just by looking at their face.",
    "9. I find it hard to make new friends.",
    "10. I notice patterns in things all the time."
]

# Create radio buttons for each question
a_scores = []
for q in questions:
    a_scores.append(st.radio(q, [1, 0], index=1, key=q))

result = st.selectbox("Test Result (From actual screening):", [0, 1])
country_code = st.number_input("Country Code (Encoded)", min_value=0)

if st.button("Predict"):
    input_data = np.array([a_scores + [result, country_code]])
    prediction = model.predict(input_data)
    st.success("🧠 ASD Detected!" if prediction[0] == 1 else "✅ No ASD Detected.")
