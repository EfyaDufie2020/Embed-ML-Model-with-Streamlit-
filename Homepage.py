import streamlit as st


st.set_page_config(
    page_title="Customer Churn App",
    page_icon=":phone:",
    layout="wide",
    initial_sidebar_state="expanded"
)
# Main Content
st.title("ChurnMaster") 
st.markdown("""
            This app  uses machine learning to generate churn data for customers using Vodafone network.
        """)

# Key features
st.subheader("Key Features")
st.markdown("""
            - Predicts customer churn based on various features.
            - Provides insights into the factors contributing to churn.
            - Offers recommendations for customer retention strategies.
            - Provides a user-friendly interface for easy navigation and exploration.
            - The app also provides a detailed report on the performance of the model.
            - The report includes metrics like accuracy, precision, recall, and F1 Score.
            """)

# How to use the App
st.subheader("Navigation")

st.markdown("""
            - Click on the tabs at the side to navigate through different sections of the app.
            - Upload your CSV file containing customer data.
            - Select your desired features for classification.
            - Choose a machine learning model from the dropdown menu.
            - Click 'Classify' to get the predicted result.
            - Click on the "Download" button to export the report as a pdf file.
            """)

# Menu
st.subheader("App Features")
st.markdown(""" 
            - **DataLens** : Access to priority data
             - **DataViz**: Access to dashboard 
            """)



# User Benefits
st.subheader("User Benefits")
st.markdown("""
            - **Data-driven** : Make informed decisions backed by data analytics.
            - **Real-time** : Get insights in real-time.
            - **Easy Machine Learning**: Utilize powerful machine learning algorithms effortlessly.
            - **Predictive** : Predict customer churn with high accuracy.
            - **Interactive** : Explore and analyze data in a user-friendly interface.
            - **Customizable** : Create personalized reports.
            - **Secure** : Access data using secure authentication.
            - **Live Demo**: Watch a live demo video to see app in action.
            """)

# Create a hyperlink
st.markdown('[Watch live demo](http://localhost:8501)')


# How to run application
st.subheader("How to run application")

# activate virtual environment


st.markdown("""
```bash
env/scripts/activate
streamlit run app.py
""")


# Machine Learning Integration
st.subheader("Machine Learning Integration")
st.markdown("""
            - **Model Selction**:Choose the model you desire for accurate predictions'
            - **Seamless Integration**: Integrate predictions into your workflow with a user-friendly interface.
            - **Probability Estimates**: Gain insights into the likelihood of predicted outcomes.
            """)


# Contact Information

st.subheader("Contact Information")

# Email button
email_button = st.markdown("""
<a href="mailto:dataexpertsireland@gmail.com" style="text-decoration: none;">
    <button style="display: block; width: 100%; padding: 10px; margin: 5px 0; background-color: #4CAF50; color: white; border: none; text-align: left; font-size: 16px;">
        📧 Email: dataexpertsireland@gmail.com
    </button>
</a>
""", unsafe_allow_html=True)

# Phone button
phone_button = st.markdown("""
<a href="tel:+1234567890" style="text-decoration: none;">
    <button style="display: block; width: 100%; padding: 10px; margin: 5px 0; background-color: #008CBA; color: white; border: none; text-align: left; font-size: 16px;">
        📞 Phone: (123) 456-7890
    </button>
</a>
""", unsafe_allow_html=True)

# Address button
address_button = st.markdown("""
<a href="https://maps.google.com/?q=123 Main street, Queens, New York" target="_blank" style="text-decoration: none;">
    <button style="display: block; width: 100%; padding: 10px; margin: 5px 0; background-color: #f44336; color: white; border: none; text-align: left; font-size: 16px;">
        🏠 Address: 123 Main street, Queens, New York
    </button>
</a>
""", unsafe_allow_html=True)






# Data Visualization
            
# st.sidebar.success("click any")
# st.sidebar.title("Home")
# st.sidebar.markdown ("DataLens")
# st.sidebar.markdown ("DataViz")
# st.sidebar.markdown ("Predict")