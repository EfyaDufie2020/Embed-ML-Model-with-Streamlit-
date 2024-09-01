import streamlit as st
import pandas as pd

st.title ("Data Page")

# Load data with Customer churn dataset
@st.cache_data(persist=True) 
def load_data():


# Read the CSV file from the URL
    data = pd.read_csv("https://raw.githubusercontent.com/EfyaDufie2020/Customer-Churn-Analysis/main/Notebooks/Customer%20Churn%20Data.csv")
    return data

# Load the CSV file from the URL 

st.dataframe(load_data())








