
def add_button(fig):
    ## buttons to change map representation
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
                        args=["type", "density"],
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
