from .helper import slider_and_label
import dash_html_components as html


slider_h1 = slider_and_label('h1', 0, 100, 0.5, 'H1')
slider_h2 = slider_and_label('h2', 0, 100, 0.5, 'H2')
slider_w1 = slider_and_label('w1', 0, 100, 0.5, 'W1')

geometry_components = html.Div([
    slider_h1,
    slider_h2,
    slider_w1
])