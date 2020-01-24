from .dashboard import create
from dash.dependencies import Input, Output

from app import app
from backend.api import solve


def construct_input(args):
    inp = {
        'h1': args[0],
        'h2': args[1],
        'w1': args[2],
        't': args[3],
        'B': args[4],
        'K': args[5],
        'wind_speed': args[6],
        'altitude': args[7],
        'line_length': args[8],
        'env_name': "Earth",
        'surface': args[9],
        'frame': args[10],
        'tail': args[11],
        'line': args[12]
    }
    return inp


# Bounds for sliders
eps = 2.0
# Bridle must be greater than knot
@app.callback(Output('b', 'min'),
              [Input('k', 'value'),
               Input('h1', 'value'),
               Input('h2', 'value')])
def update_b_min(k, h1, h2):
    return max(k + eps, h1 + h2 + eps)

# Bridle must be greater than knot
@app.callback(Output('k', 'max'),
              [Input('b', 'value')])
def update_k_max(b):
    return b - eps

# Triangle inequality
@app.callback(Output('h1', 'min'),
              [Input('b', 'value'),
               Input('k', 'value'),
               Input('h2', 'value')])
def update_h1_min(b, k, h2):
    return max(eps, abs(2*k - b) - h2 + eps)

# Triangle inequality
@app.callback(Output('h2', 'min'),
              [Input('b', 'value'),
               Input('k', 'value'),
               Input('h1', 'value')])
def update_h1_min(b, k, h1):
    return max(eps, abs(2*k - b) - h1 + eps)


@app.callback(Output('dashboard-content', 'children'),
              [Input('h1', 'value'),
               Input('h2', 'value'),
               Input('w1', 'value'),
               Input('t', 'value'),
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
    out = solve(inp)
    return create(out)
