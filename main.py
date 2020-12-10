#!/usr/bin/env python3

import figure


def main():
    figs = []
    figs.append(figure.get_figure(["Alimentation générale  <120m²"]))
    figs.append(figure.get_figure(["Alimentation générale de luxe > 300 m²"], False))

    figures_to_html(figs, "index.html")

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


if __name__ == "__main__":
    main()
