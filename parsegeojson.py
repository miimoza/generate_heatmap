#!/bin/python


import json


commerce_autre = open('data/COMMERCE_AUTRE.geojson', 'r').read()
data = json.loads(commerce_autre)

print(data['features'][0]['geometry']) #Your first point
