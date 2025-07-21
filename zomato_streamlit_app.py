import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Zomato Data Explorer", layout="wide")
st.title("Zomato Dataset Explorer")

# Load the Excel file with correct engine
@st.cache_data
def load_data():
    return pd.read_excel("dataset2.csv", engine="xlrd")

df = load_data()

st.subheader("Raw Dataset")
st.dataframe(df)

st.subheader("Dataset Description")
st.write(df.describe())

st.subheader("Value Counts by Column")
column = st.selectbox("Choose a column", df.columns)
if column:
    st.bar_chart(df[column].value_counts())

# Correlation Heatmap
if st.checkbox("Show Correlation Heatmap"):
    st.subheader("Correlation Heatmap")
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)
