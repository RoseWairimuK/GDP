#!/usr/bin/env python
# coding: utf-8

# 
# 
# ![Picture 1.png](data:image/png;base64,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)
# 
# *   **Name: Rosemary Kanyoro**
# *   **Admission Number: 149765**
# *   **Unit: DSA 8502_Predictive and Optimization Analytics**
# 
# 
# ---
# 
# 
# 

#  **Project Title:**
# 
#  **A MACHINE LEARNING APPROACH TO PREDICTION OF KENYA'S GROSS DOMESTIC PRODUCT (GDP): ANALYSING GEO-ECONOMIC DEVELOPMENT FACTORS**
# 
# 
# ---
# 
# 
# 
#  **-> Introduction**
# 
# GDP per capita is an important economic metric used globally by economists to analyse a country's prosperity based on its economic growth by measuring how much of a country's overall economic production value can be attributed to each of its citizens.
# 
# My project attempts to investigate the various factors that affect GDP per capita for different countries and apply a machine learning algorithm to develop a model that can accurately predict the GDP. The proposed model is built on a dataset of different countries and their corresponding GDP per capita values containing the geo-economic development factors, which will be trained and validated on a separate dataset to estimate the next GDP per capita for Kenya.
# 
# ---
# 
# 
#  **-> Objectives**
# 
# I seek to answer the following questions:
# 
# 1.   What factors are most strongly correlated with the GDP per capita of a country?
# 2.   Which countries have the highest and lowest GDP per capita and are the same factors influential in both groups?
# 3. Can a machine learning algorithm be trained on the various factors and then accurately predict GDP per capita for any given country?
# 4. Will the accuracy of the predictions vary between Regions? e.g Europe vs Sub-Saharan Africa
# 5. Can I use the model to build a GDP predictor for Kenya from the insights gained about the Sub-Saharan Africa region?
# 
# 
# ---
#  **-> Dataset**
# 
# The dataset was sourced from the World Factbook hosted by U.S Central Intelligence Agency (CIA) webiste. It contains the GDP per Capita data of 227 countries categorised in 11 different regions. Data Source: https://www.cia.gov/the-world-factbook/
# 
# ---
#  **-> Assumptions**
# 
# 
# 1.   It is assumed that the GDP per Capita data sourced from the World Factbook hosted by the U.S. Central Intelligence Agency (CIA) website is accurate and reliable
# 2.   Geo-economic factors are assumed to have a meaningful relationship with a country's economic prosperity and are significant contributors to GDP variations.
# 3. It is assumed that regions marked in the dataset share commonalities in terms of economic, social, and geographic characteristics that may influence GDP per capita.
# 
# 
# 
# 
# 
# ---
#  **-> Motivation**
# 
# Majority of development experts use GDP per capita in the analysis of economic growth. The project allows me to apply both my finance and economics background to interrogate the data for a topic that is crucial for economic development by highlighting the most important factors affecting the GDP per capita and how the insights can be applied to predictions for Kenya to steer conversations and draw attention to the most critical factors for GDP growth.
# 
# 
# ---
# 
# 
# 
# 
# 
# 
# 
# 

# #  **Importing Libraries**
# 
# I begin by importing all the libraries I will use for all the code I will use in the notebook

# In[86]:


#Include libraries to be used
import matplotlib.pyplot as plt
from bokeh.io import output_notebook
from bokeh import models, palettes, transform
from bokeh.plotting import figure, show
import pandas as pd
import numpy as np
import pydotplus
import ssl
from scipy.cluster import hierarchy
import seaborn as sns
from sklearn import decomposition, preprocessing, cluster, tree
from sklearn import cluster, decomposition, pipeline, preprocessing
from yellowbrick.cluster.silhouette import SilhouetteVisualizer
import statsmodels
import io
import missingno as mn
import statsmodels.api as sm
import warnings
import xgboost as xgb
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_squared_log_error, mean_absolute_error
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import minmax_scale
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV
get_ipython().run_line_magic('matplotlib', 'inline')


# #  **Section 1) Loading and inspecting the data**

# In[87]:


#reading the data and correcting the comma separators to be decimals
ssl._create_default_https_context = ssl._create_unverified_context
df=pd.read_csv('https://raw.githubusercontent.com/RoseWairimuK/Datasets-/main/countries%20of%20the%20world.csv',decimal=",")
df.head()


# In[88]:


#checking the rows and columns to confirm the 227 countries
df.shape


# In[89]:


#inspecting the data
df.describe()


# **Section 1 observations summary:**
# 
# ---
# 
# 
# 
# *   The data contains a total of 20 columns: 19 columns show the various factors and one column is the GDP per capita.
# *   The summary statistics of the numerical columns confirm the expected variations because this is data for a variety of countries.
# *   The count row implies there are missing values in some of the columns and this will be investigated in the next section. The column titles are also not ideal and will need to be harmonised.
# 
# 
# ---
# 
# 

# #  **Section 2) Data Cleaning**
# 
# With such a large dataset it is imperative to understand the initial state of the data, identify the issues that may affect my data modelling and correct these issues. The next section covers this.
# 
# 
# 
# 
# 
# 
# 
# 

# ## **2.1) Identifying problems**
# 
# 
# 
# 
# 
# 
# 
# 
# 

# In[90]:


#viewing the columns.
df.columns


# In[91]:


