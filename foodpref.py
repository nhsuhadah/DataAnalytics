# -*- coding: utf-8 -*-
"""foodpref.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KKKetozHHyWDF502hdzQyweY2h6XkXi8

**Data Cleaning/pre-processing**
"""

import pandas as pd
import numpy as np

df = pd.read_csv('Food_Preference.csv')
df.head()

df = df.drop(['Timestamp', 'Participant_ID'], axis = 1)

df = df.dropna(axis = 0, how ='any')

df['Nationality'] = df['Nationality'].replace(['Indonesia','Indonesain'],'Indonesian')

df['Nationality'] = df['Nationality'].replace(['MY','Malaysia', 'Malaysian', 'MALAYSIAN'],'Malaysian')

df['Nationality'] = df['Nationality'].replace(['Pakistani','Pakistan'],'Pakistani')

df['Nationality'].unique()

df.info()
df.describe(include='all')

# !pip install plotly
# !pip install cufflinks

# !pip install streamlit
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import plotly.express as px

st.title("Food Preference✨")

st.markdown("""
* **Data Source:** [Food-preferences.kaggle](https://www.kaggle.com/adrianmcmahon/food-preferences-of-india/data)
""" )
img = Image.open("pic.jpg")
st.image(img)

df = pd.read_csv('Food_Preference.csv')
df = df.drop(['Timestamp', 'Participant_ID'], axis = 1)
df = df.dropna(axis = 0, how ='any')
df['Nationality'] = df['Nationality'].replace(['Indonesia','Indonesain'],'Indonesian')
df['Nationality'] = df['Nationality'].replace(['MY','Malaysia', 'Malaysian', 'MALAYSIAN'],'Malaysian')
df['Nationality'] = df['Nationality'].replace(['Pakistani','Pakistan'],'Pakistani')



#Nationality
option = st.sidebar.selectbox(
    'Select Nationality',
     ['Indian'])

if option=='Indian':
    rslt_df = df.loc[df['Nationality'] == 'Indian']

# Select Gender
option = st.sidebar.selectbox(
    'Select Gender',
     ['Male', 'Female'])

if option=='Male':
    rslt_df_1 = rslt_df.loc[rslt_df['Gender'] == 'Male']
else:
    rslt_df_1 = rslt_df.loc[rslt_df['Gender'] == 'Female']

st.dataframe(rslt_df_1)

# Select food
# options = st.sidebar.selectbox(
#      'Food Preference',
#      ['Traditional food', 'Western Food'])

# if option=='Male':
#     rslt_df_2 = rslt_df_1.loc[rslt_df['Food'] == 'Traditional food']
#     st.dataframe(rslt_df_2)
# else:
#     rslt_df_2 = rslt_df_1.loc[rslt_df['Food'] == 'Western Food']
#     st.dataframe(rslt_df_2)

#Select 
numeric_columns = list(df.select_dtypes(['float','int']).columns)
chart_select = st.sidebar.selectbox(
     label = "Select the Chart type",
     options = ['Scatterplots'])

if chart_select == 'Scatterplots':
  st.sidebar.subheader("Scatterplot Settings")
  x_values = st.sidebar.selectbox('X axis', options=['Food','Juice','Dessert'])
  y_values = st.sidebar.selectbox('Y axis', options=numeric_columns)
  plot = px.scatter(data_frame = df, x=x_values, y=y_values)
  st.plotly_chart(plot)