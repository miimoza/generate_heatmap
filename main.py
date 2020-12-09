#!/usr/bin/env python3
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
import geopandas as gpd

df_places = gpd.read_file("./data/all.geojson")

lon = []
lat = []

for i in df_places["geometry"]:
    lon.append(i.x)
    lat.append(i.y)

fig = px.scatter_mapbox(df_places, lon=lon, lat=lat, hover_name="LIBACT")
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.update_traces(marker=dict(size=12), selector=dict(mode='markers'))

fig.show()
