# Telco Customer Churn Prediction

A machine learning project to predict whether a customer will churn (leave) a telecommunications company based on their subscription details, account information, and demographics.

## 🚀 Live Demo
You can test the live prediction model here:
**[Streamlit App Link](https://telco-churn-prediction.streamlit.app)** *(Replace this with your actual deployed link)*

## 📊 Project Overview
- **Goal:** Build a classification model to identify customers at high risk of churning.
- **Dataset:** Telco Customer Churn dataset (sourced from IBM).
- **Model Used:** Random Forest Classifier.
- **Performance:** Achieved an **AUC-ROC score of 0.8341** on the test set after correcting for data leakage.

## 🛠️ Technologies Used
- **Python** (Pandas, NumPy)
- **Scikit-Learn** (RandomForestClassifier, StandardScaler, OneHotEncoder, Pipeline)
- **Joblib** (Model serialization)
- **Streamlit** (Web application deployment)

## 📂 Project Files
- `Telco_customer_churn.xlsx` - The raw dataset.
- `customer_churn.ipynb` - Jupyter notebook containing EDA, data cleaning, and model training.
- `churn_model.pkl` - The serialized, trained machine learning model pipeline ready for deployment.
- `app.py` - The source code for the interactive Streamlit web application.
- `requirements.txt` - List of Python dependencies required to run the project.

## 🔧 How to Run Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/YourUsername/Telco-Churn-Prediction.git
