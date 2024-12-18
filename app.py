import streamlit as st
import pickle
import pandas as pd

# Add custom CSS for styling
st.markdown("""
    <style>
        body {
            background-color: #f0f2f6;
            font-family: 'Arial', sans-serif;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 5px;
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        .stSelectbox>div, .stNumberInput>div {
            margin-top: 10px;
            font-size: 16px;
            padding: 8px;
        }
        .stTitle {
            text-align: center;
            color: #333;
        }
        .stText {
            font-size: 18px;
            color: #555;
            text-align: center;
        }
        .stSelectbox label {
            font-weight: bold;
        }
        .stNumberInput label {
            font-weight: bold;
        }
        .stButton {
            display: flex;
            justify-content: center;
        }
        .stSelectbox>div, .stNumberInput>div, .stTextInput>div {
            font-family: 'Arial', sans-serif;
        }
    </style>
""", unsafe_allow_html=True)

st.title("Credit Card Fraud Prediction")

# 1. distance from home to bank
distance = st.number_input("Enter the distance from home to bank in km (e.g., 0.0 for nearby, 50.0 for far)", min_value=0.0, value=0.0, step=5.0)

# 2. distance from last transaction
last_transaction = st.number_input("Enter the distance from last transaction in km", min_value=0.0, value=0.0, step=5.0)

# 3. ratio to median purchase price
ratio_to_median = st.number_input("Enter the ratio to median purchase price (e.g., 1.0 for average)", min_value=0.0, value=0.0, step=5.0)

# 4. repeat retailer (yes/no)
repeat_retailer = st.selectbox("Is it a repeat retailer?", ["Yes", "No"])
repeat_retailer = 1 if repeat_retailer == "Yes" else 0

# 5. used chip (yes/no)
used_chip = st.selectbox("Is it a used chip?", ["Yes", "No"])
used_chip = 1 if used_chip == "Yes" else 0

# 6. used pin number (yes/no)
used_pin = st.selectbox("Is it a used pin number?", ["Yes", "No"])
used_pin = 1 if used_pin == "Yes" else 0

# 7. online order (yes/no)
online_order = st.selectbox("Is it an online order?", ["Yes", "No"])
online_order = 1 if online_order == "Yes" else 0

# Load the model
model = pickle.load(open("model.pkl", "rb"))

# Prediction button
if st.button("Predict"):
    verdict = model.predict([[distance, last_transaction, ratio_to_median, repeat_retailer, used_chip, used_pin, online_order]])
    if verdict[0] == 1:
        st.write("<h3 style='color: red; text-align: center;'>Fraudulent Transaction</h3>", unsafe_allow_html=True)
    else:
        st.write("<h3 style='color: green; text-align: center;'>Legitimate Transaction</h3>", unsafe_allow_html=True)
