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


pipeline = load('assets/pipeline.joblib')

column1 = dbc.Col(
    [
        dcc.Markdown(
            """

            #### **ARCHLIFE DASHBOARD**

            Use this dashboard to maintain a tighter connection with your browsing history.

            Conduct the deepest search of your browsing history:

            ⚙️Search by URL's

            ⚙️Search by Titles

            ⚙️Search by the text that's found within each URL of your browsing history

            """
        ),
        html.Br(),

        dcc.Dropdown(
            id      = 'Testing',
            options = [
                {'label': 'Testing', 'value': 0},
                {'label': 'Testing', 'value': 1},
                {'label': 'Testing', 'value': 2}
                ],
            value       = 2,
            className   = 'mb-3',
            placeholder = ''
        ),

        dcc.Markdown('##### **Testing**'),
        dcc.Dropdown(
            id      = 'Testing2',
            options = [
                {'label': 'Testing',     'value': 1},
                {'label': 'Testing',   'value': 2},
            ],
            value     = [1],
            multi     = True,
            className = 'mb-3',
            #placeholder='Select Preferred Feelings...'
        ),
    ],
    md = 4,
)

column2 = dbc.Col(
    [
    html.H2('Results of Search:', className = 'mb-3'),
    html.Div(id = 'prediction-content', className = 'lead'),
    html.Div(id = 'image')
    ],
    md=6
)

layout = dbc.Row([column1, column2])

@app.callback(
    Output('prediction-content', 'children')#,
    #[Input('Testing', 'value'),
    #Input('Testing2', 'value')]
)
def predict(input_type = '', input_feelings = [], input_tastes = []):

    data = [[input_type, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    # Feelings
    for feeling in input_feelings:
        data[0][feeling] = 1

    # Tastes
    for taste in input_tastes:
        data[0][taste]   = 1


    df = pd.DataFrame(
        columns = ['Type', 'Aroused', 'Creative', 'Energetic', 'Euphoric',
       'Focused', 'Giggly', 'Happy', 'Hungry', 'Relaxed', 'Sleepy',
       'Talkative', 'Tingly', 'Uplifted', 'Ammonia', 'Apple', 'Apricot',
       'Berry', 'Blueberry', 'Butter', 'Candy', 'Cheese', 'Chemical',
       'Chestnut', 'Citrus', 'Coffee', 'Diesel', 'Earthy', 'Floral', 'Fruity',
       'Grape', 'Grapefruit', 'Herbal', 'Honey', 'Lavender', 'Lemon', 'Lime',
       'Mango', 'Melon', 'Menthol', 'Mint', 'Minty', 'Nutty', 'Orange',
       'Peach', 'Pear', 'Pepper', 'Pine', 'Pineapple', 'Plum', 'Pungent',
       'Rose', 'Sage', 'Skunk', 'Sour', 'Spicy', 'Strawberry', 'Sweet',
       'Tangy', 'Tar', 'Tart', 'Tea', 'Tobacco', 'Tropical', 'Vanilla',
       'Violet', 'Wood'],
        data    = data
    )

    pipeline     = load('assets/pipeline.joblib')
    y_pred_proba = pipeline.predict_proba(df)



    output = set(zip(pipeline.predict_proba(df)[0], pipeline.classes_))
    output = sorted(output, reverse = True)[:3]


    output_useless, output = zip(*output)
    output = 1

    return str(output)
