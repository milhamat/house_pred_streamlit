import numpy as np
import streamlit as st
import pickle
import os

# Path to the model
path = os.path.join("artifacts", "models", "model.pkl")

# Load the model once and store it in session state
if 'model' not in st.session_state:
    try:
        with open(path, "rb") as file:
            st.session_state.model = pickle.load(file)
    except FileNotFoundError:
        st.error(f"Could not find the model file at {path}. Please ensure the file exists.")
        st.stop()

# Initialize session state for prediction
if 'predicted_price' not in st.session_state:
    st.session_state.predicted_price = None

# Set page configuration
st.set_page_config(page_title="Model Prediction", page_icon="🏠", layout="wide")
st.title("Model Prediction")

# Sliders for input features
lf = st.slider("LotFrontage", 0, 130, 25)
la = st.slider("LotArea", 0, 130, 25)
oq = st.slider("OverallQual", 0, 130, 25)
yb = st.slider("YearBuilt", 1900, 2023, 2000)
yr = st.slider("YearRemodAdd", 1900, 2023, 2005)
gla = st.slider("GrLivArea", 0, 130, 25)
fb = st.slider("FullBath", 0, 5, 2)
hb = st.slider("HalfBath", 0, 5, 1)
bag = st.slider("BedroomAbvGr", 0, 10, 3)
trag = st.slider("TotRmsAbvGrd", 0, 15, 7)

# Input features array
input_features = np.array([[lf, la, oq, yb, yr, gla, fb, hb, bag, trag]])

# Button to trigger prediction
if st.button("Predict Price"):
    try:
        # Perform prediction
        predicted_price = st.session_state.model.predict(input_features)[0]
        # Store the prediction in session state
        st.session_state.predicted_price = np.expm1(predicted_price)  # Use exponential transformation if needed
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")

# Display the prediction
if st.session_state.predicted_price is not None:
    st.success(f"The predicted price is: ${st.session_state.predicted_price:,.2f}")
