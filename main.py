#!/usr/bin/env python3

import figure

import dash
import dash_html_components as html
import dash_core_components as dcc

def main():
    # LOAD FILE ONCE
    figure.load_geojson("data/COMMERCES.geojson")
    # START SERVER
    start_server()

def start_server():
    # INPUT SECTION
    inputSection = [
        dcc.Checklist(
            id='heatmap-input',
            options=[
                {'label':'Heatmap', 'value': 'Heatmap'},
            ]
        ),
        dcc.Input(id='input-on-submit', value='Monoprix', type="text"),
        html.Button('Click Me', id='submit-val', n_clicks=0)
    ]

    # MAP SECTION
    mapSection = dcc.Graph(id='output-iframe', style=styleMap)

    # DASH
    app = dash.Dash(__name__)
    app.layout = html.Div([
        html.Div(inputSection, style = styleInputDiv),
        html.Div(mapSection, style = styleMapDiv)
    ], style = styleContainer)

    # CALLBACKS
    @app.callback(
        dash.dependencies.Output('output-iframe', 'figure'),
        [dash.dependencies.Input('submit-val', 'n_clicks')],
        [dash.dependencies.State('input-on-submit', 'value')])
    def update_output(n_clicks, value):
        return figure.get_figure([value])

    # RUN SERVER
    app.run_server(debug=False, port=8052)

styleContainer = {
    'width': '100vw',
    'height': '100vh',
    'backgroundColor': 'green',
    'padding': '0px',
    'flex-direction': 'column',
    'display': 'flex'
}

styleInputDiv = {
    'backgroundColor': 'red',
    'padding': '4px'
}

styleMapDiv = {
    'backgroundColor': 'yellow',
    'padding': '4px',
    'flex': '1'
}

styleMap = {
    'height': '100%',
    'width': '100%'
}

if __name__ == "__main__":
    main()
