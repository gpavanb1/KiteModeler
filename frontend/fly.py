from .helper import slider_and_label
import dash_html_components as html
import dash_bootstrap_components as dbc


slider_wind_speed = slider_and_label('wind_speed', 0, 10, 0.05, 'Wind Speed (m/s)', 3.0)
slider_altitude = slider_and_label('altitude', 0, 5000, 20, 'Altitude (m)', 0)
slider_line_length = slider_and_label('line_length', 0, 2000, 10, 'Line Length (m)', 50)

fly_components = html.Div([
    html.Br(),
    dbc.Row([
        dbc.Col([
            slider_wind_speed
        ]),
        dbc.Col([
            slider_altitude,
        ])
    ]),
    dbc.Row([
        dbc.Col([
            slider_line_length
        ]),
        dbc.Col([

        ])
    ])
])