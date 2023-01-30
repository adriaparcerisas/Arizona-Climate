#!/usr/bin/env python
# coding: utf-8

# In[120]:


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


st.markdown('**San Francisco** is a North American city that ranks as the fourth most populous city in the state of California and 13th in the United States, with a population of approximately 884,382 in 2013.6 It is the only consolidated city-county in California, and with a land area of 121 km², it has the second highest population density in the country among cities with more than 200,000 inhabitants, after New York [1](https://es.wikipedia.org/wiki/San_Francisco_(California)).')

st.markdown('**San Francisco climate** is a Mediterranean climate with oceanic influences, slightly cooler than the usual California coastal climate due to large currents from the Pacific, with cool, very wet winters and mild, dry summers. Because it is surrounded on three sides by water, San Franciscos climate is strongly influenced by the cold currents of the Pacific Ocean, which tends to moderate temperature oscillations and produce a cool climate, with very little seasonal temperature variation.') 

st.markdown('The dry period, from May to October, is cool, with average maximum temperatures of 18-21 °C and minimum temperatures of 11-13 °C. The rainy period, from November to April, is cool with maximum temperatures of 14-17 °C and minimum temperatures between 8 and 10 °C. On average, temperatures exceed 22 °C on only 28 days of the year.[1](https://es.wikipedia.org/wiki/San_Francisco_(California)#cite_note-55)')

st.markdown('The combination of cool ocean water and the heat of the California peninsula creates a characteristic fog in the metropolis that can cover the western half of the metropolis throughout the day in spring and early summer. The high hills in the geographic centre of the metropolis are responsible for variations of up to 20 % in annual rainfall between different parts of the metropolis.')

st.markdown('Annual rainfall levels are around 841 mm and occur during the rainy months from November to March. On average, the city experiences 102 rainy days per year. Snow is extraordinarily rare, having been recorded only 10 times in the metropolis since 1852.')


# In[5]:


st.markdown('The intention of this analysis is to provide information about how the weather has evolved on San Francisco city in terms of precipitation, humidity, pressure etc. evolved considering metrics such as:') 
st.write('')
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
df=df.fillna(0)
#df2 = df2.dropna()
dates2=[]
month2=[]
for i in range(len(df['STATION'])):
    dates2.append(datetime.strptime(str(df['STATION'].iloc[i][:10]),"%Y-%m-%d"))
    month2.append(df['STATION'].iloc[i][5:7])
df['DATE2'] = dates2
df['MONTH2'] = month2
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

###### CALCULAR MEAN DE CADA MES I FER DF AMB MONTH I MEAN VALUE PER PLOTAR.HO