#renaming columns for ease of referencing and graphics
df.rename(columns={'Area (sq. mi.)': 'Area_Sq_m', 'Coastline (coast/area ratio)': 'Coastline_coast_area_ratio','Infant mortality (per 1000 births)': 'Infant_mortality_per_1000_births','GDP ($ per capita)': 'GDP_$_per_capita','Phones (per 1000)': 'Phones_per_1000','Pop. Density (per sq. mi.)': 'Pop. Density_per_sq_m','Literacy (%)': 'Literacy_%','Arable (%)': 'Arable_%', 'Crops (%)': 'Crops_%', 'Other (%)': 'Other_%'}, inplace=True)
df.columns


# In[92]:


#checking for outliers. None, except for variations in the population per country as expected.
sns.boxplot(data = df)
plt.xticks(rotation=90);


# In[93]:


#visualising the data types. No further action needed
df.dtypes


# In[94]:


#checking nill values in the data set. Out of the 20 clumns 14 have nill values
df.isnull().any()


# In[95]:


# Function to apply background gradient
def background_gradient(val):
    if isinstance(val, (int, float)):
        color = 'background-color: lightblue' if val > 0 else ''
        return color
    return ''

# Create DataFrame with NA count and percentage
NA = pd.DataFrame(data=[df.isna().sum().tolist(), ["{:.2f}".format(i)+'%' \
                       for i in (df.isna().sum()/df.shape[0]*100).tolist()]],
                       columns=df.columns, index=['NA Count', 'NA Percent']).transpose()

# Apply background gradient using the custom function
styled_df = NA.style.applymap(background_gradient, subset=['NA Count'])

# Display styled DataFrame
styled_df


# In[96]:


#visualising the nulls
mn.matrix(df)


# ##  **2.2) Filling the missing values**
# 
# 1.   Countries that are close geologically are often similar in many ways and hence in the next section I proceed to fill in the null values using the median of the specific region that a country belongs to.  
# 2.   For categorical features like climate, I use the mode instead of median to maintain the consistency in the ratings. For instance, the climate variable in the dataset is ranked from 1-4 hence the mode maintains this rating.
# 
# 
# 
# 
# 
# 
# 
# 
# 

# In[97]:


#grouping by region to inspect the medians.
df.groupby('Region')[['GDP_$_per_capita','Literacy_%','Agriculture']].median()


# -> For more clarity on the countries found in the regions that are not commonly known:
# 
# 
# 
# 
# *   Near East - Bahrain, Cyprus, Gaza, Iraq, Israel, Jordan, Kuwait, Lebanon, Oman, Qatar, Saudi, Syria, Turkey, UAE, West Bank and Yemen.
# *   Baltics - Estonia, Latvia and Lithuania
# *   C.W. OF Ind States (Commonwealth of Independent States) - Armenia, Azerbaijan,Belarus, Georgia, Kazakhstan, Kyrgyzstan, Moldova, Russia, Tajikistan, Turmenistan, Ukraine and Uzbekistan
# 
# 
# 
# 
# 

# In[98]:


#filling the missing values
warnings.filterwarnings('ignore')
for col in df.columns.values:
    if df[col].isnull().sum() == 0:
        continue
    if col == 'Climate':
        fill_values = df.groupby('Region')['Climate'].apply(lambda x: x.mode().max())
    else:
        fill_values = df.groupby('Region')[col].median()
    for region in df['Region'].unique():
        df[col].loc[(df[col].isnull())&(df['Region']==region)] = fill_values[region]


# In[99]:


#confirming there are no missing values
df.isnull().any()


# In[100]:


#visual confirming the clean data
mn.matrix(df)


# **Section 2 observations summary:**
# 
# ---
# 
# In preparation for data modelling the identified data issues have now been resolved as follows:
# 
# *   Column titles have been renamed for clarity as well as ease of referencing in code.
# *   Missing values have been filled using the median and mode that aligns with the respective regions countries belong to.
# *  After inspecting the outliers identified, these were only evident in the population column as different countries have varying populations. There were not eliminated so as to maintain the accuracy and integrity of the underlying assumptions.
# 
# 
# ---
# 
# 

# #  **Section 3) Data Exploration**
# 
# The next sections explore the data to answer two questions from my objectives:
# 
# 
# 1.   **Which countries have the highest and lowest GDP per Capita and are the same factors influencial in both groups?**
# 
# 2. **What factors are most strongly correlated with the GDP per capita of a country?**

# ##  **3.1) Regions and Countries with the highest and lowest GDP per capita**
# 

# In[101]:


#ranking the regions
fig, ax = plt.subplots(figsize=(16,6))
#ax = fig.add_subplot(111)
top_gdp_regions = df.groupby('Region')['GDP_$_per_capita'].mean().sort_values(ascending=False).reset_index().head(25)
mean = pd.DataFrame({'Region':['WORLD MEAN'], 'GDP_$_per_capita':[df['GDP_$_per_capita'].mean()]})
gdps = pd.concat([top_gdp_regions[['Region','GDP_$_per_capita']],mean],ignore_index=True)

sns.barplot(data = gdps, x='Region', y='GDP_$_per_capita', alpha=0.7, color='#006838')
ax.set_xlabel(ax.get_xlabel(),labelpad=15)
ax.set_ylabel(ax.get_ylabel(),labelpad=30)
ax.xaxis.label.set_fontsize(10)
plt.xticks(rotation=90)
plt.show()



# In[102]:


