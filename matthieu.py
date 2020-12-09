from google.cloud import bigquery
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np


client = bigquery.Client()

# on recupere les coordonnees de chaque store
#le < 90 est important car certaines coordonnees sont erronnees et empêchent plot

stores_query = """
SELECT stoEan, postcode, stoAnabelKey, chainTypeKey, geoLocation.geoX, geoLocation.geoY
FROM dsfr-frxxx-frxxx-dev.PSC_referentiel.bv_store
WHERE geoLocation.geoX is not null
AND geoLocation.geoX < 90
LIMIT 10000
"""
stores = client.query(stores_query).to_dataframe()
stores.head(100)

#on l'affiche avec plotly express

fig = px.scatter_mapbox(stores, lat="geoY", lon="geoX",color="chainTypeKey", hover_data=["stoEan", "stoAnabelKey"])
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.update_traces(marker=dict(size=12), selector=dict(mode='markers'))

fig.show()
