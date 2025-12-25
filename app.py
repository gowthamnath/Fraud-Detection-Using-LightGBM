import streamlit as st
import pandas as pd
import joblib

model = joblib.load("lgb_model.pkl")
st.title("Fraud Detection Prediction App")


st.markdown("Please enter the transaction details and use the predict button")

st.divider()

# Mapping for transaction types
type_mapping = {
    "CASH_IN": 0,
    "CASH_OUT": 1,
    "DEBIT": 2,
    "PAYMENT": 3,
    "TRANSFER": 4
}
# User selects friendly label
transaction_type_label = st.selectbox("Select Transaction Type", list(type_mapping.keys()))
Type_Encoded = type_mapping[transaction_type_label]  # convert to numeric code for model

amount = st.number_input("Enter Amount", min_value=0.0, value=1000.0)
oldbalanceOrg = st.number_input("Old Balance(Sender)", min_value=0.0, value=10000.0)
newbalanceOrig = st.number_input("New Balance(Sender)", min_value=0.0, value=9000.0)
oldbalanceDest = st.number_input("Old Balance(Receiver)", min_value=0.0, value=0.0)
newbalanceDest = st.number_input("New Balance(Receiver)", min_value=0.0, value=0.0)

if st.button("Predict Now"):
    input_data = pd.DataFrame([{
        "amount": amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest,
        "type": Type_Encoded
    }])

    prediction = model.predict(input_data)[0]

    st.subheader(f"Prediction: '{int(prediction)}'")

    if prediction == 1:
        st.error("This transaction can be fraud")
    else:
        st.success("This transaction is not fraud")

st.markdown(
    """
    <style>
    .stApp {
        background-color: #5D4037;
    }
    </style>
    """,
    unsafe_allow_html=True
)

    
st.markdown(
    """
    <style>
    .stApp {
        font-style: italic;
    }
    </style>
    """,
    unsafe_allow_html=True
)