#ranking the top 25 countries
fig, ax = plt.subplots(figsize=(16,6))
top_gdp_countries = df.sort_values('GDP_$_per_capita',ascending=False).head(25)
mean = pd.DataFrame({'Country':['WORLD MEAN'], 'GDP_$_per_capita':[df['GDP_$_per_capita'].mean()]})
gdps = pd.concat([top_gdp_countries[['Country','GDP_$_per_capita']],mean],ignore_index=True)
sns.barplot(data = gdps, x='Country', y='GDP_$_per_capita', alpha=0.7, color='#006838')
ax.set_xlabel(ax.get_xlabel(),labelpad=15)
ax.set_ylabel(ax.get_ylabel(),labelpad=30)
ax.xaxis.label.set_fontsize(16)
ax.yaxis.label.set_fontsize(16)
plt.xticks(rotation=90)
plt.show()


# In[103]:


#ranking the last 25 countries
fig, ax = plt.subplots(figsize=(16,6))

top_gdp_countries = df.sort_values('GDP_$_per_capita',ascending=False).tail(25)
mean = pd.DataFrame({'Country':['WORLD MEAN'], 'GDP_$_per_capita':[df['GDP_$_per_capita'].mean()]})
gdps = pd.concat([top_gdp_countries[['Country','GDP_$_per_capita']],mean],ignore_index=True)
sns.barplot(data = gdps, x='Country', y='GDP_$_per_capita', alpha=0.7, color='#006838')
ax.set_xlabel(ax.get_xlabel(),labelpad=15)
ax.set_ylabel(ax.get_ylabel(),labelpad=30)
ax.xaxis.label.set_fontsize(16)
ax.yaxis.label.set_fontsize(16)
plt.xticks(rotation=90)
plt.show()


# **Section 3.1 observations summary:**
# 
# ---
# 
# 
# *   The top 2 regions are Western Europe and Nothern America while Commonwealth of Independent States and Sun-Saharan Africa report the least GDP per capita.
# *   In the leading Western Europe region,  Luxembourg and the United States are the countries with the highest GDP per capita. It is noteworthy that theirs is more than 3 times the world average.  
# *   In the lagging Sub-Saharan Region, Somalia and Sierra Leone report the lowest GDP per Capita. Kenya is among the least 25 countries meaning it is ranked 203rd in the dataset as shown above.
# *   In the modelling sections, it will be imperative to check whether the predicted values for the leading and lagging regions will differ, noting the huge variation in overall GDP per capita.
# 
# 
# 
# 
# ---
# 
# 

# ##  **3.2) Correlation between the variables**
# 

# In[104]:


#correlation between the variables
plt.figure(figsize=(16,12))
sns.heatmap(data=df.iloc[:,2:].corr(),annot=True,fmt='.2f',cmap='RdBu')
plt.show()


# In[105]:


#top factors affecting GDP per capita
fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(20,12))
plt.subplots_adjust(hspace=0.4)

corr_to_gdp = pd.Series()
for col in df.columns.values[2:]:
    if ((col!='GDP_$_per_capita')&(col!='Climate')):
        corr_to_gdp[col] = df['GDP_$_per_capita'].corr(df[col])
abs_corr_to_gdp = corr_to_gdp.abs().sort_values(ascending=False)
corr_to_gdp = corr_to_gdp.loc[abs_corr_to_gdp.index]

for i in range(2):
    for j in range(3):
        sns.regplot(x=corr_to_gdp.index.values[i*3+j], y='GDP_$_per_capita', data=df,
                   ax=axes[i,j], fit_reg=False, marker='.')
        title = 'correlation='+str(corr_to_gdp[i*3+j])
        axes[i,j].set_title(title)
axes[1,2].set_xlim(0,102)
plt.show()


# In[106]:


#checking the GDP, population and migration as per region
warnings.filterwarnings('ignore')
fig = plt.figure(figsize=(18, 24))
plt.title('Regional Correlations')
ax1 = fig.add_subplot(4, 1, 1)
ax2 = fig.add_subplot(4, 1, 2)
ax3 = fig.add_subplot(4, 1, 3)
ax4 = fig.add_subplot(4, 1, 4)
sns.countplot(data= df, y= 'Region', ax= ax1, palette='RdYlGn')
sns.barplot(data= df, y= 'Region', x= 'GDP_$_per_capita', ax= ax2, palette='RdYlGn', ci= None)
sns.barplot(data= df, y= 'Region', x= 'Net migration', ax= ax3, palette='RdYlGn', ci= None)
sns.barplot(data= df, y= 'Region', x= 'Population', ax= ax4, palette='RdYlGn', ci= None)
plt.show()


# **Section 3.2 observations summary:**
# 
# ---
# 
# 
# *   The six variables that are mostly correlated to GDP per capita are phones, birthrate, infant mortality, literacy, agriculture and net migration. This result aligns with majority of research that place technology, literacy levels and mortality rates as some of the biggest influencers.  
# 
# 
# *   The fair correlation between the net migration and the GDP is accurate because migrants tend to move to countries with better opportunities and higher GDP per capita. As shown above, the highest migrations are in the Western Europe, Asia and Near East regions.
# 
# 
# *   Interestingly, SSA and Latin America have the highest number of countries whereas Asia has the largest population. Nevertheless, Nothern America and Western Europe lead in terms of GDP per capita.
# 
# 
# *  The analysis confirms that African countries typically have some of the lowest GDP per capita in the world.
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# ---
# 
# 

# # **Section 4) Modelling**
# 
# **Focus Questions:**
# 
# 3. **Can a machine learning algorithm be trained on the various factors and then
# accurately predict GDP per capita for any given country?**  
# 
# 4. **Will the accuracy of the predictions vary between Regions? e.g Europe vs Sub-Saharan Africa?**
# 
# 
# I use two models to test my objectives namely a linear regression model and a random forest model with my target variable as the GDP per Capita.These are then assessed using the The models' performance was evaluated by calculating the Root Mean Squared Error (RMSE), Mean Absolute Error (MAE), and R-squared (coefficient of determination)
# 

