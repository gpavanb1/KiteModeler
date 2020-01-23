from .helper import slider_and_label
import dash_html_components as html


slider_h1 = slider_and_label('h1', 0, 100, 0.5, 'Top to Intersection (H1 - cm)', 12.7)
slider_h2 = slider_and_label('h2', 0, 100, 0.5, 'Intersection to Bottom (H2 - cm)', 25.4)
slider_w1 = slider_and_label('w1', 0, 100, 0.5, 'Side-to-Side (W1 - cm)', 25.4)

geometry_components = html.Div([
    slider_h1,
    slider_h2,
    slider_w1
])