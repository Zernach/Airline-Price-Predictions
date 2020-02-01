# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app, server
from pages import index, browsing_history

# Navbar docs: https://dash-bootstrap-components.opensource.faculty.ai/l/components/navbar
navbar = dbc.NavbarSimple(
    brand='ARCHLIFE INDUSTRIES',
    brand_href='/',
    children=[
        dbc.NavItem(dcc.Link('BROWSING HISTORY', href='/browsing_history', className='nav-link')),
    ],
    sticky='top',
    color='primary',
    light=False,
    dark=True
)

footer = dbc.Container(
    dbc.Row(
        dbc.Col(
            html.P(
                [
                    #html.Span('Ryan Zernach', className='mr-2'),
                    html.Img(src='assets/Archlife_Industries_Logo_Neurotechnology_Software_Company.png', className='img-fluid', height=100, width=320),
                    html.A(html.I(className='fas fa-envelope-square mr-1'), href='mailto:ryan.zernach@archlife.org'),
                    html.A(html.I(className='fab fa-github-square mr-1'), href='https://github.com/archlife-industries'),
                    html.A(html.I(className='fab fa-linkedin mr-1'), href='https://www.linkedin.com/company/archlife-industries/'),
                    html.A(html.I(className='fab fa-twitter-square mr-1'), href='https://twitter.com/archlife3')
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
    dbc.Container(id='page-content', className='mt-4'),
    html.Hr(),
    footer
])


# URL Routing for Multi-Page Apps: https://dash.plot.ly/urls
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return index.layout
    elif pathname == '/browsing_history':
        return browsing_history.layout
    else:
        return dcc.Markdown('## Page not found')

# Run app server: https://dash.plot.ly/getting-started
if __name__ == '__main__':
    app.run_server(debug=True)
