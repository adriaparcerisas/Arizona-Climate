#!/usr/bin/env python
# coding: utf-8

# In[62]:


import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as md
import matplotlib.ticker as ticker
import numpy as np
import plotly.express as px
import altair as alt
from datetime import datetime
import statistics as stats
st.set_page_config(page_title="San Francisco climate", layout="wide",initial_sidebar_state="collapsed")
st.title('San Francisco climate')

# In[20]:


st.markdown('San Francisco is....')

# In[5]:


st.markdown('The intention of this analysis is to provide information about how the weather has evolved on San Francisco city in terms of precipitation, humidity, pressure etc. evolved considering metrics such as:') 
st.write('- ')
st.write('- Hourly precipitation')
st.write('- Precipitation by month')
st.write('- Hourly humidity')
st.write('- Humidity by month')
st.write('- Correlation between precipitation and humidity')
st.write('')


# In[10]:

df = pd.read_csv('sanfrancisco_climate.csv')
#df2 = pd.read_csv('girona_global_summary.csv')
#df = pd.read_csv('lakecity_global_summary.csv')

#df = df.dropna()
#df2 = df2.dropna()

df['DATE2'] = df['STATION']

i=0
if i in range(len(df['DATE2'])):
    df['DATE2'].iloc[i] = datetime.strptime(str(df['DATE2'].iloc[i]),"%Y-%m-%dT%H:%M:%S")
#i=0
#if i in range(len(df['DATE'])):
#    df2['DATE'].iloc[i] = datetime.strptime(df2['DATE'].iloc[i], '%Y-%m-%d')



# In[22]:

st.subheader('Precipitation')
st.write('The first part of this app analyzes precipitation taken place on San Francisco.')
st.write('The metrics to be analyzed from there are:')
st.write('- Daily precipitation')
st.write('- Precipitation by month')
st.write('')

import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Create figure with secondary y-axis
fig1 = make_subplots(specs=[[{"secondary_y": True}]])

fig1.add_trace(go.Bar(x=df['DATE2'],
                y=df['HourlyPrecipitation'],
                name='Precipitation',
                marker_color='rgb(163, 203, 249)'
                , yaxis='y'))

fig1.update_layout(
    title='Hourly precipitation',
    xaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)
st.plotly_chart(fig1, theme="streamlit", use_container_width=True)

i=0
if i in range(len(df['DATE2'])):
    month = df['DATE2'].iloc[i].month
    
df['MONTH2']=month

#i=0
#if i in range(len(df2['DATE'])):
#    month2=df2['DATE'].iloc[i].month
    
#df2['MONTH']=month2




st.altair_chart(alt.Chart(df[5000:9999])
    .mark_line()
    .encode(x='MONTH2:N', y='HourlyPrecipitation:Q')
    .properties(title='Distribution of precipitation by month'))


# In[65]:


st.subheader('Humidity')
st.write('The first part of this app analyzes humidity in San Francisco.')
st.write('The metrics to be analyzed from there are:')
st.write('- Daily humidity')
st.write('- Humidity by month')
st.write('')

import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Create figure with secondary y-axis
fig1 = make_subplots(specs=[[{"secondary_y": True}]])

fig1.add_trace(go.Line(x=df['DATE2'],
                y=df['HourlyRelativeHumidity'],
                name='Humidity %',
                marker_color='rgb(249, 203, 163)'
                , yaxis='y'))

fig1.update_layout(
    title='Hourly humidity',
    xaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)
st.plotly_chart(fig1, theme="streamlit", use_container_width=True)

i=0
if i in range(len(df['DATE2'])):
    month = df['DATE2'].iloc[i].month
    
df['MONTH2']=month

#i=0
#if i in range(len(df2['DATE'])):
#    month2=df2['DATE'].iloc[i].month
    
#df2['MONTH']=month2




st.altair_chart(alt.Chart(df[5000:9999])
    .mark_line()
    .encode(x='MONTH2:N', y='HourlyRelativeHumidity:Q')
    .properties(title='Distribution of humidity by month'))


# In[16]:


st.write('')
st.markdown('This app has been done by **_Adrià Parcerisas_**, a PhD Biomedical Engineer related to Machine Learning and Artificial intelligence technical projects for data analysis and research, as well as dive deep on-chain data analysis about cryptocurrency projects. You can find me on [Twitter](https://twitter.com/adriaparcerisas)')
st.write('')
st.markdown('The full sources used to develop this app can be found to the following link: [Github link](https://github.com/adriaparcerisas/College-Football-Playoff)')
st.markdown('_Powered by [Flipside Crypto](https://flipsidecrypto.xyz) and [MetricsDAO](https://metricsdao.notion.site)_')


# In[17]:





# In[ ]:




