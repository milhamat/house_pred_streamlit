import numpy as np
import pandas as pd
import streamlit as st
import pickle
import os
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

# Define paths
MODEL_PATH = os.path.join("artifacts", "models", "model.pkl")
DATA_PATH = os.path.join("artifacts", "train.csv")

# Load model
def load_model(path):
    try:
        with open(path, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        st.error(f"Model file not found at {path}. Please ensure it exists.")
        st.stop()

# Load and preprocess data
def load_data(path):
    try:
        data = pd.read_csv(path)
        selected = [
            'Id', 'LotFrontage', 'LotArea', 'OverallQual', 'YearBuilt',
            'YearRemodAdd', 'GrLivArea', 'FullBath', 'HalfBath',
            'BedroomAbvGr', 'TotRmsAbvGrd', 'SalePrice'
        ]
        data = data[selected]
        data['LotFrontage'] = data['LotFrontage'].fillna(data['LotFrontage'].mean())
        labels = np.log(data.pop('SalePrice'))
        features = data.drop('Id', axis=1).select_dtypes(include=[np.number])
        return features.values, labels.values
    except FileNotFoundError:
        st.error(f"Data file not found at {path}. Please ensure it exists.")
        st.stop()

# Display model evaluation metrics
def display_model_metrics(model, x_test, y_test):
    y_pred = model.predict(x_test)
    metrics = {
        "R2 Score": r2_score(y_test, y_pred),
        "Root Mean Squared Error": np.sqrt(mean_squared_error(y_test, y_pred)),
        "Mean Squared Error": mean_squared_error(y_test, y_pred),
        "Mean Absolute Error": mean_absolute_error(y_test, y_pred),
    }
    for metric, value in metrics.items():
        st.write(f"{metric}: {value:.2f}")

# Initialize session state
if 'model' not in st.session_state:
    st.session_state.model = load_model(MODEL_PATH)

if 'predicted_price' not in st.session_state:
    st.session_state.predicted_price = None

# Load data
train_features, train_labels = load_data(DATA_PATH)
x_train, x_test, y_train, y_test = train_test_split(
    train_features, train_labels, test_size=0.1, random_state=0
)

# Streamlit app layout
st.set_page_config(page_title="Model Prediction", page_icon="🧙‍♀️", layout="wide")
st.title("🧙‍♀️ Model Prediction")

col1, col2 = st.columns([2, 1])

with col1:
    st.header("Input Features")
    input_features = {
        "LotFrontage": st.slider("Linear feet of street connected to property", 21, 313, 200),
        "LotArea": st.slider("Lot size in square feet", 1300, 2000, 1500),
        "OverallQual": st.slider("Overall material and finish quality", 1, 10, 5),
        "YearBuilt": st.slider("Original construction date", 1872, 2010, 1950),
        "YearRemodAdd": st.slider("Remodel date", 1950, 2010, 1980),
        "GrLivArea": st.slider("Above grade (ground) living area square feet", 334, 1000, 500),
        "FullBath": st.slider("Full bathrooms above grade", 0, 4, 2),
        "HalfBath": st.slider("Half baths above grade", 0, 2, 1),
        "BedroomAbvGr": st.slider("Bedroom above grade", 0, 8, 3),
        "TotRmsAbvGrd": st.slider("Total rooms above grade (does not include bathrooms)", 2, 15, 7),
    }

with col2:
    st.header("Model Evaluation")
    display_model_metrics(st.session_state.model, x_test, y_test)

    st.header("Prediction")
    if st.button("Predict Price"):
        try:
            input_values = np.array([list(input_features.values())])
            predicted_price = st.session_state.model.predict(input_values)[0]
            st.session_state.predicted_price = np.expm1(predicted_price)
        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")

    if st.session_state.predicted_price is not None:
        st.success(f"The predicted price is: ${st.session_state.predicted_price:,.2f}")
