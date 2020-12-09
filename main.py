#!/usr/bin/env python3
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
import geopandas as gpd

# LOAD DATA
df_places = gpd.read_file("./data/COMMERCES.geojson")

#df_places = df_places[df_places.LIBACT == "Chocolaterie - Confiserie"]
#df_places = df_places[df_places.LIBACT == "Hôtel de tourisme sans étoile"]
#df_places = df_places[df_places.LIBACT != "Locaux Vacants"]
df_places = df_places.query("LIBACT != 'Locaux Vacants' and\
                             LIBACT != 'Locaux en travaux' and\
                             LIBACT != 'Bureau en boutique'")


#df_places = df_places[df_places.LIBACT == ""]
#df_places = df_places[df_places.LIBACT == ""]

#df_places = df_places[df_places.LIBACT == ""]
#df_places = df_places[df_places.LIBACT == ""]
#df_places = df_places[df_places.LIBACT == ""]
#df_places = df_places[df_places.LIBACT == ""]
#df_places = df_places[df_places.LIBACT == ""]
#df_places = df_places[df_places.LIBACT == ""]
#df_places = df_places[df_places.LIBACT == ""]
#df_places = df_places[df_places.LIBACT == ""]
#df_places = df_places[df_places.LIBACT == ""]

#df_places = df_places[df_places.LIBACT == "Restaurant indien, pakistanais et Moyen Orient"]

#df_places = df_places[df_places.LIBACT == "Produits alimentaires bio et circuits courts"]
#df_places = df_places[df_places.LIBACT == "Montres"]

#df_places = df_places.query("LIBACT == 'Chaussures Enfant' or\
#                             LIBACT == 'Chaussures Homme' or\
#                             LIBACT == 'Chaussures Femme' or \
#                             LIBACT == 'Chaussures Mixte'")

#df_places = df_places[df_places.LIBACT == "Vente de jeux vidéo (+ salle de jeux vidéos)"]
#df_places = df_places[df_places.LIBACT == "Vente et fabrication de tenues de mariées"]
#df_places = df_places[df_places.LIBACT == "Locaux Vacants"]
#df_places = df_places.query("LIBACT == 'Hôtel de tourisme avec 4 étoiles' or\
#                             LIBACT == 'Hôtel de tourisme avec 5 étoiles' or\
#                             LIBACT == 'Hôtel de tourisme - Palace'")

#df_places = df_places[df_places.LIBACT == "Vente de matériel informatique"]
#df_places = df_places[df_places.LIBACT == "Vente d'articles érotiques et sex-shop"]
#df_places = df_places[df_places.LIBACT == "Tissus - Textile - Mercerie"]
#df_places = df_places[df_places.LIBACT == "Achat - Vente d'or"]
#df_places = df_places[df_places.LIBACT == "Fabrication et vente d'instruments de musique"]
#df_places = df_places.query("LIBACT == 'Restaurant asiatique' or LIBACT == 'Traiteur asiatique'")



lon = []
lat = []
for i in df_places["geometry"]:
    lon.append(i.x)
    lat.append(i.y)




# CREATE FIGURE
#fig = px.scatter_mapbox(df_places, lon=lon, lat=lat, hover_name="LIBACT", \
#                        center=dict(lat=48.86, lon=2.35), zoom=12.2)
fig = px.density_mapbox(df_places, lon=lon, lat=lat, hover_name="LIBACT", \
                        radius=2, center=dict(lat=48.86, lon=2.35), zoom=12.2)


# LAYOUT (background, margins)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

# TRACES (markers)
fig.update_traces(marker=dict(size=8), selector=dict(mode='markers'))

#Get unique LIBACT names
libact_list = set(df_places["LIBACT"])

# BUTTON TO CHANGE MAP REPRESENTATION
fig.update_layout(
    updatemenus=[
        dict(
            type = "buttons",
            direction = "left",
            buttons=list([
                dict(
                    args=["type", "scatter"],
                    label="Points",
                    method="restyle"
                ),
                dict(
                    args=["shapes", []],
                    label="Heatmap",
                    method="restyle"
                )
            ]),
            pad={"r": 10, "t": 10},
            showactive=True,
            x=0,
            xanchor="left",
            y=1.1,
            yanchor="top"
        ),
    ]
)


"""
# FILTER
data = [dict(
  act = df_places["LIBACT"],
  transforms = [dict(
    type = 'filter',
    target = 'LIBACT',
    operation = '=',
    value = 'Tabac'
  )]
)]


layout = dict(
    title = 'Tabac'
)

filter = dict(data=data, layout=layout)
"""


# SHOW
#fig.show(filter, validate=False)
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
