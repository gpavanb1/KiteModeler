import dash_core_components as dcc
import dash_html_components as html

import frontend.callbacks

from app import app


app.layout = html.Div([
    html.H1(id='heading', children='Kite Modeler - Reboot'),
    dcc.Tabs(id='tabs', value='geometry', children=[
        dcc.Tab(label='Geometry', value='geometry'),
        dcc.Tab(label='Bridle', value='bridle'),
        dcc.Tab(label='Fly', value='fly')
    ]),
    html.Div(id='tabs-content')
])


if __name__ == '__main__':
    app.run_server(debug=True)
