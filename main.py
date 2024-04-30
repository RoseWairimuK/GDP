import streamlit as st
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit_option_menu import option_menu
from numerize.numerize import numerize
import warnings
import plotly.graph_objects as go
import pickle
import xgboost as xgb
warnings.filterwarnings('ignore')


# Loading the cleaned dataset to visualise a few plots on the App
csv_url = "https://raw.githubusercontent.com/RoseWairimuK/Files/main/cleaned_gdp_data.csv"
df = pd.read_csv(csv_url)

# Setting page configuration
st.set_page_config(page_title="GDP Analysis", page_icon="🌎", layout="wide")
st.title("🌎 Prediction of GDP per Capita($) Based on Geo-Economic Factors")

# Removing comma separator from Year Column that was bit problematic
df['Year'] = df['Year'].astype("str")

# Sidebar Section
st.sidebar.image("data/gdp.png", caption="GDP ANALYSIS AND PREDICTION BY ROSEMARY KANYORO")
st.sidebar.image("data/about.png")
st.sidebar.write("GDP per capita is an important economic metric used globally by economists to analyse a country's prosperity based on its economic growth by measuring how much of a country's overall economic production value can be attributed to each of its citizens. "
                 "Explore the various geo-economic development factors that affect GDP per capita for different countries and simulate and predict from your inputs of choice using the eXtreme Gradient Boosting machine learning algorithm that has been trained and tested for the best performance!")

# Adding access to my project notebook from GitHub
st.sidebar.markdown("### Access Jupyter Notebook Here")
github_link = "https://github.com/RoseWairimuK/GDP/blob/main/gdp.ipynb"
st.sidebar.markdown(f"[Open Notebook on GitHub]({github_link})")

st.sidebar.image("data/gdpc.png")
#••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
# 1. VIEW DATASET SECTION
# Creating an expander for dataset view
with st.expander("View Dataset and Filter Preferred Region and Country", expanded=True):

    col1, col2 = st.columns(2)

    with col1:
        selected_regions = st.multiselect("Filter by Region eg. Sub-Saharan Africa ", options=["All"] + list(df["Region"].unique()), default=["All"], key="region_filter")

    with col2:
        # Filtering countries based on selected regions
        if "All" in selected_regions:
            available_countries = list(df["Country"].unique())
        else:
            available_countries = list(df[df["Region"].isin(selected_regions)]["Country"].unique())

        selected_countries = st.multiselect("Filter by Country eg. Kenya", options=["All"] + available_countries, default=["All"], key="country_filter")

    # Applying filters
    if "All" in selected_regions:
        selected_regions = list(df["Region"].unique())  
    if "All" in selected_countries:
        selected_countries = list(df["Country"].unique())  

    filtered_df = df[
        df["Region"].isin(selected_regions) &
        df["Country"].isin(selected_countries)
    ]

    # Displaying filtered dataset
    st.write("### 🔢 Dataset")
    st.dataframe(filtered_df)

#••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
# 2. THE KEY METRICS SECTION
# Creating Key Metrics section
st.subheader("📈 Key Metrics")

with st.expander("Key Metrics Related to Region and Country Selected Above as of the Latest Data. You can filter based on your selection above!", expanded=True):
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
# 3. THE UNIVARIATE, BIVARIATE AND MULTIVARIATE EDA SECTION
# Creating the EDA section

st.subheader("📊 Exploratory Data Analysis")

with st.expander("Explore Features of Interest and Relationships", expanded=True):
    # Setting uo the region and country filters 
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

    # Analysis dropdown option
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
#4. SETTING UP THE GDP SIMULATOR
# Filtering data for the year 2018 (latest) in order to plot a comparison
df_2018 = df[df['Year'] == "2018"]  # Format 'Year' as a string

# Calculating the average GDP per capita for each region in 2018
average_gdp_per_region_2018 = df_2018.groupby('Region')['GDP_$_per_capita'].mean()

# Defining the input section
st.title("🌍 GDP per capita simulator")
st.write("Please input the following features:")

col1, col2 = st.columns(2)

with col1:
    population = st.number_input("Population (eg. 50,000,000)", key="population")
    pop_density = st.number_input("Population Density (people per sq. m)", key="pop_density")
    infant_mortality = st.number_input("Infant Mortality Rate (per 1000 births)", key="infant_mortality")
    literacy_rate = st.number_input("Literacy Rate (%)", key="literacy_rate")
    phones_per_1000 = st.number_input("Phones (per 1000 People)", key="phones_per_1000")
with col2:
    birth_rate = st.number_input("Birth Rate (per 1000 people per year)", key="birth_rate")
    death_rate = st.number_input("Death Rate (per 1000 people per year)", key="death_rate")
    agriculture = st.number_input(" Value added from Agriculture $B" , key="agriculture")
    industry = st.number_input("Value added from Industry $B", key="industry")
    service = st.number_input("Value added from Service $B", key="service")

# When user clicks the "Predict GDP" button
if st.button("Predict GDP", key="predict_button"):
    # Loading the trained XGBoost model
    with open('Xgb_model.pkl', 'rb') as f:
        model = pickle.load(f)

    # Creating a feature vector
    features = [[population, pop_density, infant_mortality, literacy_rate, phones_per_1000, birth_rate, death_rate, agriculture, industry, service]]

    # Making prediction
    prediction = model.predict(features)

    # Showing the predicted GDP per capita
    st.write(f"##### Based on these factors the Predicted GDP per capita is: ${prediction[0]:,.2f}")

    # Creating a DataFrame with prediction and average GDP per capita for each region for comparison
    df_plot = pd.DataFrame({'Region': list(average_gdp_per_region_2018.index) + ['YOUR PREDICTION'],
                            'GDP per capita': list(average_gdp_per_region_2018.values) + [prediction[0]]})

    # Sorting the DataFrame by GDP per capita in descending order
    df_plot_sorted = df_plot.sort_values(by='GDP per capita', ascending=False)

    # Plotting the predicted GDP versus average GDP for each region in 2018
    st.subheader("👉 View Your Prediction vs. Average GDP for the Regions")

    # Creating a bar plot
    fig = go.Figure()

    # Adding bars for each region
    for region, gdp_per_capita in zip(df_plot_sorted['Region'], df_plot_sorted['GDP per capita']):
        color = 'orange' if region == 'YOUR PREDICTION' else 'green'
        fig.add_trace(go.Bar(x=[region], y=[gdp_per_capita], marker_color=color, showlegend=False))

    # Updating layout
    fig.update_layout(title='A comparison of the Predicted GDP vs. Average GDP per Region (2018)',
                    xaxis_title='Region',
                    yaxis_title='GDP per capita')

    # Showing the plot
    st.plotly_chart(fig)
