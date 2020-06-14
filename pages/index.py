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
        
            #### **🛩 HOW ARE AIRLINE FLIGHT PRICES CALCULATED?**

            Have you ever bought a plane ticket to get you from point A-to-B, and then wondered why you've been charged that price?
            
            Unless you use a ticket price comparison platform, you're usually stuck paying the magic number that's calculated when you select your flight specifications.
            
            After interactively experimenting with my flight price predictor web app, hopefully you'll more clearly understand how flight pricing works.

            """
        ),
        dcc.Link(dbc.Button("PREDICT THE PRICE FOR YOUR NEXT FLIGHT  ➡️", color='primary'), href='/predictions'),
        html.Br(),
        html.Br(),
        dcc.Link(dbc.Button('VIEW PREDICTIVE MODELING PROCESS ➡️', color='primary'), href='/process'),
        html.Br(),
        html.Br(),
        dcc.Markdown("""Go back to [Ryan Zernach](http://ryan.zernach.com/2019/11/01/how-are-airline-flight-prices-calculated/)'s Portfolio Page""")
    ],
    md=6,
)

gapminder = px.data.gapminder()
fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
           hover_name="country", log_x=True, size_max=60)


column2 = dbc.Col(
    [
        #dcc.Graph(figure=fig)
        html.Img(src='assets/Airline Price Predicitons -- By Ryan Zernach -- Ryan.Zernach.com Zernach.com Data Science Predictive Modeling.png', className='img-fluid', height=550, width=550)
    ]
)

layout = dbc.Row([column2, column1])