import streamlit as st
import plotly.express as px
import pandas as pd
import os
import ssl
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title="GDP Analysis", page_icon=":earth_africa:",layout="wide")

st.title(":earth_africa:: Analysis of GDP Per Capita")
st.markdown('<style>div.block-container{padding-top:1rem;}</style>',unsafe_allow_html=True)


# GitHub raw file URL
ssl._create_default_https_context = ssl._create_unverified_context
csv_url = 'https://raw.githubusercontent.com/RoseWairimuK/Datasets-/main/countries%20of%20the%20world.csv'

# Read the CSV file from GitHub
df = pd.read_csv(csv_url, decimal=",")

# Display the data in Streamlit
st.dataframe(df)


