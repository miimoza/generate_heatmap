import plotly.express as px
import plotly.graph_objects as go
import plotly
df = px.data.tips()

fig = px.scatter(df, x="total_bill", y="tip", color="sex")
fig.add_trace(px.scatter(df, x="total_bill", y="tip", color="smoker").data[0])
fig.add_trace(px.scatter(df, x="total_bill", y="tip", color="smoker").data[1])


updatemenus=[dict(type = "buttons", direction = "left",
             buttons=list([
             dict(args=[{'visible': [True  , True  , False , False ]} ,],
                  label = "sex"   , method="update"),

             dict(args=[{'visible': [False , False , True  , True  ]} ,],
                  label = "smoker", method="update")
             ])),]

fig.update_layout(updatemenus = updatemenus,
                  legend_title_text='')

fig.show()
