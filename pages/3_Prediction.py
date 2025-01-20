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

# Two-column layout
col1, col2 = st.columns([2, 1])

# Input sliders in col1
with col1:
    st.header("Input Features")
    lf = st.slider("Linear feet of street connected to property", 21, 313, 200)
    la = st.slider("Lot size in square feet", 1300, 2000, 1500)
    oq = st.slider("Overall material and finish quality", 1, 10, 5)
    yb = st.slider("Original construction date", 1872, 2010, 1950)
    yr = st.slider("Remodel date", 1950, 2010, 1980)
    gla = st.slider("Above grade (ground) living area square feet", 334, 1000, 500)
    fb = st.slider("Full bathrooms above grade", 0, 4, 2)
    hb = st.slider("Half baths above grade", 0, 2, 1)
    bag = st.slider("Bedroom above grade", 0, 8, 3)
    trag = st.slider("Total rooms above grade (does not include bathrooms)", 2, 15, 7)

# Button and prediction result in col2
with col2:
    st.header("Prediction")
    # Button to trigger prediction
    if st.button("Predict Price"):
        # Input features array
        input_features = np.array([[lf, la, oq, yb, yr, gla, fb, hb, bag, trag]])

        try:
            # Perform prediction
            predicted_price = st.session_state.model.predict(input_features)[0]
            # Store the prediction in session state
            st.session_state.predicted_price = np.expm1(predicted_price)  # Use exponential transformation if needed
        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")

    # Display the prediction result
    if st.session_state.predicted_price is not None:
        st.success(f"The predicted price is: ${st.session_state.predicted_price:,.2f}")
