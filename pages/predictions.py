# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
from joblib import load

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout



pipeline = load('assets/pipeline.joblib')

column1 = dbc.Col(
    [
        dcc.Markdown(
            """

            # **PREDICTIONS**

            To predict the price of your airline ticket(s), simply make selections from the options below:

            """
        ),
        html.Br(),
        dcc.Markdown('##### **AIRLINE COMPANY**'),
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
            value = 4,
            className='mb-3',
            placeholder='Select your Airline Company...'
        ),
        dcc.Markdown('##### **ORIGIN CITY/AIRPORT**'),
        dcc.Dropdown(
            id='Origin',
            options = [
                {'label': 'TPA — Tampa International Airport', 'value': 0},
                {'label': 'LAX — Los Angeles International Airport', 'value': 1},
                {'label': 'JFK — John F. Kennedy International Airport', 'value': 2},
                {'label': 'ATL — Hartsfield-Jackson Atlanta International Airport', 'value': 3},
            ],
            value = 2,
            className='mb-3',
            placeholder='Select your Origin Location...'
        ),
        dcc.Markdown('##### **DESTINATION CITY/AIRPORT**'),
        dcc.Dropdown(
            id='Dest',
            options = [
                {'label': 'TPA — Tampa International Airport', 'value': 0},
                {'label': 'LAX — Los Angeles International Airport', 'value': 1},
                {'label': 'JFK — John F. Kennedy International Airport', 'value': 3},
                {'label': 'ATL — Hartsfield-Jackson Atlanta International Airport', 'value': 2},
            ],
            value = 2,
            className='mb-3',
            placeholder='Select your Destination Location...'
        ),
        dcc.Markdown('##### **MONTH OF FLIGHT**'),
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
            value = 1,
            className='mb-3',
            placeholder='Select your Month of Flight...'
        ),
        dcc.Markdown('##### **QTY OF TICKETS TO ORDER**'),
        dcc.Slider(
            id='NumTicketsOrdered',
            min=1,
            max=20,
            step=1,
            value=1,
            marks={n: str(n) for n in range(1,21,1)},
            className='mb-3',
        ),
    ],
    md=4,
)

column2 = dbc.Col(
    [
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    #html.Img(src='assets/Shapley Force Plots used for explaining decision tree outcome of individual instances -- Ryan Zernach Zernach.com -- Airline Price Predictions.png', className='img-fluid', height=500, width=750),
    html.H2('Predicted Airline Flight Price', className= 'mb-3'),
    html.Div(id='prediction-content', className='lead'),
    html.Div(id='image')
    ]
    #md=6,
)

layout = dbc.Row([column1, column2])

@app.callback(
    Output('prediction-content', 'children'),
    [Input('AirlineCompany', 'value'),
    Input('Origin', 'value'),
    Input('Dest', 'value'),
    Input('Quarter', 'value'),
    Input('NumTicketsOrdered', 'value')]
)

#predict_bundle = {'MktID': 20184210618801,
#                'Quarter': 1,
#                'Origin': 3,
#                'OriginWac': 30,
#                'Dest': 3,
#                'DestWac': 15,
#                'Miles': 1000,
#                'ContiguousUSA': 2,
#                'NumTicketsOrdered': 1,
#                'AirlineCompany': 4}

def predict(predict_bundle):

    df = pd.DataFrame(
        data=[[MktID, Quarter, Origin, OriginWac, Dest, DestWac, Miles, ContiguousUSA, NumTicketsOrdered, AirlineCompany]],
        columns=['MktID', 'Quarter', 'Origin', 'OriginWac', 'Dest', 'DestWac', 'Miles', 'ContiguousUSA', 'NumTicketsOrdered', 'AirlineCompany']
    )

    PricePerTicket = pipeline.predict(df)[0]
    return PricePerTicket
