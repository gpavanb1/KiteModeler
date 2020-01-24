import dash
import flask
import os
import dash_bootstrap_components as dbc

STATIC_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = 'Kite Modeler - Reboot'
server = app.server
app.config.suppress_callback_exceptions = True


@app.server.route('/static/<resource>')
def serve_static(resource):
    return flask.send_from_directory(STATIC_PATH, resource)
