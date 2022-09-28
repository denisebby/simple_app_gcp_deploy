import dash
from dash import dcc, html
from dash.dependencies import Output, Input, State
import plotly.express as px
import dash_bootstrap_components as dbc

import pandas as pd
import os

# Define app
# VAPOR, LUX, QUARTZ
# external_stylesheets=[dbc.themes.QUARTZ]
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], meta_tags=[{'name': 'viewport','content': 'width=device-width, initial-scale=1.0'}])
app.title = "Filler title"
server = app.server

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

navbar = dbc.NavbarSimple(
    brand="An app deployed on gcp",
    brand_href="#",
    color="black",
    dark=True,
    id = "navbar-example-update"
)

app.layout = html.Div(children=[
    navbar,

    dbc.Container([
        html.H1(children='Hello Dash'),

        html.Div(children='''
            Dash: A web application framework for your data.
        '''),

        dcc.Graph(
            id='example-graph',
            figure=fig
        ),

        dcc.Input(
            id="input_text",
            type= "text",
            placeholder="Input Here",
        ),
        html.Div(id="output_text")
        
        ],

        style = {"margin-top": "5%", "margin-bottom": "5%"}
    )
])

##################### CALLBACKS ################################
@app.callback(
    Output("output_text", "children"),
    [Input("input_text", "value")],
)
def cb_render(val):
    return val

if __name__=='__main__':
    # app.run_server(debug=False, port=8005)
    app.run_server(debug=False, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))