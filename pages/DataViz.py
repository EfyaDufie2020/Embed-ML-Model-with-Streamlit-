import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Define the URL to the CSV file
url = "https://raw.githubusercontent.com/EfyaDufie2020/Customer-Churn-Analysis/main/Notebooks/Customer%20Churn%20Data.csv"

# Define a function to load data
@st.cache_data
def load_data():
    try:
        data = pd.read_csv(url)
        return data
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame()  # Return an empty DataFrame in case of error

# Load the data
data = load_data()

# Create the Streamlit App and add the title
st.title("Customer Churn Dashboard")




# Check if data is loaded successfully
if not data.empty:
    # Basic Statistics
    st.subheader("Basic Statistics")
    
    # Display the DataFrame with expanded layout
    st.dataframe(data.describe(), use_container_width=True)



    # Churn Distribution (Pie Chart)
    st.subheader("Churn Distribution (Pie Chart)")
    if 'Churn' in data.columns:
        churn_counts = data['Churn'].value_counts()
        fig = px.pie(values=churn_counts.values, names=churn_counts.index, title="Churn Distribution")
        st.plotly_chart(fig, use_container_width=True)  # Adjust width to container
    else:
        st.warning("Column 'Churn' not found in the data.")

    

    # Gender vs Churn
    st.subheader("Churn Rate by Gender")
    gender_churn = data.groupby('gender')['Churn'].value_counts(normalize=True).unstack()
    if 'Yes' in gender_churn.columns:
        gender_churn['Churn Rate'] = gender_churn['Yes'] * 100
        gender_churn = gender_churn.reset_index()
        fig_gender = px.bar(gender_churn, x='gender', y='Churn Rate', title="Churn Rate by Gender",
                            labels={'Churn Rate': 'Churn Rate (%)', 'gender': 'Gender'})
        st.plotly_chart(fig_gender)
    else:
        st.warning("The 'Yes' column is not found in the 'Churn' data.")



    # Senior Citizen vs Churn
    st.subheader("Churn Rate by Senior Citizen Status")
    senior_churn = data.groupby('SeniorCitizen')['Churn'].value_counts(normalize=True).unstack()
    if 'Yes' in senior_churn.columns:
        senior_churn['Churn Rate'] = senior_churn['Yes'] * 100
        senior_churn = senior_churn.reset_index()
        fig_senior = px.bar(senior_churn, x='SeniorCitizen', y='Churn Rate', title="Churn Rate by Senior Citizen Status",
                            labels={'Churn Rate': 'Churn Rate (%)', 'SeniorCitizen': 'Senior Citizen Status'})
        st.plotly_chart(fig_senior)
    else:
        st.warning("The 'Yes' column is not found in the 'Churn' data.")



    # Contract vs Churn
    st.subheader("Churn Rate by Contract Type")
    contract_churn = data.groupby('Contract')['Churn'].value_counts(normalize=True).unstack()
    if 'Yes' in contract_churn.columns:
        contract_churn['Churn Rate'] = contract_churn['Yes'] * 100
        contract_churn = contract_churn.reset_index()
        
        # Create a line chart using Plotly
        fig_contract = px.line(contract_churn, x='Contract', y='Churn Rate', title="Churn Rate by Contract Type",
                               labels={'Churn Rate': 'Churn Rate (%)', 'Contract': 'Contract Type'})
        
        st.plotly_chart(fig_contract)
    else:
        st.warning("The 'Yes' column is not found in the 'Churn' data.")



    # Monthly Charges vs Churn
    st.subheader("Churn Rate by Monthly Charges")
    
    # Bin Monthly Charges into categories
    bins = [0, 30, 60, 90, 120]
    labels = ['Low (0-30)', 'Medium (30-60)', 'High (60-90)', 'Very High (90-120)']
    data['MonthlyChargesCategory'] = pd.cut(data['MonthlyCharges'], bins=bins, labels=labels, right=False)
    
    # Group data by 'MonthlyChargesCategory' and 'Churn'
    charges_churn = data.groupby('MonthlyChargesCategory')['Churn'].value_counts(normalize=True).unstack()
    
    # Calculate churn rate
    if 'Yes' in charges_churn.columns:
        charges_churn['Churn Rate'] = charges_churn['Yes'] * 100
    else:
        st.warning("The 'Yes' column is not found in the 'Churn' data.")
    
    # Reset index to use with Plotly Express
    charges_churn = charges_churn.reset_index()

    # Plot the bar chart using Plotly Express
    fig = px.bar(charges_churn, x='MonthlyChargesCategory', y='Churn Rate',
                 title='Churn Rate by Monthly Charges',
                 labels={'Churn Rate': 'Churn Rate (%)', 'MonthlyChargesCategory': 'Monthly Charges'})
    
    # Display the chart in Streamlit
    st.plotly_chart(fig)




    # Internet Service vs Churn
    st.subheader("Churn Rate by Internet Service")
    
    # Group data by 'InternetService' and 'Churn'
    internet_churn = data.groupby('InternetService')['Churn'].value_counts(normalize=True).unstack()
    
    # Calculate churn rate
    if 'Yes' in internet_churn.columns:
        internet_churn['Churn Rate'] = internet_churn['Yes'] * 100
    else:
        st.warning("The 'Yes' column is not found in the 'Churn' data.")
    
    # Reset index to use with Plotly Express
    internet_churn = internet_churn.reset_index()

    # Plot the bar chart using Plotly Express
    fig = px.bar(internet_churn, x='InternetService', y='Churn Rate',
                 title='Churn Rate by Internet Service',
                 labels={'Churn Rate': 'Churn Rate (%)'})
    
    # Display the chart in Streamlit
    st.plotly_chart(fig)

    

    # Add interactive filters to allow users to filter data
    st.subheader("Filter Data")
    columns = data.columns.tolist()
    selected_column = st.selectbox("Select a column to filter by", columns)
    unique_values = data[selected_column].unique()
    selected_value = st.selectbox(f"Select a value from {selected_column}", unique_values)
    filtered_data = data[data[selected_column] == selected_value]
    st.write(f"Filtered Data (showing rows where {selected_column} is {selected_value}):")
    st.dataframe(filtered_data)
