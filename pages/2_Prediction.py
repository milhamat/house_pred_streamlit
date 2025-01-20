import streamlit as st
import os

st.set_page_config(page_title="Model Prediction", page_icon="🏠", layout="wide")
st.title("Model Prediction")

lf = st.slider("LotFrontage", 0, 130, 25)
st.write(lf)

la = st.slider("LotArea", 0, 130, 25)
st.write(la)

oq = st.slider("OverallQual", 0, 130, 25)
st.write(oq)

yb = st.slider("YearBuilt", 0, 130, 25)
st.write(yb)

yr = st.slider("YearRemodAdd", 0, 130, 25)
st.write(yr)

gla = st.slider("GrLivArea", 0, 130, 25)
st.write(gla)

fb = st.slider("FullBath", 0, 130, 25)
st.write(fb)

hb = st.slider("HalfBath", 0, 130, 25)
st.write(hb)

bag = st.slider("BedroomAbvGr", 0, 130, 25)
st.write(bag)

trag = st.slider("TotRmsAbvGrd", 0, 130, 25)
st.write(trag)

path = os.path.join("artifacts", "models", "model.pkl")
st.write(path)