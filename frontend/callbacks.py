import dash_html_components as html
from dash.dependencies import Input, Output

from .geometry import geometry_components
from .bridle import bridle_components
from .fly import fly_components

from app import app


@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_inputs(tab):
    if tab == 'geometry':
        return html.Div([
            html.H3('Geometry'),
            geometry_components
        ])
    elif tab == 'bridle':
        return html.Div([
            html.H3('Bridle'),
            bridle_components
        ])
    elif tab == 'fly':
        return html.Div([
            html.H3('Fly'),
            fly_components
        ])