# ##  **4.1) Preprocessing**
# 
# **Label Encoding**
# 
# 
# Two of my variables Region and Climate are categorical features and hence I first convert these into machine readable form so that the model takes them into consideration.

# In[107]:


#label encoding the region and climate columns
LE = LabelEncoder()
df['Region_label'] = LE.fit_transform(df['Region'])
df['Climate_label'] = LE.fit_transform(df['Climate'])
df.head()


# ## **4.2) Linear Regression Model**

# In[108]:


#assigning the train and test samples of the data
train, test = train_test_split(df, test_size=0.3, shuffle=True)
training_features = ['Population', 'Area_Sq_m',
       'Pop. Density_per_sq_m', 'Coastline_coast_area_ratio',
       'Net migration', 'Infant_mortality_per_1000_births',
       'Literacy_%', 'Phones_per_1000',
       'Arable_%', 'Crops_%', 'Other_%', 'Birthrate',
       'Deathrate', 'Agriculture', 'Industry', 'Service', 'Region_label',
       'Climate_label']
target = 'GDP_$_per_capita'
train_X = train[training_features]
train_Y = train[target]
test_X = test[training_features]
test_Y = test[target]


# In[109]:


#applying the linear regression
model = LinearRegression()
model.fit(train_X, train_Y)
train_pred_Y = model.predict(train_X)
test_pred_Y = model.predict(test_X)
train_pred_Y = pd.Series(train_pred_Y.clip(0, train_pred_Y.max()), index=train_Y.index)
test_pred_Y = pd.Series(test_pred_Y.clip(0, test_pred_Y.max()), index=test_Y.index)

rmse_train = np.sqrt(mean_squared_error(train_pred_Y, train_Y))
mae_train = mean_absolute_error(train_pred_Y, train_Y)
rmse_test = np.sqrt(mean_squared_error(test_pred_Y, test_Y))
mae_test = mean_absolute_error(test_pred_Y, test_Y)
r2_train = r2_score(train_Y, train_pred_Y)
r2_test = r2_score(test_Y, test_pred_Y)

print('rmse_train:',rmse_train,'mae_train:',mae_train,'R squared train:',r2_train)
print('rmse_test:',rmse_test,'mae_test:',mae_test,'R squared test:',r2_test)


# **Section 4.2 observations summary:**
# 
# ---
# 
# 
# *  The regression model assigns the GDP per capita as the dependent variable and all others as the independent variables.  
# 
# *  The output of the Linear Regression model shows that the RMSE for the training and test set is high which indicates that there are prediction errors and that the model may not be accurately capturing all the patterns and relationships in the training data. The R-squared of 0.74 means that the model explains about 74% of the variance in the training set.
# *   For the test set, the RMSE and MAE are also high showing and the R-squared of 0.83 also shows that the model explains about 83% of the variance in the test set.
# 
# *   Overall, the model is not accurately capturing the patterns and relationships in the data. The high RMSE and MAE values on the testing set as compared to the traiuning set suggests the model might be overfitting to the training data, resulting in poorer performance on the unseen portion of the data. In the next step I try using a different model.
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# ---
# 
# 

# ##  **4.3) Random Forest Model**

# In[110]:


#applying the random forest model
model = RandomForestRegressor(n_estimators = 50,
                             max_depth = 6,
                             min_weight_fraction_leaf = 0.05,
                             max_features = 0.8,
                             random_state = 42)
model.fit(train_X, train_Y)
train_pred_Y = model.predict(train_X)
test_pred_Y = model.predict(test_X)
train_pred_Y = pd.Series(train_pred_Y.clip(0, train_pred_Y.max()), index=train_Y.index)
test_pred_Y = pd.Series(test_pred_Y.clip(0, test_pred_Y.max()), index=test_Y.index)

rmse_train = np.sqrt(mean_squared_error(train_pred_Y, train_Y))
mae_train = mean_absolute_error(train_pred_Y, train_Y)
rmse_test = np.sqrt(mean_squared_error(test_pred_Y, test_Y))
mae_test = mean_absolute_error(test_pred_Y, test_Y)
r2_train = r2_score(train_Y, train_pred_Y)
r2_test = r2_score(test_Y, test_pred_Y)

print('rmse_train:',rmse_train,'mae_train:',mae_train,'R squared train:',r2_train)
print('rmse_test:',rmse_test,'mae_test:',mae_test,'R squared test:',r2_test)


# **Section 4.3 observations summary:**
# 
# ---
# 
#   
# 
# *  The output of the Random Forest model shows that the RMSE for the training is significant implying prediction errors and that the model may not be accurately capturing all the patterns and relationships in the training data. The R-squared of 0.90 also denotes that the model explains about 90% of the variance in the training set.
# *   For the test set, the RMSE and MAE is also significant for the same reasons. The R-squared of 0.80  shows that the model explains about 80% of the variance in the test set.
# 
# *   The results show that the model may not be accurately capturing the patterns and relationships in the data. There is room for improvement in the performance of this model and I will apply a different approach and focus on one region in the next section.
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# ---
# 
# 

# ##  **4.4) Visualizing the results**
# To check the model output, I make a scatter plot of prediction against the actuals. As you can see the model gives a resonable prediction, as majority of the data points are gathering around the line y=x.

# In[111]:


# Visualising the GDP per capita
plt.figure(figsize=(18,14))

# Concatenate the Series objects train_Y, test_Y, train_pred_Y, and test_pred_Y
train_test_Y = pd.concat([train_Y, test_Y])
train_test_pred_Y = pd.concat([train_pred_Y, test_pred_Y])

