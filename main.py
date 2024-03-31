import streamlit as st
import plotly.express as px
import pandas as pd
import os
import ssl
import warnings
warnings.filterwarnings('ignore')

# Function to load data from GitHub (moved before button usage)
@st.cache_data
def load_data():
    csv_url = 'https://raw.githubusercontent.com/RoseWairimuK/GDP/main/clean_data.csv'
    df = pd.read_csv(csv_url, decimal=",")
    return df.head()

# Set page configuration
st.set_page_config(
    page_title="GDP Analysis",
    page_icon=":earth_africa:",
    layout="wide"
)

# Main title in the main content area
st.title(":earth_africa: Analysis of GDP Per Capita")


# Add a button to the sidebar
if st.sidebar.button("View Dataset"):
    with st.expander("View Dataset", expanded=True):
        df = load_data()
        st.dataframe(df)  # Display data on the right side
        if st.button("Close"):
            st.text("Dataset view closed.")