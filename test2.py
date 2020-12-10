#!/bin/python


import plotly.offline as pyo
import plotly.graph_objs as go
import plotly as py
import dash 
import dash_html_components as html


fig1 = go.Scatter(y=[1,2,3])
fig2 = go.Scatter(y=[3,2,1])
plots = [fig1, fig2]


app = dash.Dash()
layout = html.Div(
        [html.Div(plots[i]) for i in range(len(plots))],
        style = {'margin-right': '0px'}
    )

app.layout = layout
app.run_server(port=8052)