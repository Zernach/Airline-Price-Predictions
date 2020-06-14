# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Visualizations

            Insights sample testing text


            """
        ),
        html.Img(src='assets/Which factors have the most influence on the price of a plane ticket Ryan Zernach Zernach.com.png', className='img-fluid'),
        dcc.Markdown(
            """

            """
        ),
        html.Img(src='assets/Partial-Dependence-Plot-Airplane-Flight-Prices-DIstance-Traveled-Miles-Rises-Price-Rises-Number-Tickets-Ordered-Rises-Price-Drops-Ryan-Zernach-Zernach.com_.png', className='img-fluid')
        
    ],
)

layout = dbc.Row([column1])