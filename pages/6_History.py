import streamlit as st
import pandas as pd
df = pd.read_csv('./data/history.csv')
st.dataframe(df)