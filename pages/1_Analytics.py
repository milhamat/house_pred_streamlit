import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt

path = os.path.join("artifacts", "train.csv")
data = pd.read_csv(path)

st.set_page_config(page_title="Data Analytics", page_icon="🏠", layout="wide")
st.title("House Prediction Data Analytics")

st.write("This page is dedicated to data analytics of the house prediction dataset. The dataset contains 1460 rows and 81 columns. The columns are as follows:")
st.dataframe(data.head(5))

st.write("In this case I have selected 10 features to be analyzed. The features are as follows:")
st.write("LotFrontage, LotArea, OverallQual, YearBuilt, YearRemodAdd, GrLivArea, FullBath, HalfBath, BedroomAbvGr, TotRmsAbvGrd,SalePrice")
st.markdown(
"""
The following list won't indent no matter what I try:
 - LotFrontage    : Linear feet of street connected to property
 - LotArea        : Lot size in square feet
 - OverallQual    : Overall material and finish quality
 - YearBuilt      : Original construction date
 - YearRemodAdd   : Remodel date
 - GrLivArea      : Above grade (ground) living area square feet
 - FullBath       : Full bathrooms above grade
 - HalfBath       : Half baths above grade
 - BedroomAbvGr   : Bedroom above grade
 - TotRmsAbvGrd   : Total rooms above grade (does not include bathrooms)
"""
)

selected = ['LotFrontage', 'LotArea', 'OverallQual', 'YearBuilt',
       'YearRemodAdd', 'GrLivArea', 'FullBath', 'HalfBath', 'BedroomAbvGr',
       'TotRmsAbvGrd','SalePrice']
train = data[selected]
st.dataframe(train.head(5))

st.write("Displaying histograms for all numerical columns")
fig, ax = plt.subplots(figsize=(12, 12))
train.hist(figsize=(20, 20), color='skyblue', ax=ax)

st.pyplot(fig)