fig2 = px.histogram(df, x="MONTH2", y="HourlyPrecipitation", histfunc='avg')
fig2.update_layout(
    title='Average precipitation by month',
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
st.plotly_chart(fig2, theme="streamlit", use_container_width=True)


# In[122]:


st.subheader('Humidity')
st.write('The second part of this app analyzes humidity in San Francisco.')
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

#i=0
#if i in range(len(df2['DATE'])):
#    month2=df2['DATE'].iloc[i].month
    
#df2['MONTH']=month2

fig2 = px.histogram(df, x="MONTH2", y="HourlyRelativeHumidity", histfunc='avg', color_discrete_sequence=['yellow'])
fig2.update_layout(
    title='Average relative humidity by month',
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
st.plotly_chart(fig2, theme="streamlit", use_container_width=True)


# In[ ]:


st.subheader('Precipitation vs Humidity')
st.write('The third part of this app analyzes the correlation between precipitation and humidity in San Francisco.')
st.write('The metrics to be analyzed from there are:')
st.write('- Daily precipitation vs humidity')
st.write('- Precipitation vs humidity values')
st.write('')

import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Create figure with secondary y-axis
fig1 = make_subplots(specs=[[{"secondary_y": True}]])

fig1.add_trace(go.Bar(x=df['DATE2'],
                y=df['HourlyRelativeHumidity'],
                name='Humidity %',
                marker_color='rgb(249, 203, 163)'
                , yaxis='y'))
fig1.add_trace(go.Line(x=df['DATE2'],
                y=df['HourlyPrecipitation'],
                name='Precipitation',
                marker_color='rgb(163, 203, 249)'
                , yaxis='y'))
fig1.update_layout(
    title='Hourly precipitation and humidity',
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

#i=0
#if i in range(len(df2['DATE'])):
#    month2=df2['DATE'].iloc[i].month
    
#df2['MONTH']=month2

fig2 = px.scatter(df, x="HourlyPrecipitation", y="HourlyRelativeHumidity", color_discrete_sequence=['orange'])
fig2.update_layout(
    title='Precipitation vs Realtive Humidity',
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
st.plotly_chart(fig2, theme="streamlit", use_container_width=True)


# In[ ]:


st.subheader('Wind Speed')
st.write('The fourth part of this app analyzes Wind Speed in San Francisco.')
st.write('The metrics to be analyzed from there are:')
st.write('- Hourly Wind Speed')
st.write('- Wind Speed by month')
st.write('')

import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Create figure with secondary y-axis
fig1 = make_subplots(specs=[[{"secondary_y": True}]])

fig1.add_trace(go.Line(x=df['DATE2'],
                y=df['HourlyWindSpeed'],
                name='speed',
                marker_color='rgb(110, 203, 120)'
                , yaxis='y'))

fig1.update_layout(
    title='Hourly Wind Speed',
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

#i=0
#if i in range(len(df2['DATE'])):
#    month2=df2['DATE'].iloc[i].month
    
#df2['MONTH']=month2

fig2 = px.histogram(df, x="MONTH2", y="HourlyWindSpeed", histfunc='avg', color_discrete_sequence=['green'])
fig2.update_layout(
    title='Average Wind Speed by month',
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
st.plotly_chart(fig2, theme="streamlit", use_container_width=True)


# In[124]:


st.subheader('Precipitation vs Wind speed')
st.write('The fifth part of this app analyzes the correlation between precipitation and wind speed in San Francisco.')
st.write('The metrics to be analyzed from there are:')
st.write('- Daily precipitation vs wind speed')
st.write('- Precipitation vs wind speed values')
st.write('')

import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Create figure with secondary y-axis
fig1 = make_subplots(specs=[[{"secondary_y": True}]])

fig1.add_trace(go.Bar(x=df['DATE2'],
                y=df['HourlyWindSpeed'],
                name='speed',
                marker_color='rgb(249, 203, 163)'
                , yaxis='y'))
fig1.add_trace(go.Line(x=df['DATE2'],
                y=df['HourlyPrecipitation'],
                name='Precipitation',
                marker_color='rgb(163, 203, 249)'
                , yaxis='y'))
fig1.update_layout(
    title='Hourly precipitation and wind speed',
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

#i=0
#if i in range(len(df2['DATE'])):
#    month2=df2['DATE'].iloc[i].month
    
#df2['MONTH']=month2

fig2 = px.scatter(df, x="HourlyPrecipitation", y="HourlyWindSpeed", color_discrete_sequence=['orange'])
fig2.update_layout(
    title='Precipitation vs wind speed',
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
st.plotly_chart(fig2, theme="streamlit", use_container_width=True)


# In[ ]:


DailyCoolingDegreeDays DailyHeatingDegreeDays

st.subheader('Cooling vs Heating Degrees')
st.write('The sixth part of this app analyzes the differences between daily cooling degree days and daily heating degree days in San Francisco.')
st.write('The metrics to be analyzed from there are:')
st.write('- Daily cooling vs heating degrees')
st.write('- Cooling vs heating degrees')
st.write('')

import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Create figure with secondary y-axis
fig1 = make_subplots(specs=[[{"secondary_y": True}]])

fig1.add_trace(go.Line(x=df['DATE2'],
                y=df['DailyCoolingDegreeDays'],
                name='Cooling degrees',
                marker_color='rgb(106, 132, 238)'
                , yaxis='y'))
fig1.add_trace(go.Line(x=df['DATE2'],
                y=df['DailyHeatingDegreeDays'],
                name='Heating degrees',
                marker_color='rgb(238, 186, 106)'
                , yaxis='y'))
fig1.update_layout(
    title='Daily cooling and heating degrees',
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

#i=0
#if i in range(len(df2['DATE'])):
#    month2=df2['DATE'].iloc[i].month
    
#df2['MONTH']=month2

fig2 = px.scatter(df, x="DailyCoolingDegreeDays", y="DailyHeatingDegreeDays", color_discrete_sequence=['orange'])
fig2.update_layout(
    title='Cooling vs heating degrees',
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
st.plotly_chart(fig2, theme="streamlit", use_container_width=True)


# In[82]:


st.write('')
st.markdown('This app has been done by **_Adrià Parcerisas_**, a PhD Biomedical Engineer related to Machine Learning and Artificial intelligence technical projects for data analysis and research, as well as dive deep on-chain data analysis about cryptocurrency projects. You can find me on [Twitter](https://twitter.com/adriaparcerisas)')
st.write('')
st.markdown('The full sources used to develop this app can be found to the following link: [Github link](https://github.com/adriaparcerisas/College-Football-Playoff)')
st.markdown('_Powered by [Flipside Crypto](https://flipsidecrypto.xyz) and [MetricsDAO](https://metricsdao.notion.site)_')


# In[17]:





# In[ ]:




