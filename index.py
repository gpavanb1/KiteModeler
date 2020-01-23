import dash_core_components as dcc
import dash_html_components as html

import frontend.callbacks
from frontend.geometry import geometry_components
from frontend.bridle import bridle_components
from frontend.fly import fly_components
from frontend.material import material_components

from app import app


app.layout = html.Div([
    html.H1(id='heading', children='Kite Modeler - Reboot'),
    dcc.Tabs([
            dcc.Tab(label='Geometry', value='geometry', children=[html.Div([
                html.H3('Geometry'),
                geometry_components
            ])]),
            dcc.Tab(label='Bridle', value='bridle', children=[html.Div([
                html.H3('Bridle'),
                bridle_components
            ])]),
            dcc.Tab(label='Fly', value='fly', children=[html.Div([
                html.H3('Fly'),
                fly_components
            ])]),
            dcc.Tab(label='Material', value='material', children=[html.Div([
                html.H3('Material'),
                material_components
            ])])
        ], id='tabs', value='geometry'),
    html.Div(id='tabs-content'),
    html.Div(id='dashboard-content')
])


if __name__ == '__main__':
    app.run_server(debug=True)
