# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

# Imports from this application
from app import app, server
from pages import index, predictions, process

# Navbar docs: https://dash-bootstrap-components.opensource.faculty.ai/l/components/navbar
navbar = dbc.NavbarSimple(
    brand='🛩 AIRLINE PRICE PREDICTIONS — HOME',
    brand_href='/', 
    children=[
        dbc.NavItem(dcc.Link('PREDICTIONS', href='/predictions', className='nav-link')),
        dbc.NavItem(dcc.Link('MODELING PROCESS', href='/process', className='nav-link')), 
    ],
    sticky='top',
    color='primary', 
    light=False, 
    dark=True
)

# Footer docs:
# dbc.Container, dbc.Row, dbc.Col: https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
# html.P: https://dash.plot.ly/dash-html-components
# fa (font awesome) : https://fontawesome.com/icons/github-square?style=brands
# mr (margin right) : https://getbootstrap.com/docs/4.3/utilities/spacing/
# className='lead' : https://getbootstrap.com/docs/4.3/content/typography/#lead
footer = dbc.Container(
    dbc.Row(
        dbc.Col(
            html.P(
                [
                    #html.Span('Ryan Zernach', className='mr-2'), 
                    html.Img(src='assets/Ryan_Zernach_The_Zernach_Foundation.png', className='img-fluid', height=100, width=100),
                    html.A(html.I(className='fas fa-envelope-square mr-1'), href='mailto:ryan@zernach.com'), 
                    html.A(html.I(className='fab fa-github-square mr-1'), href='https://github.com/Zernach/Airline-Price-Predictions'), 
                    html.A(html.I(className='fab fa-linkedin mr-1'), href='https://www.linkedin.com/in/zernach/'), 
                    html.A(html.I(className='fab fa-twitter-square mr-1'), href='https://twitter.com/zernach')
                ],
                className='lead'
            )
        )
    )
)

# Layout docs:
# html.Div: https://dash.plot.ly/getting-started
# dcc.Location: https://dash.plot.ly/dash-core-components/location
# dbc.Container: https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    dbc.Container(id='page-content', className="mt-4"),
    footer
])

# URL Routing for Multi-Page Apps: https://dash.plot.ly/urls
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return index.layout
    elif pathname == '/predictions':
        return predictions.layout
    elif pathname == '/process':
        return process.layout
    else:
        return dcc.Markdown('## Page not found')

# Run app server: https://dash.plot.ly/getting-started
if __name__ == '__main__':
    app.run_server(debug=True)