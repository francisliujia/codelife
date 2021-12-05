#!/usr/bin/env python
# coding: utf-8

# In[130]:


import json
# just imported pandas if you want to print a dataframe use print(df) in jupyter only df works as this is the name of de variable.  
import pandas as pd
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline


# In[131]:


filename = 'all_earthquakes.json'
# I needed it to be encoded on utf-8
with open(filename,  encoding="utf8") as f:
    all_eq_data = json.load(f)


# In[132]:


all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))

title = all_eq_data['metadata']['title']

mags, lons, lats, hover_texts =[], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    title = eq_dict['properties']['title']
    
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(title)
    
# I pref data frames in pandas
df = pd.DataFrame([mags, lons, lats, hover_texts])
df = df.T
df = df.rename(columns={0: "Mag", 1: "Lon",2: "Lat", 3: "Title"})
df = df.dropna()


# In[137]:


data = [{
    'type': 'scattergeo',
    'lon': df['Lon'],
    'lat': df['Lat'],
    'text': df['Title'],
    'marker': {
        # Kept size fixed the scale of Mag does not seem to be accepted by plotly
        'size': 5,
        'color': df['Mag'],
        # Err: Invalid property specified for object of type plotly.graph_objs.scattergeo.Marker: 'colorscales' and 'reversecale'
        # Don't know why :P
        #'colorscales': 'icefire',
        #'reversecale': True,
        'colorbar': {'title': 'Magnitude'}
    },

}]
my_layout = Layout(title='past month Global Earthquakes')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='last_month_global_earthquakes.html')


# In[ ]:




