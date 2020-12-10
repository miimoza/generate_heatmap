#!/usr/bin/env python3
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
import geopandas as gpd
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import time

def get_figure(libact_list, heatmap=True):
    df_places = load_data(libact_list)
    
    lon, lat = get_coord(df_places)

    if heatmap:
        fig = px.density_mapbox(df_places, lon=lon, lat=lat, hover_name="LIBACT", \
                            radius=8, center=dict(lat=48.86, lon=2.35), zoom=12.2)
    else:
        fig = px.scatter_mapbox(df_places, lon=lon, lat=lat, hover_name="LIBACT", \
                            center=dict(lat=48.86, lon=2.35), zoom=12.2)
    

    # TRACES (markers)
    fig.update_traces(marker=dict(size=8), selector=dict(mode='markers'))

    # LAYOUT (background, margins)
    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    # RETURN
    return fig

def load_geojson(path):
    global geo_panda
    geo_panda = gpd.read_file(path)

def load_data(libact_list):
    df_places = geo_panda.copy(deep=True)

    df_places = df_places.query("LIBACT != 'Locaux Vacants' and\
                             LIBACT != 'Locaux en travaux' and\
                             LIBACT != 'Bureau en boutique'")

    
    df_final = []
    for libact in libact_list:
        df_final.append(df_places[df_places.LIBACT == libact])

    # merge all mdr

    return df_final[0]

def get_coord(df):
    lon = []
    lat = []
    for i in df["geometry"]:
        lon.append(i.x)
        lat.append(i.y)

    return lon, lat

