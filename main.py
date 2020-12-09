#!/usr/bin/env python3
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
import geopandas as gpd

# LOAD DATA
df_places = gpd.read_file("./data/COMMERCES.geojson")
lon = []
lat = []
for i in df_places["geometry"]:
    lon.append(i.x)
    lat.append(i.y)

# CREATE FIGURE
fig = px.scatter_mapbox(df_places, lon=lon, lat=lat, hover_name="LIBACT")

# LAYOUT (background, margins)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

# TRACES (markers)
fig.update_traces(marker=dict(size=8), selector=dict(mode='markers'))

# SHOW
fig.show()

"""
fig = px.density_mapbox(df_places, lon=lon, lat=lat, hover_name="LIBACT", radius=10, \
                        center=dict(lat=0, lon=180), zoom=0, \
                        mapbox_style="stamen-terrain")


def getArray(n):
    arr = []
    for i in range(0, n):
        arr.append(False)
    arr.append(True)
    for i in range(n, 10000):
        arr.append(False)
    return arr

# BUTTONS
fig.update_layout(
    updatemenus = [
        dict(
            type = "buttons",
            direction = "left",
            buttons=list([
                dict(
                    method='restyle',
                    label="Fabrication et vente d'instruments de musique",
                    args=[{"visible": getArray(76)}]
                ),
                dict(
                    method='restyle',
                    label="Restaurant asiatique",
                    args=[{"visible": getArray(45)}]
                ),
                dict(
                    method='restyle',
                    label='None',
                    args=[{'visible': getArray(56)}]
                )
            ]),
        )
    ]
)"""