df_modelled = df.loc[train_test_Y.index]
label = df_modelled['Country']

colors = {'ASIA (EX. NEAR EAST)         ':'red',
          'EASTERN EUROPE                     ':'orange',
          'NORTHERN AFRICA                    ':'gold',
          'OCEANIA                            ':'green',
          'WESTERN EUROPE                     ':'blue',
          'SUB-SAHARAN AFRICA                 ':'purple',
          'LATIN AMER. & CARIB    ':'olive',
          'C.W. OF IND. STATES ':'cyan',
          'NEAR EAST                          ':'hotpink',
          'NORTHERN AMERICA                   ':'lightseagreen',
          'BALTICS                            ':'rosybrown'}

for region, color in colors.items():
    X = train_test_Y.loc[df_modelled['Region']==region]
    Y = train_test_pred_Y.loc[df_modelled['Region']==region]
    ax = sns.regplot(x=X, y=Y, marker='.', fit_reg=False, color=color, scatter_kws={'s':200, 'linewidths':0}, label=region)
plt.legend(loc=4,prop={'size': 12})

ax.set_xlabel('GDP ($ per capita) Actuals',labelpad=40)
ax.set_ylabel('GDP ($ per capita) Predicted',labelpad=40)
ax.xaxis.label.set_fontsize(15)
ax.yaxis.label.set_fontsize(15)
ax.tick_params(labelsize=12)

x = np.linspace(-1000,50000,100)
y = x
plt.plot(x,y,c='gray')

plt.xlim(-1000,60000)
plt.ylim(-1000,40000)

for i in range(0,train_test_Y.shape[0]):
    if((df_modelled['Area_Sq_m'].iloc[i]>8e5) |
       (df_modelled['Population'].iloc[i]>1e8) |
       (df_modelled['GDP_$_per_capita'].iloc[i]>10000)):
        plt.text(train_test_Y.iloc[i]+200, train_test_pred_Y.iloc[i]-200, label.iloc[i], size='small')


# **Section 4.4 observations summary:**
# 
# 
# ---
# 
# 
# Questions Answered:
# 
# **-> Can a machine learning algorithm be trained on the various factors and then accurately predict GDP per capita for any given country?**
# 
# The line y=x represents perfect predictions, where the predicted values exactly match the actual values. My data points cluster around this line, indicating that the models are accurately capturing the relationship between the geo-economic factors which are the independent variables and the GDP per capita which is the dependent variable.
# 
# Therefore, the output proves that the model can indeed predict the GDP per capita for the countries. As shown in the scatter plot above, the predicted vs actuals of majority of the countries are aligned as they are converge along the line.
# 
# *  There is some room for improvement for the model and an option for evaluating more models but I focus on this in the next section where I narrow down to one specific region.
# 
# 
# **-> Will the accuracy of the predictions vary between Regions? e.g Europe vs Sub-Saharan Africa?**
# 
# Yes, the predicted values seem more accurate for the bottom 5 regions in terms of GDP per Capita as compared to the regions with higher GDP per Capita. In their research paper "National Income and Its Distribution',Brueckner and Lederman (2015) affirm that inequality on GDP per capita in different countries is greatly influenced by income inequalities and the effect this has on aggregate output.
# 
# Interestingly, countries in the lower GDP per Capita brackets often share similar socio-economic characteristics, presenting a more homogeneous economic landscape with fewer complexities. The above models, trained on data predominantly representing countries with lower economic development, seem to capture and generalize well to these common characteristics, thus yielding more accurate predictions.
# 
# In contrast, nations with higher GDP per Capita like Luxembourg likely exhibit greater economic diversity, intricate interdependencies, and non-linear relationships among geo-economic factors. These complexities may be the ones presenting challenges for the models in capturing the nuanced relationships accurately, leading to comparatively less precise predictions for countries in the higher GDP per Capita brackets.
# 
# 
# 
# 
# 
#   
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# ---
# 
# 

# #   **Section 5) A Deep Dive into Sub Saharan Africa (SSA) Region**
# 
# From the visualisation, it is evident that the model is more accurate for the low GDP regions as compared than Higher GDP regions. It is therefore imperative for me to redo the analysis with Sub-Saharan Africa as the focus to interrogate the factors that are more influential in this region. I can then use these insights to optimise my model and make a prediction for Kenya.

# ##  **5.1) Exploring the SSA data**

# In[112]:


#extracting SSA data
SSA_df=(df[df['Region'].str.contains("SUB-SAHARAN AFRICA")])
SSA_df.head()


# In[113]:


#describing the SSA data
SSA_df.describe()


# In[114]:


#top factors affecting GDP per capita in SSA
fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(20,12))
plt.subplots_adjust(hspace=0.4)

corr_to_gdp = pd.Series()
for col in SSA_df.columns.values[2:]:
    if ((col!='GDP_$_per_capita')&(col!='Climate')):
        corr_to_gdp[col] = SSA_df['GDP_$_per_capita'].corr(SSA_df[col])
abs_corr_to_gdp = corr_to_gdp.abs().sort_values(ascending=False)
corr_to_gdp = corr_to_gdp.loc[abs_corr_to_gdp.index]

for i in range(2):
    for j in range(3):
        sns.regplot(x=corr_to_gdp.index.values[i*3+j], y='GDP_$_per_capita', data=df,
                   ax=axes[i,j], fit_reg=False, marker='.')
        title = 'correlation='+str(corr_to_gdp[i*3+j])
        axes[i,j].set_title(title)
