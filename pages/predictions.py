# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Predictions

            To predict the price of your airline ticket(s), simply make selections from the options below:

            """
        ),
        dcc.Markdown('##### Airline Company'), 
        dcc.Dropdown(
            id='AirlineCompany', 
            options = [
                {'label': 'Southwest Airline Co. (WN)', 'value': 2},
                {'label': 'Delta Air Lines Inc. (DL)', 'value': 4},
                {'label': 'American Airlines Inc. (AA)', 'value': 1},
                {'label': 'United Air Lines Inc. (UA)', 'value': 5},
                {'label': 'Jetblue Airways (B6)', 'value': 7},
                {'label': 'Alaskan Airlines Inc. (AS)', 'value': 3},
                {'label': 'Spirit Airlines (NK)', 'value': 9},
                {'label': 'Allegiant Air (G4)', 'value': 8},
                {'label': 'Frontier Airlines Inc. (F9)', 'value': 6},
                {'label': 'Hawaiian Airlines Inc. (HA)', 'value': 10},
                {'label': 'Sun Country Airlines (SY)', 'value': 12},
                {'label': 'Virgin America (VX)', 'value': 11},
            ], 
            value = 'Delta Air Lines Inc. (DL)', 
            className='mb-5', 
        ), 
        dcc.Markdown('##### Origin City/Airport'), 
        dcc.Dropdown(
            id='Origin', 
            options = [
                {'label': 'TPA — Tampa International Airport', 'value': 2},
                {'label': 'TPA — Tampa International Airport', 'value': 2},
                {'label': 'TPA — Tampa International Airport', 'value': 2},
            ], 
            value = 'TPA — Tampa International Airport', 
            className='mb-5', 
        ), 
        dcc.Markdown('##### Destination City/Airport'), 
        dcc.Dropdown(
            id='Dest', 
            options = [
                {'label': 'TPA — Tampa International Airport', 'value': 2},
                {'label': 'TPA — Tampa International Airport', 'value': 2},
                {'label': 'TPA — Tampa International Airport', 'value': 2},
            ], 
            value = 'TPA — Tampa International Airport', 
            className='mb-5', 
        ), 
        dcc.Markdown('##### Month of Flight'), 
        dcc.Dropdown(
            id='Quarter', 
            options = [
                {'label': 'January', 'value': 1},
                {'label': 'February', 'value': 1},
                {'label': 'March', 'value': 1},
                {'label': 'April', 'value': 2},
                {'label': 'May', 'value': 2},
                {'label': 'June', 'value': 2},
                {'label': 'July', 'value': 3},
                {'label': 'August', 'value': 3},
                {'label': 'September', 'value': 3},
                {'label': 'October', 'value': 4},
                {'label': 'November', 'value': 4},
                {'label': 'December', 'value': 4},
            ], 
            value = 'January', 
            className='mb-5', 
        ),
        dcc.Markdown('##### Number of Tickets to Order'), 
        dcc.Slider(
            id='NumTicketsOrdered', 
            min=1, 
            max=20, 
            step=1, 
            value=1, 
            marks={n: str(n) for n in range(1,21,1)}, 
            className='mb-5', 
        ),
    ],
    md=4,
)

column2 = dbc.Col(
    [

    ]
)

layout = dbc.Row([column1, column2])