import streamlit as st
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit_option_menu import option_menu
from numerize.numerize import numerize
import warnings
import plotly.graph_objects as go
warnings.filterwarnings('ignore')


# Loading the cleaned dataset
csv_url = "https://raw.githubusercontent.com/RoseWairimuK/Files/main/gdp_dataset.csv"
df = pd.read_csv(csv_url)

# Setting page configuration
st.set_page_config(page_title="GDP Analysis", page_icon="🌎", layout="wide")
st.subheader("🌎 Prediction of GDP per Capita($) Based on Geo-Economic Factors")

# Removing comma separator from Year Column that was bit problematic
df['Year'] = df['Year'].astype("str")

# Sidebar Section
st.sidebar.image("data/gdp.png", caption="GDP ANALYSIS AND PREDICTION BY ROSEMARY KANYORO")
st.sidebar.image("data/about.png")
st.sidebar.write("GDP per capita is an important economic metric used globally by economists to analyse a country's prosperity based on its economic growth by measuring how much of a country's overall economic production value can be attributed to each of its citizens. "
                 "Explore the various geo-economic development factors that affect GDP per capita for different countries and predict the GDP per Capita from your geo-economic inputs of choice using a model that has been trained and tested")

# Adding access the notebook from GitHub
st.sidebar.markdown("### Access Jupyter Notebook Here")
github_link = "https://github.com/RoseWairimuK/GDP/blob/main/gdp.ipynb"
st.sidebar.markdown(f"[Open Notebook on GitHub]({github_link})")

#••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••

# Create an expander for dataset view
with st.expander("View Dataset and Filter Preferred Region and Country", expanded=True):
    # Align filters horizontally
    col1, col2 = st.columns(2)

    with col1:
        selected_regions = st.multiselect("Filter by Region", options=["All"] + list(df["Region"].unique()), default=["All"], key="region_filter")

    with col2:
        selected_countries = st.multiselect("Filter by Country", options=["All"] + list(df["Country"].unique()), default=["All"], key="country_filter")

    # Apply filters
    if "All" in selected_regions:
        selected_regions = list(df["Region"].unique())  # Include all regions
    if "All" in selected_countries:
        selected_countries = list(df["Country"].unique())  # Include all countries

    filtered_df = df[
        df["Region"].isin(selected_regions) &
        df["Country"].isin(selected_countries)
    ]

    # Display filtered dataset
    st.write("### Dataset")
    st.dataframe(filtered_df)

#••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••

# Creating Key Metrics section
st.subheader("🔢 Key Metrics")

with st.expander("Key Metrics Related to Region and Country Selected Above as of 2018 (Latest in Dataset)", expanded=True):
    # Filtering dataset based on selected regions and countries
    filtered_df_key_metrics = df.copy()
    if "All" not in selected_regions:
        filtered_df_key_metrics = filtered_df_key_metrics[filtered_df_key_metrics["Region"].isin(selected_regions)]
    if "All" not in selected_countries:
        filtered_df_key_metrics = filtered_df_key_metrics[filtered_df_key_metrics["Country"].isin(selected_countries)]

    # Filtering dataset specifically for the year 2018
    filtered_df_key_metrics = filtered_df_key_metrics[filtered_df_key_metrics["Year"] == "2018"]

    # Converting relevant columns to numeric data types
    numeric_columns = ['Population', 'Literacy_%', 'Birthrate', 'Deathrate', 'GDP_$_per_capita']
    filtered_df_key_metrics[numeric_columns] = filtered_df_key_metrics[numeric_columns].apply(pd.to_numeric, errors='coerce')

    # Calculating key metrics
    num_countries = len(filtered_df_key_metrics["Country"].unique())
    total_population = filtered_df_key_metrics["Population"].sum()
    average_literacy = filtered_df_key_metrics["Literacy_%"].mean()
    average_birthrate = filtered_df_key_metrics["Birthrate"].mean()
    average_deathrate = filtered_df_key_metrics["Deathrate"].mean()
    average_gdp_per_capita = filtered_df_key_metrics["GDP_$_per_capita"].mean()

    # Displaying key metrics with styling
    total1, total2, total3, total4, total5, total6 = st.columns(6, gap='small')
    with total1:
        st.info('Number of countries', icon="🌍")
        st.metric(label="Count", value=num_countries)

    with total2:
        st.info('Total Population', icon="👥")
        st.metric(label="Population", value=f"{total_population:,.0f}")

    with total3:
        st.info('Avg Literacy_%', icon="📚")
        st.metric(label="Literacy %", value=f"{average_literacy:.2f}")

    with total4:
        st.info('Avg', icon="👶")
        st.metric(label="Birthrate", value=f"{average_birthrate:.2f}")

    with total5:
        st.info('Avg Deathrate', icon="💀")
        st.metric(label="Deathrate", value=f"{average_deathrate:.2f}")

    with total6:
        st.info('Avg GDP_per Capita ($)', icon="💰")
        st.metric(label="GDP per capita", value=f"{average_gdp_per_capita:,.2f}")

#••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••

# Creating the EDA section

st.subheader("📊 Exploratory Data Analysis")

with st.expander("Explore Features of Interest and Relationships", expanded=True):
    # Filters
    col1, col2, col3 = st.columns(3)
    with col1:
        selected_region = st.selectbox("Select Region", options=["All"] + list(df["Region"].unique()), index=0)
    with col2:
        if selected_region != "All":
            filtered_countries = df[df["Region"] == selected_region]["Country"].unique()
            selected_country = st.selectbox("Select Country", options=["All"] + list(filtered_countries), index=0)
        else:
            selected_country = st.selectbox("Select Country", options=["All"] + list(df["Country"].unique()), index=0)
    with col3:
        selected_year = st.selectbox("Select Year", options=["All"] + list(df["Year"].unique()), index=0)

    # Applying filters
    filtered_df = df.copy()
    if selected_region != "All":
        filtered_df = filtered_df[filtered_df["Region"] == selected_region]
    if selected_country != "All":
        filtered_df = filtered_df[filtered_df["Country"] == selected_country]
    if selected_year != "All":
        filtered_df = filtered_df[filtered_df["Year"] == selected_year]

    # Analysis dropdown
    analysis_type = st.selectbox("Select Analysis Type", options=["Univariate", "Bivariate", "Multivariate"])

    # Removing filters from feature selection
    available_features = [col for col in df.columns if col not in ["Region", "Country", "Year"]]

    # Feature selection
    selected_features = st.multiselect("Select Features", options=["All"] + available_features, default=["All"])

    # Plotting
    try:
        if analysis_type == "Univariate":
            if selected_features != ["All"]:
                for feature in selected_features:
                    fig = px.line(filtered_df, x='Year', y=feature, title=f"Univariate Analysis of {feature}",
                                  color_discrete_sequence=['green'])
                    st.plotly_chart(fig)

        elif analysis_type == "Bivariate":
            if len(selected_features) == 2:
                feature1, feature2 = selected_features
                fig = px.scatter(filtered_df, x=feature1, y=feature2,
                                 title=f"Bivariate Analysis of {feature1} vs {feature2}",
                                 color_discrete_sequence=['green'])
                st.plotly_chart(fig)

        elif analysis_type == "Multivariate":
            if len(selected_features) > 0 and "All" not in selected_features:
                fig = px.bar(filtered_df, x='Year', y=selected_features, title="Multivariate Analysis",
                             barmode='stack', color_discrete_sequence=px.colors.qualitative.Plotly)
                st.plotly_chart(fig)

    except Exception as e:
        st.warning("An error occurred. Please recheck your selected features.")

#••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••