axes[1,2].set_xlim(0,102)
plt.show()


# In[115]:


#investigating the GDP, population and literacy in the SSA region
warnings.filterwarnings('ignore')
fig = plt.figure(figsize=(25, 33))
plt.title('A view of top 30 SSA Region GDP per Capita, Population & Literacy (Including Kenya)')
ax1 = fig.add_subplot(3, 1, 1)
ax2 = fig.add_subplot(3, 1, 2)
ax3 = fig.add_subplot(3, 1, 3)

sns.barplot(data= SSA_df, y= 'Country', x= 'GDP_$_per_capita', ax= ax1, color='#006838', ci= None)
sns.barplot(data= SSA_df, y= 'Country', x= 'Population', ax= ax2, color='#006838', ci= None)
sns.barplot(data= SSA_df, y= 'Country', x= 'Literacy_%', ax= ax3, color='#006838', ci= None)
plt.show()


# In[116]:


#a closer look at GDP vs Agriculture
fig = plt.figure(figsize=(20, 20))
sns.jointplot(data= SSA_df, x= 'Agriculture', y= 'GDP_$_per_capita', kind= 'hex',color='#006838')
plt.title('GDP Analysis: GDP vs Agriculture')
plt.show()


# **Section 5.1 observations summary:**
# 
# ---
# 
#   
# 
# *  In SSA the top countries in terms of GDP per Capita are South Africa, Mauritius, Namibia, Seychelles and Botswana and Gabon. A deeper literature review of what makes these countries lead amongst their peers confirms that in Africa the heavily agriculture, mineral and tourism based economies do better.  Eg. the economy of Gabon is also heavily dependent on its oil reserves and revenue from oil production accounts for about 43% of the country’s GDP and 81% of its exports. Botswana is boosted by its abundant natural resources such as gemstones and precious metals and South Africa benefits greatly from the production of electricity as it has a nuclear power plant(Mappr, 2023).
# 
# *   Kenya is among the contries with the highest population, with Nigeria, Ethiopia and Congo leading as at the time of this dataset. Rapid population growth that is does not grow at par with other economoc and infrastructural development tends to result in declines in GDPdue to increased per capita food consumption, poorer land quality and overally high dependency ratios. This explains the disparity in population vs the GDP per capita in the dataset.
# 
# 
# 
# *   From the dataset the literacy levels are mostly uniform in SSA with Kenya also among the countries with the highest literacy levels. On the other hand, I was surprised by the relationship between GDP and Agriculture as shown by the hex above but this proves that it cannot stand as a strong factor economically by itself especially in countries with high population. GDP per capita needs vibrancy, investment and growth in multiple economic activities to boost the overall GDP.
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# ---
# 
# 

# ##  **5.2) Pre-processing the SSA data**
# 
# In this section I start by preprocessing the SSA data in preparation for modelling. I also use a feature selection technique to complement Principal component analysis (PCA) to reduce the dimensionality of my data and pinpoint the key GDP per capital variables for the SSA region. This will ensure my prediction for Kenya will be more accurate.

# In[117]:


#normalising the data in preparation for modelling
SSA_df_normalised = SSA_df.copy()
cols = ['Population', 'Area_Sq_m', 'Pop. Density_per_sq_m',
       'Coastline_coast_area_ratio', 'Net migration',
       'Infant_mortality_per_1000_births', 'GDP_$_per_capita', 'Literacy_%',
       'Phones_per_1000', 'Arable_%', 'Crops_%', 'Other_%', 'Climate',
       'Birthrate', 'Deathrate', 'Agriculture', 'Industry', 'Service']
SSA_df_normalised[cols] = minmax_scale(SSA_df_normalised[cols])
SSA_df_normalised = SSA_df_normalised.drop(columns=['Country', 'Region', 'Region_label','Climate_label'])
SSA_df_normalised.head()


# In[118]:


#PCA
pca = PCA(n_components=10)
PC = pca.fit_transform(SSA_df_normalised)
pca_SSA = pd.DataFrame(data = PC
             , columns = ['PC1', 'PC2', 'PC3', 'PC4', 'PC5', 'PC6', 'PC7','PC8','PC9','PC10'])

pca_SSA.head(6)


# In[119]:


#visualising the PCA
fig, ax = plt.subplots(nrows=1,
                       ncols=1)
ax.bar(
    x      = np.arange(pca.n_components_) + 1,
    height = pca.explained_variance_ratio_,
    color= "green"
)

for x, y in zip(np.arange(len(df.columns)) + 1,
                pca.explained_variance_ratio_):
    label = round(y, 2)
    ax.annotate(
        label,
        (x,y),
        textcoords="offset points",
        xytext=(0,10),
        ha='center'
    )

ax.set_xticks(np.arange(pca.n_components_) + 1)
ax.set_ylim(0, 1.1)
ax.set_title('PCA Explained Variance Ratio')
ax.set_xlabel('Principal Components')


# In[120]:


#dropping the GDP per capita column from the independent variables and assigning it as the target variables
X1 = SSA_df_normalised.drop(columns=['GDP_$_per_capita'])
y1 = pd.DataFrame(SSA_df_normalised['GDP_$_per_capita'])


# In[121]:


#Backward elimination code below iterates through the predictors until only the significant variables are chosen
warnings.simplefilter(action='ignore', category=FutureWarning)

cols = list(X1)
pmax = 1
while (len(cols)>0):
    p = []
    X_1 = X1[cols]
    X_1 = sm.add_constant(X_1)
    model = sm.OLS(y1,X_1).fit()
    p = pd.Series(model.pvalues.values[1:],index = cols)
    pmax = max(p)
    feature_with_p_max = p.idxmax()
    if(pmax>0.05):
        cols.remove(feature_with_p_max)
    else:
        break
