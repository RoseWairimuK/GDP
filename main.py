import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load('linear_regression_model.pkl')

# Input fields for geopolitical factors
population = st.slider('Population', min_value=0, max_value=100000000, step=1000000)
area_sq_m = st.slider('Area (Sq. M)', min_value=0, max_value=10000000, step=100000)
pop_density_per_sq_m = st.slider('Population Density (per Sq. M)', min_value=0, max_value=1000, step=10)
infant_mortality = st.slider('Infant Mortality (per 1000 births)', min_value=0, max_value=100, step=1)
climate = st.selectbox('Climate', options=['1', '2', '3', '4', '5'])
birthrate = st.slider('Birthrate', min_value=0, max_value=50, step=0.1)
deathrate = st.slider('Deathrate', min_value=0, max_value=50, step=0.1)
industry = st.slider('Industry', min_value=0, max_value=100, step=1)

# Button to trigger prediction
if st.button('Predict GDP'):
    # Make predictions
    input_data = np.array([[population, area_sq_m, pop_density_per_sq_m, infant_mortality, climate, birthrate, deathrate, industry]])
    prediction = model.predict(input_data)
    
    # Display predicted GDP
    st.write('Predicted GDP:', prediction)