#!/usr/bin/env python
# coding: utf-8

# In[1]:


# MODEL CREATION

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import pickle

# Load dataset
df = pd.read_csv(r"C:\Users\ALGIN FARRELL\Desktop\New projects\StressMate\data\StressLevelDataset.csv")

# Select only the 7 key features
selected_features = [
    "anxiety_level",
    "depression",
    "sleep_quality",
    "study_load",
    "future_career_concerns",
    "peer_pressure",  
    "social_support"
]

X = df[selected_features]
y = df["stress_level"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Logistic Regression model
model = LogisticRegression(max_iter=500)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("✅ Model Training Complete")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

import os
os.makedirs("models", exist_ok=True)

pickle.dump(model, open("models/stress_model.pkl", "wb"))
print("💾 Model saved as models/stress_model.pkl")


# In[2]:


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