selected_features_BE = cols
print(selected_features_BE)


# In[122]:


#identifying the details of the featues identified as the most important
x1 = X1.filter(['Population', 'Area_Sq_m', 'Pop. Density_per_sq_m', 'Infant_mortality_per_1000_births', 'Climate', 'Birthrate', 'Deathrate', 'Industry'])
x1.head()


# In[123]:


#creating a dataframe with only the most important features
SSA_df2 = x1.join(y1)
SSA_df2.head()


# **Section 5.2 observations summary:**
# 
# 
# ---
# 
# 
# 
# *   The above section was aimed at selecting the most important features in the SSA data. The PCA confirmed that some components are more significant than others and I paired this with the backward elimination process which helped me to refine the features further and pinpoint exactly what they were.
# *   The backward elimination process selects a P-value level of 0.05, fits the model with all features, identifies features with the highest P-value,
# removes the feature with highest P-value, fits the model again and repeats the Backward Elimination until we remove all features with p-value higher the significance level. Optimal features were identified as population, area, population density, infant mortality, climate, birthrate, deathrate and industry.
# 
# 
# 
# 
# 
# 
# 
#   
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# ---
# 
# 

# ##  **5.3) Modelling the SSA data**
# 
# I proceed to use the Random Forest and the Linear Regression models to model the key aforementioned features of the smaller Sub Saharan Africa region against my target variable which is the GDP per Capita variable. In this section, I also apply the XGBoost model for a further inspection of how accurate the predictions focusing on this one region will be to allow for a comparative analysis of the model performances.

# ##**5.3.1) Optimised Random Forest Model**
# 
# 
# 
# 

# In[124]:


#assigning the train and test samples of the data
train, test = train_test_split(SSA_df2, test_size=0.2, shuffle=True)
training_features = ['Population', 'Area_Sq_m', 'Pop. Density_per_sq_m', 'Infant_mortality_per_1000_births', 'Climate', 'Birthrate', 'Deathrate', 'Industry']
target = 'GDP_$_per_capita'
train_X = train[training_features]
train_Y = train[target]
test_X = test[training_features]
test_Y = test[target]


# In[125]:


#Create the Random Forest Regressor
rf = RandomForestRegressor(random_state=42)

# Define the parameter grid to search through
param_grid = {
    'n_estimators': [50, 100, 150],
    'max_depth': [6, 8, 10],
    'min_weight_fraction_leaf': [0.01, 0.05, 0.1],
    'max_features': [0.7, 0.8, 0.9]
}

# Create the GridSearchCV object
grid_search = GridSearchCV(estimator=rf, param_grid=param_grid, cv=5, scoring='neg_mean_squared_error', n_jobs=-1)

# Fit the grid search to the data
grid_search.fit(train_X, train_Y)

# Get the best parameters
best_params = grid_search.best_params_

# Initialize the model with the best parameters
best_rf = RandomForestRegressor(random_state=42, **best_params)

# Fit the model with the best parameters
best_rf.fit(train_X, train_Y)

# Make predictions on train and test sets
train_pred_Y = best_rf.predict(train_X)
test_pred_Y = best_rf.predict(test_X)

# Calculate evaluation metrics
rmse_train = np.sqrt(mean_squared_error(train_pred_Y, train_Y))
mae_train = mean_absolute_error(train_pred_Y, train_Y)
rmse_test = np.sqrt(mean_squared_error(test_pred_Y, test_Y))
mae_test = mean_absolute_error(test_pred_Y, test_Y)
r2_train = r2_score(train_Y, train_pred_Y)
r2_test = r2_score(test_Y, test_pred_Y)

# Print the evaluation metrics
print('Best Parameters:', best_params)
print('RMSE Train:', rmse_train, 'MAE Train:', mae_train, 'R-squared Train:', r2_train)
print('RMSE Test:', rmse_test, 'MAE Test:', mae_test, 'R-squared Test:', r2_test)


# **Section 5.3.1 observations summary:**
# 
# ---
# 
#   
# 
# *  As compared to the random forest modelling I had applied to all countries in the dataset before, the output of the Random Forest model applied to the Sub Saharan Africa region is quite impressive showing a relatively small difference between the predicted and actual values. By narrowing down to the SSA region, I gained a better understanding of the characteristics of the data that are most relevant to Kenya and reduces the amount of noise and hude variations between the high and lower ranked countries that may have skewed the output in the previous section 4.3.
# 
# 
# 
# 
# 
# 
# 
# 
# 
# ---
# 
# 

# ##**5.3.2) Optimised XGBoost Model**

# In[126]:


# Define the parameter grid to search through
param_grid = {
    'n_estimators': [50, 100, 150],
    'max_depth': [6, 8, 10],
    'learning_rate': [0.1, 0.01, 0.001],
    'subsample': [0.7, 0.8, 0.9]
}

# Initialize the XGBoost Regressor
xgb_model = xgb.XGBRegressor(random_state=42)

# Create the GridSearchCV object
grid_search = GridSearchCV(estimator=xgb_model, param_grid=param_grid, cv=5, scoring='neg_mean_squared_error', n_jobs=-1)

# Fit the grid search to the data
grid_search.fit(train_X, train_Y)

# Get the best parameters
best_params = grid_search.best_params_

# Initialize the model with the best parameters
best_xgb = xgb.XGBRegressor(random_state=42, **best_params)

# Fit the model with the best parameters
best_xgb.fit(train_X, train_Y)

