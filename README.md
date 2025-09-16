# 🧠 StressMate – Student Stress Analyzer  

StressMate is an AI-powered chatbot built with **Streamlit** that predicts student stress levels (Low, Medium, High) based on academic and lifestyle factors.  
It uses **machine learning (Logistic Regression)** trained on a stress dataset to provide quick and simple predictions.  

---

## 📌 Features
- Collects 7 key factors that affect student stress:  
  - Anxiety Level  
  - Depression  
  - Sleep Quality  
  - Study Load  
  - Future Career Concerns  
  - Social Influence  
  - Social Support  
- Predicts stress level as 🟢 Low, 🟡 Medium, or 🔴 High  
- Provides friendly advice and recommendations  
- Interactive chatbot UI powered by **Streamlit**  

---
## Live Demo

You can try the chatbot live here:  
[Open StressMate Chatbot](https://stressmate-hwxrf3mckssmvxpuwba68u.streamlit.app/)

---
## 📂 Project Structure

StressMate/
├── data/
│ └── StressLevelDataset.csv 
│
├── models/
│ └── stress_model.pkl 
│
├── app/
│ └── stressmate_chatbot.py 
│
├── train_stressmate.py 
├── requirements.txt
├── README.md 

---
🌍 Deployment

You can deploy StressMate on Streamlit Community Cloud:

-Push this repo to GitHub

-Go to Streamlit Cloud

-Deploy → Select repo & app/stressmate_chatbot.py

-Share your public link 🎉

---
📊 Dataset

Dataset used: StressLevelDataset.csv (Kaggle-based student stress dataset).

Target variable:

-0 = Low Stress

-1 = Medium Stress

-2 = High Stress

---
💡 Future Improvements

-Add more ML models (Random Forest, SVM)

-Track stress trends over time


---
## Author

**Algin Farrell**

- LinkedIn: [Your LinkedIn Profile](https://www.linkedin.com/in/algin-farrell-16681432b)  
- Email: alginfarrell82@gmail.com
