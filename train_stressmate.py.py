#!/usr/bin/env python
# coding: utf-8

# In[6]:


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


# In[ ]:




