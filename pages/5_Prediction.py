import streamlit as st
import joblib 
import pandas as pd
import os
import datetime


st.set_page_config(
    page_title="Prediction",
    page_icon=':line_chart:',
    layout="wide",
    initial_sidebar_state="expanded"
)

@st.cache_resource()


# Load the ML model

