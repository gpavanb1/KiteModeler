import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from frontend.geometry import geometry_components


app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1(id='heading', children='Kite Modeler'),
    dcc.Tabs(id='tabs', value='geometry', children=[
        dcc.Tab(label='Geometry', value='geometry'),
        dcc.Tab(label='Bridle', value='bridle'),
        dcc.Tab(label='Fly', value='fly')
    ]),
    html.Div(id='tabs-content')
])


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
            html.H3('Bridle')
        ])
    elif tab == 'fly':
        return html.Div([
            html.H3('Fly')
        ])


if __name__ == '__main__':
    app.run_server(debug=True)