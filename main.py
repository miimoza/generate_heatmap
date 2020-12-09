#!/usr/bin/env python3
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
import geopandas as gpd
import libact_selector
import representation_toggle


def main():
    df_places = load_data("data/COMMERCE_ALIMENTAIRE.geojson")
    libact_list = set(df_places["LIBACT"])

    lon, lat = get_coord(df_places)

    # CREATE FIGURE
    #fig = px.scatter_mapbox(df_places, lon=lon, lat=lat, hover_name="LIBACT", \
    #                        center=dict(lat=48.86, lon=2.35), zoom=12.2)
    fig = px.density_mapbox(df_places, lon=lon, lat=lat, hover_name="LIBACT", \
                            radius=4, center=dict(lat=48.86, lon=2.35), zoom=12.2)

    # TRACES (markers)
    fig.update_traces(marker=dict(size=8), selector=dict(mode='markers'))

    # LAYOUT (background, margins)
    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    representation_toggle.add_button(fig)
    libact_selector.add_button(fig)

    # SHOW
    #fig.show(filter, validate=False)
    fig.show(auto_open=True, show_link=True)

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

if __name__ == "__main__":
    main()
