import streamlit as st
import os

st.set_page_config(page_title="Model Prediction", page_icon="🏠", layout="wide")
st.title("Model Prediction")

path = os.path.join("artifacts", "models", "model.pkl")

st.write(path)