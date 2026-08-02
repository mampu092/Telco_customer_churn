import streamlit as st
import pandas as pd
import joblib

model = joblib.load('churn_model.pkl')

st.set_page_config(page_title="Telco Churn Predictor")
st.title("📞 Customer Churn Predictor")
st.markdown("Enter the customer details below to predict churn.")

st.divider()

col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["Male", "Female"])
    senior_citizen = st.selectbox("Senior Citizen", ["Yes", "No"])
    partner = st.selectbox("Partner", ["Yes", "No"])
    dependents = st.selectbox("Dependents", ["Yes", "No"])
    tenure_months = st.number_input("Tenure (Months)", min_value=0, max_value=100, value=1)
    phone_service = st.selectbox("Phone Service", ["Yes", "No"])
    multiple_lines = st.selectbox("Multiple Lines", ["Yes", "No", "No phone service"])
    internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
    online_security = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
    online_backup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])

with col2:
    device_protection = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])
    tech_support = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])
    streaming_tv = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
    streaming_movies = st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])
    contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
    paperless_billing = st.selectbox("Paperless Billing", ["Yes", "No"])
    payment_method = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"])
    monthly_charges = st.number_input("Monthly Charges ($)", min_value=0.0, max_value=150.0, value=50.0)
    total_charges = st.number_input("Total Charges ($)", min_value=0.0, max_value=10000.0, value=100.0)

st.divider()

if st.button("🔮 Predict Churn"):
    input_data = pd.DataFrame({
        'Gender': [gender], 'Senior Citizen': [senior_citizen], 'Partner': [partner],
        'Dependents': [dependents], 'Tenure Months': [tenure_months], 'Phone Service': [phone_service],
        'Multiple Lines': [multiple_lines], 'Internet Service': [internet_service],
        'Online Security': [online_security], 'Online Backup': [online_backup],
        'Device Protection': [device_protection], 'Tech Support': [tech_support],
        'Streaming TV': [streaming_tv], 'Streaming Movies': [streaming_movies],
        'Contract': [contract], 'Paperless Billing': [paperless_billing],
        'Payment Method': [payment_method], 'Monthly Charges': [monthly_charges],
        'Total Charges': [total_charges]
    })
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]
    
    if prediction == 1:
        st.error(f"⚠️ HIGH RISK OF CHURN (Confidence: {probability:.1%})")
    else:
        st.success(f"✅ LOW RISK OF CHURN (Confidence: {1 - probability:.1%})")
