import dash
import dash_bootstrap_components as dbc

external_stylesheets = [
    # Bootswatch theme
    dbc.themes.CYBORG,
    # for social media icons
    'https://use.fontawesome.com/releases/v5.9.0/css/all.css'
]

meta_tags=[
    {'name': 'viewport',
    'content': 'width=device-width, initial-scale=1'}
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets, meta_tags=meta_tags)

# see https://dash.plot.ly/urls
app.config.suppress_callback_exceptions = True

# appears in browser title bar
app.title = 'Airline Price Predictions' 

server = app.server



# """
# NOTES ABOUT DASH BOOTSTRAP:

# https://github.com/facultyai/dash-bootstrap-components

# dash-bootstrap-components provides Bootstrap components.

# Plotly Dash is great! However, creating the initial layout can require a lot 
# of boilerplate. dash-bootstrap-components reduces this boilerplate by providing 
# standard layouts and high-level components.

# app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CERULEAN])

# Go to https://bootswatch.com/ to preview these Bootswatch themes:

# dbc.themes.BOOTSTRAP
# dbc.themes.CERULEAN
# dbc.themes.COSMO
# dbc.themes.CYBORG
# dbc.themes.DARKLY
# dbc.themes.FLATLY
# dbc.themes.JOURNAL
# dbc.themes.LITERA
# dbc.themes.LUMEN
# dbc.themes.LUX
# dbc.themes.MATERIA
# dbc.themes.MINTY
# dbc.themes.PULSE
# dbc.themes.SANDSTONE
# dbc.themes.SIMPLEX
# dbc.themes.SKETCHY
# dbc.themes.SLATE
# dbc.themes.SOLAR
# dbc.themes.SPACELAB
# dbc.themes.SUPERHERO
# dbc.themes.UNITED
# dbc.themes.YETI
# """