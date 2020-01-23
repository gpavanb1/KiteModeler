import dash_html_components as html
from dash.dependencies import Input, Output

from app import app


@app.callback(Output('dashboard-content', 'children'),
              [Input('h1', 'value'),
               Input('h2', 'value'),
               Input('w1', 'value'),
               Input('b', 'value'),
               Input('k', 'value'),
               Input('wind_speed', 'value'),
               Input('altitude', 'value'),
               Input('line_length', 'value')
               ])
def update_inputs(**kwargs):
    pass
