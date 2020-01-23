from .helper import slider_and_label
import dash_html_components as html


slider_wind_speed = slider_and_label('wind_speed', 0, 100, 0.5, 'Wind Speed (m/s)')
slider_altitude = slider_and_label('altitude', 0, 100, 0.5, 'Altitude (m)')
slider_line_length = slider_and_label('line_length', 0, 100, 0.5, 'Line Length (m)')

fly_components = html.Div([
    slider_wind_speed,
    slider_altitude,
    slider_line_length
])