#!/usr/bin/env python
# coding: utf-8

# In[1]:


import plotly.graph_objects as go


# In[8]:


import pandas as pd 
df = pd.read_csv('data/us_ag_data.csv')


# In[5]:


fig = go.Figure(data=go.Choropleth(
    locations=df['code'], # Spatial coordinates
    z = df['total exports'].astype(float), # Data to be color-coded
    locationmode = 'USA-states', # set of locations match entries in `locations`
    colorscale = 'Reds',
    colorbar_title = "Millions USD",
))


# In[6]:


fig.update_layout(
    title_text = 'US Agriculture Exports by State',
    geo_scope='usa', # limite map scope to USA
)

fig.show()

