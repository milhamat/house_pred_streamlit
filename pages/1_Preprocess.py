import streamlit as st
import numpy as np
import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
import io
from io import BytesIO

path = os.path.join("artifacts", "train.csv")
data = pd.read_csv(path)

st.set_page_config(page_title="Data Preprocess", page_icon="🏠", layout="wide")
st.title("House Prediction Data Preprocessing")

st.write("This page is dedicated to data Preprocessing of the house prediction dataset. The dataset contains 1460 rows and 81 columns. The columns are as follows:")
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

buffer = io.StringIO()
train.info(buf=buffer)
s = buffer.getvalue()
st.write("check the missing values in the selected features")
st.text(s)

st.write("Displaying histograms for all numerical columns")
fig, ax = plt.subplots(figsize=(12, 12))
train.hist(figsize=(20, 20), color='skyblue', ax=ax)
st.pyplot(fig)

st.write("y_label Log transformation")

col1, col2 = st.columns([1, 1])

buf = BytesIO()
col1.subheader("Before")
fig1, ax = plt.subplots(figsize=(3, 3))
sns.histplot(train['SalePrice'], kde=True, color="skyblue", ax=ax)
fig1.savefig(buf, format="png")
col1.image(buf)

col2.subheader("After")
fig2, ax = plt.subplots(figsize=(3, 3))
sns.histplot(np.log(train['SalePrice']), kde=True, color="skyblue", ax=ax)
fig2.savefig(buf, format="png")
col2.image(buf)

st.write("after the Log transformation, the data is more normally distributed")
st.write("lastly, we need to fill the LotFrontage missing values with the mean value")



col1, col2 = st.columns([1, 1])

col1.subheader("Before")
fig3, ax = plt.subplots(figsize=(3, 3))
sns.histplot(train['LotFrontage'], kde=True, color="skyblue", ax=ax)
fig3.savefig(buf, format="png")
col1.pyplot(fig3)

train['LotFrontage'] = train['LotFrontage'].fillna(train['LotFrontage'].mean())

col2.subheader("After")
fig4, ax = plt.subplots(figsize=(3, 3))
sns.histplot(train['LotFrontage'], kde=True, color="skyblue", ax=ax)
fig4.savefig(buf, format="png")
col2.pyplot(fig4)

buffer = io.StringIO()
train.info(buf=buffer)
s = buffer.getvalue()
st.write("check the missing values in the LotFrontage")
st.text(s)