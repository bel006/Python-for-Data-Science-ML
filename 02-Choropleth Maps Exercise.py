#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../Pierian_Data_Logo.png' /></a>
# ___

# # Choropleth Maps Exercise 
# 
# Welcome to the Choropleth Maps Exercise! In this exercise we will give you some simple datasets and ask you to create Choropleth Maps from them. Due to the Nature of Plotly we can't show you examples
# 
# [Full Documentation Reference](https://plot.ly/python/reference/#choropleth)
# 
# ## Plotly Imports

# In[1]:


import plotly.graph_objs as go 
from plotly.offline import init_notebook_mode,iplot
init_notebook_mode(connected=True) 


# ** Import pandas and read the csv file: 2014_World_Power_Consumption**

# In[2]:


import pandas as pd


# In[3]:


df = pd.read_csv('2014_World_Power_Consumption')


# ** Check the head of the DataFrame. **

# In[4]:


df.head()


# In[62]:


# placeholder


# ** Referencing the lecture notes, create a Choropleth Plot of the Power Consumption for Countries using the data and layout dictionary. **

# In[5]:


data = dict(type = 'choropleth',
           locations = df['Country'],
           locationmode = 'country names',
           z = df['Power Consumption KWH'],
           text = df['Country'],
           colorbar = {'title':'Power Consumption KWH'})

# locationmode = 'country names' comes from documentation


# In[6]:


layout = dict(title = '2014 Power Consumption for Countries',
             geo = dict(showframe = False,
                       projection = {'type':'mercator'}))


# In[7]:


choromap = go.Figure(data = [data],layout = layout)
iplot(choromap,validate=False)


# ## USA Choropleth
# 
# ** Import the 2012_Election_Data csv file using pandas. **

# In[8]:


df2 = pd.read_csv('2012_Election_Data')


# ** Check the head of the DataFrame. **

# In[9]:


df2.head()


# In[110]:


# placeholder


# ** Now create a plot that displays the Voting-Age Population (VAP) per state. If you later want to play around with other columns, make sure you consider their data type. VAP has already been transformed to a float for you. **

# In[10]:


data = dict(type = 'choropleth',
            locations = df2['State Abv'],
            z = df2['Voting-Age Population (VAP)'],
            locationmode = 'USA-states',
            text = df2['State'],
            colorbar = {'title':'Voting-Age Population'})


# In[11]:


# shows a map of the world with just the data from USA

# layout = dict(title = '2012 Voting Age Population Per State',
#              geo = dict(showframe = False,
#                        projection = {'type':'mercator'}))

# solution

layout = dict(title = '2012 Voting Age Population Per Sate',
             geo = dict(scope='usa',showlakes=True,lakecolor='rgb(85,173,240)'))


# In[12]:


choromap = go.Figure(data = [data],layout = layout)
iplot(choromap,validate=False)


# # Great Job!
