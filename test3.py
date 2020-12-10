#!/usr/bin/env python3

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
import geopandas as gpd
import libact_selector
import representation_toggle
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import time


def figures_to_html(figs, filename):
    '''Saves a list of plotly figures in an html file.

    Parameters
    ----------
    figs : list[plotly.graph_objects.Figure]
        List of plotly figures to be saved.

    filename : str
        File name to save in.

    '''
    import plotly.offline as pyo

    dashboard = open(filename, 'w')
    dashboard.write("<html><head></head><body>" + "\n")

    add_js = True
    for fig in figs:

        inner_html = pyo.plot(
            fig, include_plotlyjs=add_js, output_type='div'
        )

        dashboard.write(inner_html)
        add_js = False

    dashboard.write("</body></html>" + "\n")

def load_data(path):
    df_places = gpd.read_file(path)
    #df_places = df_places[df_places.LIBACT == "Achat - Vente d'or"]
    df_places = df_places.query("LIBACT != 'Locaux Vacants' and\
                             LIBACT != 'Locaux en travaux' and\
                             LIBACT != 'Bureau en boutique'")
    return df_places

def get_coord(df):
    lon = []
    lat = []
    for i in df["geometry"]:
        lon.append(i.x)
        lat.append(i.y)

    return lon, lat


df_places = load_data("data/COMMERCE_ALIMENTAIRE.geojson")
libact_list = set(df_places["LIBACT"])
lon, lat = get_coord(df_places)

print(df_places)
#df_places = df_places[df_places.LIBACT == "Achat - Vente d'or"]
# CREATE FIGURE

fig1 = px.density_mapbox(df_places, lon=lon, lat=lat, hover_name="LIBACT", \
                        radius=4, center=dict(lat=48.86, lon=2.35), zoom=12.2)
fig2 = px.scatter_mapbox(df_places, lon=lon, lat=lat, hover_name="LIBACT", \
                        center=dict(lat=48.86, lon=2.35), zoom=12.2)




figures_to_html([fig1, fig2], "caca.html")