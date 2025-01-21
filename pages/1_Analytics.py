import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

st.set_page_config(page_title="Data Analytics", page_icon="📊", layout="wide")
st.title("📊 Data Analytics")

# Load dataset
path = os.path.join("artifacts", "train.csv")
data = pd.read_csv(path)

# Select relevant features and preprocess
selected = [
    "LotFrontage", "LotArea", "OverallQual", "YearBuilt", "YearRemodAdd",
    "GrLivArea", "FullBath", "HalfBath", "BedroomAbvGr", "TotRmsAbvGrd", "SalePrice"
]
df = data[selected]

# Handle missing values
df['LotFrontage'] = df['LotFrontage'].fillna(df['LotFrontage'].mean())

# Log-transform SalePrice to reduce skewness
df['LogSalePrice'] = np.log(df['SalePrice'])

# Correlation Analysis
st.header("Correlation Analysis")
correlation_matrix = df.corr()
fig1 = plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix")
st.pyplot(fig1)
st.subheader("Observations:")
st.write("- The correlation matrix shows the relationship between the features and the target variable SalePrice.")
st.write("- We can see that there is several features that strong correlation like LogSalePrice, OverallQual, GrLivArea, FullBath, TotRmsAbvGrd, YearBuilt, YearRemodAdd.")

# Distribution Analysis: SalePrice
st.header("Distribution Analysis: SalePrice")
fig2 = plt.figure(figsize=(8, 6))
sns.histplot(df['SalePrice'], kde=True, bins=30, color="skyblue")
plt.title("Distribution of SalePrice")
plt.xlabel("SalePrice")
plt.ylabel("Frequency")
st.pyplot(fig2)
st.subheader("Observations:")
st.write("- The histogram shows the distribution of SalePrice. We can see that the distribution is right-skewed, which can be addressed by log-transforming the target variable.")

# Feature vs SalePrice: Scatter Plots
st.header("Feature vs SalePrice: Scatter Plots")
features_to_plot = ["LotFrontage", "LotArea", "GrLivArea", "YearBuilt"]
fig3 = plt.figure(figsize=(12, 8))
for i, feature in enumerate(features_to_plot, 1):
    ax = fig3.add_subplot(2, 2, i)
    sns.scatterplot(x=df[feature], y=df['SalePrice'], alpha=0.6, ax=ax)
    ax.set_title(f"{feature} vs SalePrice")
    ax.set_xlabel(feature)
    ax.set_ylabel("SalePrice")
fig3.tight_layout()
st.pyplot(fig3)
st.subheader("Observations:")
st.write("- The scatter plots show the relationship between the selected features and SalePrice. We can observe some patterns and outliers in the data.")
st.write("- Features like GrLivArea have a strong influence on SalePrice, while LotFrontage and LotArea show weaker correlations.")
st.write("- Houses built more recently generally have higher sale prices, though the relationship is not linear.")


# Feature Group Analysis: OverallQual
st.header("Feature Group Analysis: OverallQual")
fig4 = plt.figure(figsize=(8, 6))
sns.boxplot(x=df['OverallQual'], y=df['SalePrice'], palette="viridis")
plt.title("Overall Quality vs SalePrice")
plt.xlabel("Overall Quality")
plt.ylabel("SalePrice")
st.pyplot(fig4)
st.subheader("Observations:")
st.write("- The boxplot shows the relationship between OverallQual (Overall Quality) and SalePrice. We can see that there is a clear positive correlation between the two variables.")

# Time Trends: YearBuilt and YearRemodAdd
st.header("Time Trends: YearBuilt and YearRemodAdd")
fig5 = plt.figure(figsize=(10, 6))
sns.lineplot(x="YearBuilt", y="SalePrice", data=df, label="Year Built", color="blue")
sns.lineplot(x="YearRemodAdd", y="SalePrice", data=df, label="Year Remodeled", color="orange")
plt.title("Price Trends Over Time")
plt.xlabel("Year")
plt.ylabel("Average SalePrice")
plt.legend()
st.pyplot(fig5)
st.subheader("Observations:")
st.write("- The line plot shows the average SalePrice trends over time based on the YearBuilt and YearRemodAdd features. We can observe dynamic fluctuations in SalePrice over the years and it has positive trends over the years.")