# Make predictions on train and test sets
train_pred_Y_xgb = best_xgb.predict(train_X)
test_pred_Y_xgb = best_xgb.predict(test_X)

# Calculate evaluation metrics
rmse_train_xgb = np.sqrt(mean_squared_error(train_pred_Y_xgb, train_Y))
mae_train_xgb = mean_absolute_error(train_pred_Y_xgb, train_Y)
rmse_test_xgb = np.sqrt(mean_squared_error(test_pred_Y_xgb, test_Y))
mae_test_xgb = mean_absolute_error(test_pred_Y_xgb, test_Y)
r2_train_xgb = r2_score(train_Y, train_pred_Y_xgb)
r2_test_xgb = r2_score(test_Y, test_pred_Y_xgb)

# Print the evaluation metrics
print('Best Parameters:', best_params)
print('RMSE Train:', rmse_train_xgb, 'MAE Train:', mae_train_xgb, 'R-squared Train:', r2_train_xgb)
print('RMSE Test:', rmse_test_xgb, 'MAE Test:', mae_test_xgb, 'R-squared Test:', r2_test_xgb)


# ##**5.3.3) Linear Regression Model**
# 
# 
# 
# 

# In[127]:


# Train a Linear Regression model
ml = LinearRegression()
ml.fit(train_X, train_Y)

# Make predictions on train and test sets
train_pred_Y_linear = ml.predict(train_X)
test_pred_Y_linear = ml.predict(test_X)

# Calculate evaluation metrics for Linear Regression
rmse_train_linear = np.sqrt(mean_squared_error(train_Y, train_pred_Y_linear))
mae_train_linear = mean_absolute_error(train_Y, train_pred_Y_linear)
r2_train_linear = r2_score(train_Y, train_pred_Y_linear)

rmse_test_linear = np.sqrt(mean_squared_error(test_Y, test_pred_Y_linear))
mae_test_linear = mean_absolute_error(test_Y, test_pred_Y_linear)
r2_test_linear = r2_score(test_Y, test_pred_Y_linear)

# Print the evaluation metrics for Linear Regression
print('Linear Regression:')
print('RMSE Train:', rmse_train_linear, 'MAE Train:', mae_train_linear, 'R-squared Train:', r2_train_linear)
print('RMSE Test:', rmse_test_linear, 'MAE Test:', mae_test_linear, 'R-squared Test:', r2_test_linear)

# Make predictions using x1 (or any other set of features)
predicted_gdp = ml.predict(x1)

# Print or view the predicted GDP values
print("\nPredicted GDP values using the Linear Regression model:")
print(predicted_gdp)


# In[128]:


#creating a dataframe of the actual vs the predicted gdp per capita
predicted = pd.DataFrame(predicted_gdp, columns=['Predicted_GDP_per_Capita'])
country = predicted.assign(Country = SSA_df['Country'].values)
summary = country.assign(Actual_GDP_per_Capita = SSA_df_normalised['GDP_$_per_capita'].values)
summary = summary[['Country', 'Actual_GDP_per_Capita', 'Predicted_GDP_per_Capita']]
summary.head()


# In[129]:


#plotting the model predictions
plt.figure(figsize=(20,10))
plt.plot(summary['Country'], summary['Actual_GDP_per_Capita'], color='blue')
plt.plot(summary['Country'], summary['Predicted_GDP_per_Capita'], color='green')
plt.title('Actual vs Predicted Values')
plt.xlabel('Country')
plt.ylabel('Values')
plt.legend(['Actual_GDP_per_Capita','Predicted_GDP_per_Capita'])
plt.xticks(rotation=90)
plt.show()


# **Section 5.3.2 observations summary:**
# 
# ---
# 
#   
# 
# *  The visual above confirms that as compared to the modelling applied for all countries, the predictions of the  SSA model are largely accurate. Granted, there are 6 countries where the predicted values differed considerably form the predicted values. With a further investigation of the features most highly correlated values with their GDP per capita it is likely that a different mix of factors specific to these countries may be optimal. However, the predictions for majority of the countries are accurate and I am comfortable to proceed with the model.
# 
# 
# 
# 
# 
# 
# 
# 
# ---
# 
# 

# 
# 
#  **CONCLUSION**
# 
# 
# ---
# 
# 
# 
# 
# The project has confirmed that machine learning can be used to investigate the patterns in the factors that affect GDP per capita for different countries and to develop a model that can predict the GDP when the most critical of these these factors are used as inputs. All the objective questions have been answered and explained in the respective sections observation summary notes. The project denotes the importance of diving deeper into the GDP specificities for countries per region for better model outcomes instead of analysing GDP globally. The model can aid in scenario planning, risk assessment, and providing a directional understanding of potential economic trajectories. It offers valuable guidance for long-term planning and strategy formulation for various sectors.
# 
# 
# 
# 
# 
# 
# 
# 
# ---
#  **-> Benefits**
# 
# 
# 
# *  With information on the key variables for a certain year, one can use them as inputs and use the model to get a prediction of the year's GDP per capita. Based on how high or low the prediction is, it will be easier to take a deeper dive into the specific variables that need more research and investigation in order to influence the desired outcome.
# *   If you want to compare the GDP per Capita for select countries or regions, the PCA and feature selection section also allows you to pinpoint the different variables you need to focus on that cause variations per region.
# 
# *   In Kenya, economic development often tends to be politicised and this project allows for the use of data to contribute to these discussion and to shed light on the major geo-economic factors that need our attention, analysis and further investment in order to also be among the top in Africa.
# 
# 
# 
# ---
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
