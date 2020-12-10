#!/usr/bin/env python3

import figure

import dash
import plotly.offline as pyo
import dash_html_components as html
import dash_core_components as dcc

def main():
    start_server()


def libact_to_html_figure(libacts):

    fig = figure.get_figure(libacts)

    frame_html = "<html><head></head><body>" + "\n"
    add_js = True

    inner_html = pyo.plot(
        fig, include_plotlyjs=add_js, output_type='div'
    )

    frame_html += inner_html
    
    add_js = False
    frame_html += "</body></html>" + "\n"
    return frame_html

def start_server():
    # SERVER AND CALLBACK
    app = dash.Dash()
    app.layout = html.Div([
        dcc.Input(id='input-on-submit', value='initial value', type="text"),
        html.Button('Click Me', id='submit-val', n_clicks=0),
        html.Div(html.Iframe(id='output-iframe', srcDoc="Loading..."),
            style = {'weight': '100%', 'height': '100%'}),
        html.Div(id='container-button-basic',
             children='Enter a value and press submit')
    ], style = {'weight': '100%', 'height': '100%', 'overflow': 'hidden'})

    @app.callback(
        dash.dependencies.Output('output-iframe', 'srcDoc'),
        [dash.dependencies.Input('submit-val', 'n_clicks')],
        [dash.dependencies.State('input-on-submit', 'value')])
    def update_output(n_clicks, value):
        return libact_to_html_figure([value])

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
