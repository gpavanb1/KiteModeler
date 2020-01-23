import dash_html_components as html
from dash.dependencies import Input, Output

from app import app


def construct_input(args):
    inp = {
        'h1': args[0],
        'h2': args[1],
        'w1': args[2],
        'B': args[3],
        'K': args[4],
        'wind_speed': args[5],
        'altitude': args[6],
        'line_length': args[7],
        'env_name': "Earth",
        'surface': args[8],
        'frame': args[9],
        'tail': args[10],
        'line': args[11]
    }
    return inp


@app.callback(Output('dashboard-content', 'children'),
              [Input('h1', 'value'),
               Input('h2', 'value'),
               Input('w1', 'value'),
               Input('b', 'value'),
               Input('k', 'value'),
               Input('wind_speed', 'value'),
               Input('altitude', 'value'),
               Input('line_length', 'value'),
               Input('surface', 'value'),
               Input('frame', 'value'),
               Input('tail', 'value'),
               Input('line', 'value')
               ])
def update_inputs(*args):
    inp = construct_input(args)
    return html.Div([
        html.H4(str(inp))
    ])
