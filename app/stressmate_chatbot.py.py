#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# stressmate_chatbot.py

import streamlit as st
import pickle
import numpy as np

# Load trained model
model = pickle.load(open("models/stress_model.pkl", "rb"))

st.set_page_config(page_title="StressMate - Student Stress Analyzer", page_icon="🧠", layout="centered")

st.title("🧠 StressMate - Student Stress Analyzer")
st.write("Hello! I'm **StressMate**, your AI companion to check stress levels. 💬")
st.write("Answer a few quick questions and I'll predict your stress level (Low, Medium, or High).")

# Collect user inputs
anxiety = st.slider("😟 Anxiety Level (1-10)", 1, 10, 5)
depression = st.slider("😞 Depression Level (1-10)", 1, 10, 5)
sleep_quality = st.slider("😴 Sleep Quality (1-10)", 1, 10, 5)
study_load = st.slider("📚 Study Load (1-10)", 1, 10, 5)
career = st.slider("🎯 Future Career Concerns (1-10)", 1, 10, 5)
social_influence = st.slider("👥 Social Influence (1-10)", 1, 10, 5)
social_support = st.slider("🤝 Social Support (1-10)", 1, 10, 5)

# Prediction button
if st.button("🔍 Predict Stress Level"):
    # Arrange input features
    features = np.array([[anxiety, depression, sleep_quality, study_load, career, social_influence, social_support]])
    
    # Predict
    prediction = model.predict(features)[0]
    
    # Map prediction to label
    stress_labels = {0: "🟢 Low Stress", 1: "🟡 Medium Stress", 2: "🔴 High Stress"}
    st.subheader(f"Prediction: {stress_labels[prediction]}")

    # Friendly advice
    if prediction == 0:
        st.success("You're doing great! Keep maintaining your healthy habits. ")
    elif prediction == 1:
        st.warning("Take small breaks, talk to friends, and try relaxation techniques. ")
    else:
        st.error("Your stress seems high. Please consider talking to a counselor or trusted person. ")

