import streamlit as st
import plotly.express as px
import pandas as pd
from streamlit_option_menu import option_menu
from numerize.numerize import numerize
import warnings
import plotly.graph_objects as go
warnings.filterwarnings('ignore')


# Loading the cleaned 
csv_url = "https://raw.githubusercontent.com/RoseWairimuK/Files/main/gdp_dataset.csv"
df = pd.read_csv(csv_url)

# Set page configuration
st.set_page_config(page_title="GDP Analysis",page_icon="🌎", layout="wide")
st.subheader("📊 Analysis and Prediction of GDP PER Capita ($)")
st.markdown("##")

# Convert the "Year" column back to integers
df['Year'] = df['Year'].astype("str")

#adding sidebar
st.sidebar.image("data/gdp.png", caption="GDP ANALYSIS AND PREDICTION BY ROSEMARY KANYORO")
#____________________________________________________________________________________________________________________________

# Switching options for the side bar and creating 3 main filters
#Regions filter
st.sidebar.header("Select Region")
selected_regions = st.sidebar.multiselect(
    "Select Region",
    options=["All"] + list(df["Region"].unique()),
    default=["All"]
)
if "All" not in selected_regions:
    df = df[df["Region"].isin(selected_regions)]

#Country filter
st.sidebar.header("Select Country")
selected_country = st.sidebar.multiselect(
    "Select Country",
    options=["All"] + list(df["Country"].unique()),
    default=["All"]
)
if "All" not in selected_country:
    df = df[df["Country"].isin(selected_country)]

#Year filter
st.sidebar.header("Select Year")
selected_year = st.sidebar.multiselect(
    "Select Year",
    options=["All"] + list(df["Year"].unique()),
    default=["All"]
)
if "All" not in selected_year:
    df = df[df["Year"].isin(selected_year)]


# Creating a collapsible section for the dataset and column features
with st.expander("VIEW ENTIRE DATASET OR SELECT PREFERRED FEATURES", expanded=True):
    # Multiselect columns
    selected_columns = st.multiselect(
        "Select Columns",
        options=["All"] + list(df.columns),
        default=["All"]
    )

    # Displaying the filtered dataset
    if "All" in selected_columns:
        st.write("### GDP Dataset")
        st.dataframe(df)
    else:
        st.write("### GDP Dataset")
        st.dataframe(df[selected_columns])

 #_________________________________________________________________________________________________________ 
        
# Create EDA section
st.subheader("🔎 Exploratory Data Analysis")

analysis_option = st.selectbox("Select Analysis Type", ["Univariate", "Bivariate", "Multivariate"])

# Remove "Country", "Region", and "Year" from available features
available_features = [col for col in df.columns if col not in ["Country", "Region", "Year"]]

if analysis_option == "Univariate":
    selected_feature = st.selectbox("Select Feature", available_features)
    fig = px.line(df, x="Year", y=selected_feature, title=f"Univariate Analysis: {selected_feature}")
    fig.update_traces(line=dict(color='green'))  # Set default line color to green
    st.plotly_chart(fig)

elif analysis_option == "Bivariate":
    selected_x = st.selectbox("Select X-axis Feature", available_features)
    selected_y = st.selectbox("Select Y-axis Feature", available_features)
    fig = px.scatter(df, x=selected_x, y=selected_y, title=f"Bivariate Analysis: {selected_x} vs {selected_y}")
    fig.update_traces(marker=dict(color='green'))  # Set default marker color to green
    st.plotly_chart(fig)

elif analysis_option == "Multivariate":
    selected_features = st.multiselect("Select Features", available_features, default=available_features[:2])
    default_color = 'green'  # Set default color
    colors = px.colors.qualitative.Plotly
    fig = go.Figure()
    for i, feature in enumerate(selected_features):
        color = default_color if i == 0 else colors[i % len(colors)]  # Set default color for the first feature, and use different colors for subsequent features
        fig.add_trace(go.Bar(x=df['Year'], y=df[feature], name=feature, marker_color=color))
    fig.update_layout(title=f"Multivariate Analysis: {', '.join(selected_features)}", barmode='stack')
    st.plotly_chart(fig)