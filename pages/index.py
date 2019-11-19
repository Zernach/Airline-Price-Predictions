# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## 🛩 How are airline flight prices calculated?

            Have you ever bought a plane ticket to get you from point A-to-B, and then wondered why you've been charged that price?
            
            Unless you use a ticket price comparison platform, you're usually stuck paying the magic number that's calculated when you select your flight specifications.
            
            Hopefully after interactiving with this web app and experimenting with my flight price predictor, you'll more clearly understand how flight pricing works.

            """
        ),
        dcc.Link(dbc.Button('Begin Predicting Flight Prices', color='primary'), href='/predictions')
    ],
    md=4,
)

gapminder = px.data.gapminder()
fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
           hover_name="country", log_x=True, size_max=60)

column2 = dbc.Col(
    [
        dcc.Graph(figure=fig),
    ]
)

layout = dbc.Row([column1, column2])