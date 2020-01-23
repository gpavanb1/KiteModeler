from .helper import slider_and_label
import dash_html_components as html


slider_b = slider_and_label('b', 2.0, 100, 0.5, 'Bridle Length (B - cm)', 39.37)
slider_k = slider_and_label('k', 2.0, 100, 0.5, 'Knot Length (K - cm)', 30.48)

bridle_components = html.Div([
    html.Br(),
    slider_b,
    slider_k
])