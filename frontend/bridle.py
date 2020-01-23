from .helper import slider_and_label
import dash_html_components as html


slider_b = slider_and_label('b', 0, 100, 0.5, 'Bridle Length (B - cm)', 35)
# TODO : Set bridle larger than knot
slider_k = slider_and_label('k', 0, 100, 0.5, 'Knot Length (K - cm)', 30)

bridle_components = html.Div([
    slider_b,
    slider_k
])