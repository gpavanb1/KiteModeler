import dash

app = dash.Dash(__name__)
app.title = 'Kite Modeler - Reboot'
server = app.server
app.config.suppress_callback_exceptions = True
