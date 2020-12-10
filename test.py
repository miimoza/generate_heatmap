#!/bin/python
from plotly.subplots import make_subplots
import plotly.graph_objects as go

fig = make_subplots(rows=1, cols=2)

fig.add_trace(
    go.Scatter(x=[1, 2, 3], y=[4, 5, 6]),
    row=1, col=1
)

fig.add_trace(
    go.Scatter(x=[20, 30, 40], y=[50, 60, 70]),
    row=1, col=2
)

fig.update_layout(height=600, width=800, title_text="Side By Side Subplots")


fig.update_layout(
        updatemenus=[
            dict(
                type="buttons",
                direction="right",
                x=0.7,
                y=1.2,
                showactive=True,
                buttons=list(
                    [
                        dict(
                            label="Points",
                            method="update",
                            args=[
                                {"visible": [True, True]},
                                {"yaxis.title.text": "Cones Sold",},
                            ],
                        ),
                        dict(
                            label="Heatmap",
                            method="update",
                            args=[
                                {"visible": [False, False]},
                                {"yaxis.title.text": "Drinks Sold"},
                            ],
                        ),
                    ]
                ),
            )
        ]
    )


fig.show()
