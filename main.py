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
    with open('data/libact_list') as f:
        libact_list = f.read().splitlines()

    # INPUT SECTION
    headerSection = [
        html.H1("Cluster Paris"),
        dcc.Dropdown(
            id='display-selector',
            options=[
                {'label': 'Heat map', 'value': 'heatmap'},
                {'label': 'Points', 'value': 'plots'},
            ],
            value='heatmap',
            searchable=False,
            clearable=False,
            style=styleDisplaySelector
        )  
    ]

    inputSection = [
        dcc.Checklist(
            id='libact-checklist',
            options=[
                {'label': libact, 'value': libact} for libact in libact_list
            ],
            style=styleInput
        ),
        html.Button('Actualiser', id='submit-button', n_clicks=0)
    ]

    # MAP SECTION
    mapSection = dcc.Graph(id='output-graph', style=styleMap)

    # DASH
    app = dash.Dash(__name__)
    app.layout = html.Div([
        html.Div(headerSection, style = styleHeaderDiv),
        html.Div([
            html.Div(mapSection, style = styleMapDiv),
            html.Div(inputSection, style = styleInputDiv)
        ], style = styleMainSection)

    ], style = styleContainer)

    # CALLBACKS
    @app.callback(
        dash.dependencies.Output('output-graph', 'figure'),
        [dash.dependencies.Input('submit-button', 'n_clicks'), dash.dependencies.Input('display-selector', 'value')],
        [
            dash.dependencies.State('libact-checklist', 'value')
            
        ]
    )
    def update_output(n_clicks, display_type, libact_list):
        return figure.get_figure(libact_list, display_type)

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

styleHeaderDiv = {
    'backgroundColor': 'red',
    'padding': '4px',
    'font-size' : '12px'
}

styleDisplaySelector = {
    'width': '25%'
}

styleMainSection = {
    'overflow': 'hidden',
    'backgroundColor': 'lime',
    'flex': '1',
    'flex-direction': 'row',
    'display': 'flex'
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

styleInputDiv = {
    'backgroundColor': 'purple',
    'flex-direction': 'column',
    'display': 'flex'
}

styleInput = {
    'backgroundColor': 'orange',
    'overflow-y': 'scroll',
    'flex-direction': 'column',
    'display': 'flex'
}

if __name__ == "__main__":
    main()
