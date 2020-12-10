#!/usr/bin/env python3

import figure

import dash
import plotly.offline as pyo
import dash_html_components as html
import dash_core_components as dcc

def main():
    figure.load_geojson("data/COMMERCES.geojson")
    start_server()

def libacts_to_html_figure(libacts):
    fig = figure.get_figure(libacts)
    frame_html = "<html><head></head><body>" + "\n"
    frame_html += pyo.plot(
        fig, include_plotlyjs=True, output_type='div'
    )
    frame_html += "</body></html>" + "\n"
    return frame_html

def start_server():
    app = dash.Dash()
    app.layout = html.Div([
        dcc.Checklist(
            id='heatmap-input',
            options=[
                {'label':'Heatmap', 'value': 'Heatmap'},
            ]
        ),
        dcc.Input(id='input-on-submit', value='Monoprix', type="text"),
        html.Button('Click Me', id='submit-val', n_clicks=0),
        html.Div(html.Iframe(id='output-iframe', srcDoc="Loading...", style = {'width': '100%', 'height': '100%', 'position': 'absolute'}),
            style = {'width': '100%', 'height': '100%', 'overflow': 'hidden', "backgroundColor": "yellow"}),
    ], style = {'width': '500px', 'height': '500px', 'overflow': 'hidden', "backgroundColor": "red"})

    @app.callback(
        dash.dependencies.Output('output-iframe', 'srcDoc'),
        [dash.dependencies.Input('submit-val', 'n_clicks')],
        [dash.dependencies.State('input-on-submit', 'value')])
    def update_output(n_clicks, value):
        return libacts_to_html_figure([value])

    app.run_server(port=8052)



"""
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
"""

if __name__ == "__main__":
    main()
